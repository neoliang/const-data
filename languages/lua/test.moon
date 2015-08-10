


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
