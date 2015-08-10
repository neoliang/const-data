


describe 'test const data',->
	constData = nil
	setup ()->
		constData = require 'constData'
		constData.set_data_dir('../../testdata/')
	it 'load reward',->
		assert.is_truthy(constData)
		assert.is_truthy(constData.load_table('reward'))
	it 'get reward_excel',->
		assert.is_truthy(constData.get_table('reward_excel'))
		assert.is_truthy(constData.get_hash_table('reward_excel'))

	it 'find',->
		ls = constData.find 'reward',(r)-> r.trigger_type == 'piece'
		assert.are.equal(type(ls),'table')
		assert.is_true(#ls > 0)
		ls = constData.find 'reward',()->false
		assert.are.equal(#ls,0)
	it 'find_one',->
		r = constData.find_one 'reward',(t)->return t.trigger_type == 'piece'
		assert.is_truthy(r)
		assert.is_truthy(r.id)
		assert.is_truthy(r.trigger_type)
		r = constData.find_one 'reward',()->false
		assert.is_nil(r)
	it 'find_by_id',->
		r = constData.find_by_id 'reward',1
		assert.are.equal(r.id,1)
	it 'get_table and get_hash_table',->
		ls = constData.get_table 'reward'
		assert.is_truthy(ls)
		ls = constData.get_hash_table 'reward_excel'
		assert.is_truthy(ls)