## sql join
### 多种join
**参考**:[SQL 连接(JOIN)](https://www.w3schools.com/sql/sql_join.asp)

- JOIN（inner join）: 如果表中有至少一个匹配，则返回行
- LEFT JOIN: 即使右表中没有匹配，也从左表返回所有的行
- RIGHT JOIN: 即使左表中没有匹配，也从右表返回所有的行
- FULL JOIN：只要其中一个表中存在匹配，则返回行

![inner join](https://raw.githubusercontent.com/liangpinglk/note/master/picture/sql-join/img_innerjoin.gif)
![leftjoin](https://raw.githubusercontent.com/liangpinglk/note/master/picture/sql-join/img_leftjoin.gif)
![right join](https://raw.githubusercontent.com/liangpinglk/note/master/picture/sql-join/img_rightjoin.gif)
![full join](https://raw.githubusercontent.com/liangpinglk/note/master/picture/sql-join/img_fulljoin.gif)


### 多表join
**参考**:[SQL-用JOIN连接多个表](https://blog.csdn.net/qq_26593881/article/details/52104699)
```
select * from table1 inner join table2 on table1.id=table2.id
即：
FROM (((表1 INNER JOIN 表2 ON 表1.字段号=表2.字段号) INNER JOIN 表3 ON 表1.字段号=表3.字段号)
INNER JOIN 表4 ON Member.字段号=表4.字段号) INNER JOIN 表X ON Member.字段号=表X.字段号
```

- 例子(三表join)  
```
postgres=# select com.province, com.company_name, com.syear, m.name,f.name, f.created, f.max_value, f.max_unit from (nsmdb.crawlerapp_companies com inner join nsmdb.crawlerapp_monitor_points m on com.syear='2020' and m.company_id = com.distributed_key) inner join nsmdb.crawlerapp_monitor_infos f on  f.monitor_id = m.id limit 10;
 province |        company_name        | syear |   name   |      name      |            created            | max_value | max_unit 
----------+----------------------------+-------+----------+----------------+-------------------------------+-----------+----------
 陕西     | 米脂县银河水务有限责任公司 |  2020 | 排放明渠 | 总氮（以N计）  | 2020-03-03 21:19:30.121944+08 |           | 
 陕西     | 米脂县银河水务有限责任公司 |  2020 | 排放明渠 | 氨氮（NH3-N）  | 2020-03-03 21:19:30.341917+08 |           | 
 陕西     | 米脂县银河水务有限责任公司 |  2020 | 排放明渠 | 总磷（以P计）  | 2020-03-03 21:19:30.507474+08 |           | 
 陕西     | 米脂县银河水务有限责任公司 |  2020 | 排放明渠 | pH值           | 2020-03-03 21:19:30.705341+08 |           | 
 陕西     | 米脂县银河水务有限责任公司 |  2020 | 排放明渠 | 化学需氧量     | 2020-03-03 21:19:30.9279+08   |           | 
 陕西     | 米脂县银河水务有限责任公司 |  2020 | 排放明渠 | 总镉           | 2020-03-03 21:19:31.245837+08 |           | 
 陕西     | 米脂县银河水务有限责任公司 |  2020 | 排放明渠 | 总汞           | 2020-03-03 21:19:31.426495+08 |           | 
 陕西     | 米脂县银河水务有限责任公司 |  2020 | 排放明渠 | 五日生化需氧量 | 2020-03-03 21:19:31.578713+08 |           | 
 陕西     | 米脂县银河水务有限责任公司 |  2020 | 排放明渠 | 六价铬         | 2020-03-03 21:19:31.810691+08 |           | 
 陕西     | 米脂县银河水务有限责任公司 |  2020 | 排放明渠 | 动植物油       | 2020-03-03 21:19:31.967115+08 |           | 
(10 行记录)
```

### on和where用法的区别
```
之前做左连接查询，发现on中的过滤条件不起作用，最后网上查了下，是因为左连接on条件会忽略左表的条件，
如果要对左表数据进行过滤，则需要用where过滤。右连接同理。
```
