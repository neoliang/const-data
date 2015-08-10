

local _data_dir = ''
local _name_to_tables = {}
local _name_to_hash_tables = {}
local load = require 'load'

local function load_table( tName )
	local ct = _name_to_tables[tName]	
	if ct then
		return ct
	end
	ct = load.load(_data_dir ..  tName .. '.lua' )
	assert(ct)
	_name_to_tables[tName] = ct
	if #ct > 0 and ct[1].id ~= nil then
		local ct_hash = {}
		for i,v in ipairs(ct) do
			ct_hash[v.id] = v
		end
		_name_to_hash_tables[tName] = ct_hash
	end
	return ct
end

local function get_table( tName )
	local ct = _name_to_tables[tName]
	if ct == nil then
		ct = load_table(tName)
	end
	return ct
end
local function get_hash_table( tName )
	local ct_hash = _name_to_hash_tables[tName]
	if ct_hash == nil then
		load_table(tName)
		ct_hash = _name_to_hash_tables[tName]
	end
	return ct_hash
end

local function reload_table( tName )
	_name_to_hash_tables[tName] = nil
	_name_to_tables[tName] = nil
	load_table(tName)
end

local function reload_all(  )
	_name_to_tables = {}
	_name_to_hash_tables = {}
end

local function find( tName,cmp )
	local results = {}
	local ct = get_table(tName)
	if ct == nil then
		print('table',tName ,'does not exsit')
		return results
	end

	for i,v in ipairs(ct) do
		if cmp(v) then
			table.insert(results,v)
		end
	end
	return results
end

local function find_one( tName,cmp )
	local results = find(tName,cmp)
	if #results > 0 then
		return results[1]
	end
end

local function find_by_id( tName,id )
	local ct_hash = get_hash_table(tName)
	if ct_hash then
		return ct_hash[id]
	end
end

local function set_data_dir( dir )
	_data_dir = dir
	if string.sub(_data_dir,string.len(_data_dir)) ~= '/' then
		_data_dir = _data_dir .. '/'
	end
end

return{
	find = find,
	find_one = find_one,
	find_by_id = find_by_id,
	get_table = get_table,
	get_hash_table = get_hash_table,
	set_data_dir = set_data_dir,
	reload_table = reload_table,
	reload_all = reload_all,
	load_table = load_table
}