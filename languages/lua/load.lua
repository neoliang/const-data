local lfs = require('lfs')
local isfileExsit
isfileExsit = function(f)
  f = io.open(f, 'rb')
  if f then
    io.close(f)
    return true
  end
  return false
end
loadfilewithSearch = function(file)
  if isfileExsit(file) then
    return assert(loadfile(file))
  end
  if isfileExsit(file .. '.lua') then
    return assert(loadfile(file .. '.lua'))
  end
  if isfileExsit(file .. '.moon') then
    return assert(loadfile(file .. '.moon'))
  end
  for f in string.gmatch(package.path, '[^;]+') do
    local full = string.gsub(f, '?', file)
    if isfileExsit(full) then
      return assert(loadfile(full))
    end
  end
  print('cant load file in loadfilewithSearch', file)
  return nil
end
local load
load = function(file)
  local f = loadfilewithSearch(file)
  if f then
    return f()
  end
end
return {
  load = load
}
