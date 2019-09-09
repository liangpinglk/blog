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

### on和where用法的区别
```
之前做左连接查询，发现on中的过滤条件不起作用，最后网上查了下，是因为左连接on条件会忽略左表的条件，
如果要对左表数据进行过滤，则需要用where过滤。右连接同理。
```
