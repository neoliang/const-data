#const-data

 const-data is a free, open source tool, the target of this tool are:

 1.convert csv or excel to simple language specified data format.

 2.generate language speicfied reading codes
 
# csv or excel format
1. the first three rows are fixed
2. the first rows describes data which will be ignored in converting
3. the second row describes data name in this column
4. the third row describes data type in this column: validate types are:

    a. int

    b. float
    
    c. string
    
    d. json
    
    e. comment: the comment type of column will be ignored in converting
    
    f. empty: the type of column of empty type  will be int

5. examples:


  id | 触发类型 | 触发id | 奖励 | 备注 | 其它
  -------- | :------------: | :------------: | :------------------:| :------------------:| :------------------:
  id |trigger_type|trigger_id|reward|comment|extra
     |string|int|json|comment|float
  1 |piece|26|{"yellow":2}|泥土消除奖励|0
  2 |piece|27|{"diamond:1}|钻石消除奖励|10.5


  a. the type of id-column is int because it's empty

# converting csv file to lua file

```python
#convert one csv file
#in root dir 
cd convert
python ./convert.py -file ../testdata/reward.csv -out_dir ../testdata -if csv -of lua

#convert csv files in dir
python ./convert.py -dir ../testdata -out_dir ../testdata -if csv -of lua

```

# converting csv file to json file

```python
#convert one csv file
#in root dir 
cd convert
python ./convert.py -file ../testdata/reward.csv -out_dir ../testdata -if csv -of json

#convert csv files in dir
python ./convert.py -dir ../testdata -out_dir ../testdata -if csv -of json

```

#converting excel to other files

1.the command line is almost same as convert csv excpe the option -if is excel

2.you must install xlrd using pip as following:

```pyton
pip install xlrd
```

#command line usage:

```text
  usage: python ./convert.py -if input_format -of output_format -file input_file -out_dir lua_dir
  python ./convert_csv_to_lua.py -if input_format -of output_format -dir csv_dir -out_dir lua_dir

  options:  
    -if:    input file format : csv or excel
    -of:    output file format lua,json
    -dir:     convert files in dir
    -file:    convert file
    -out_dir: the dir of output files
    -h print: this message  

```

#reading code:

reading code are in languages dir

#lua reading

1.the reading interface is constData.lua which dependent to load.lua

2.test.moon is used for testing constData,to run the test you must install [busted](http://olivinelabs.com/busted) framework

lua reading examples:
```lua
local constData = require 'constData'
constData.set_data_dir('../../testdata/')

--find records 
local ls = constData.find('reward',function(r) return r.trigger_type == 'piece' end)
for _,r in ipairs(ls) do
  print(r)
end

--find one, return nil or record
local record = constData.find_one('reward',function(r)return r.trigger_type == 'piece' end)
print(record)

--find by id return nil or record
local record = constData.find_by_id('reward',1)
print(record)
```



