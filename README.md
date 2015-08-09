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

# convert csv file to lua file

```python
#convert one csv file
#in root dir 
cd convert
python ./convert_csv_to_lua.py -csv ../testdata/reward.csv -out_dir ../testdata

#convert csv files in dir
python ./convert_csv_to_lua.py -dir ../testdata -out_dir ../testdata

```

