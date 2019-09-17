# SQL性能优化
> 在平时工作中，经常和数据打交道，数据量很小时一般查询都会很快（即使没怎么优化），但是当数据量很
大时，就很容易遇到性能问题，目前我工作中所使用的的数据大概500多G（数据会不断增长，目前使用分区表
存储）。因此，认真优化每一个SQL对性能提升至关重要。
### 1.index
索引是我们常用的优化方式，但是，需要我们了解索引在数据库中是如何运作的，否则会起到反作用，关于索
引，之后会在另一篇文章中做介绍。

### 2.Symbol Operator
我们常用>,<,=,!= 等的运算符号在我们的查询里，我们可以透过已经建立过index索引的列来加快查询的速
度。例如：
``` SQL
SELECT * FROM TABLE WHERE COLUMN > 16
```
现在，上面这个查询式没优化的。因为DBMS必须去找所有大于小于16的所有资料。我们可以把它改写成如下：
``` SQL
SELECT * FROM TABLE WHERE COLUMN >= 15
```
这样的话DBMS就会直接跳到15去，然后直接找比15小的出来。
### 3.Wildcard
在sql里面我们提供了％来做模糊查询，然而这个％的查询会拖慢你的查询速度，特别是当你的table非常大
的时候。我们可以透过前后缒的方式优化我们的查询而不要全部都使用，例如：
``` sql
# Full wildcard
SELECT * FROM TABLE WHERE COLUMN LIKE '%hello%';
# Postfix wildcard
SELECT * FROM TABLE WHERE COLUMN LIKE 'hello%';
# Prefix wildcard
SELECT * FROM TABLE WHERE COLUMN LIKE '%hello';
```
这个列必须要做index才比较会有效果
```
ps:对一个百万条资料的table做Full wildcard会killing这个数据库
```
### 4.NOT Operator
尝试去避免使用NOT在你的sql里面，用正向的的方式查询会快很多。例如用LIKE, IN, EXIST or = 符
号而不要使用NOT LIKE, NOT IN, NOT EXIST or != 符号。使用反向符号会导致数据库会去搜寻每一
条数据去确定他都是真的不属于或不存在这个table。相反地​​，假如有这条数据的话，用正向的方式查询会直
接的跳到这个查询结果。
### 5.Wildcard VS Substr
假如要查询特定的索引的话，如果那个列有做index，那么最好使用wildcard 而不是substr 例如
``` SQL
# 不好的
SELECT * FROM TABLE WHERE  substr ( COLUMN, 1, 1 ) = 'value'.
```
上面这个查询会去substr每一条数据就为了找'value'这个字串，而
``` SQL
SELECT * FROM TABLE WHERE  COLUMN = 'value%'.
```
Wildcard 会找的比较快，假如value是在每一条数据的最前面的话
### 6.Index Unique Column
有些数据库例如MySQL对于unique 和indexed的列搜寻速度比较好。因此假如这个列是unique的，最好记
得对他们做index。但是要是那个列根本就没有搜寻的必要的话，就不要做index，即使他们是unique的。
### 7.Max and Min Operators
Max和Min是为了找到最大跟最小值用的，我们在已经做index的列使用他们两个的话，速度会很快。但是假如
这个列只想要查询最大跟最小值的话，就不要去做index了这不划算，就好比为了一棵树而放弃整座森林一样。
为了他而让整个数据库效能降低。
### 8.Types
尽量使用最有效（最小的）数据类型。用太大的数据类型去存很小的数据是不必要甚至是危险的。用较小的数
据类型可以得到比较小的table空间。例如用MEDIUMINT通常就比用INT好，因为MEDIUMINT少了25%的空间，
还有在储存email或是少数资料时VARCHAR还是比longtext好。
### 9.Primary Index
主要的Primary列通常都用来做index用的，所以尽可能的让他越小越好。这让DBMS能更简单有效的去查询每
一条数据。
### 10.Limit The Result
对于数据量较大时，采取分页操作（offset limit）。
### 11.Use Default Value
如果你使用MySQL时，尽量使用Default值，Insert values 只有当值跟DEfalut不一样时才用，在mysql
里，这样可以减少一次解析的时间并增快写入的速度。
### 12.In Subquery
尽量少使用子查询，如果非要用，可以用join查询来替代
### 13.Utilize Union instead of OR
在MySQL里面，用了or 会让整个查询的速度优势不见，就算做index也没啥太大的效用
```sql
SELECT * FROM TABLE WHERE COLUMN_A = 'value' OR COLUMN_B ='value'
```
我们可以把上面透过union改写成下面这样
```sql
SELECT * FROM TABLE WHERE COLUMN_A = 'value'
UNION
SELECT * FROM TABLE WHERE COLUMN_B = 'value'
```
这样跑比较快。

如果or条件较多的话，可以用in取代or。
### 14.用EXISTS替代IN、用NOT EXISTS替代NOT IN
### 15.避免在索引列上使用计算：
```SQL
WHERE SAL*12>25000;
```
### 16.在过滤条件中，可以过滤掉最大数量记录的条件必须放在where子句的末尾
FROM子句中写在最后的表(基础表，driving table)将被最先处理，在FROM子句中包含多个表的情况下，
你必须选择记录条数最少的表作为基础表。如果有三个以上的连接查询，那就需要选择交叉表 (intersection table)
作为基础表，交叉表是指那个被其他表所引用的表;
### 17.避免在索引列上使用IS NULL和IS NOT NULL;
### 18.总是使用索引的第一个列;
### 19.用UNION-ALL替代UNION;
### 20.避免改变索引列的类型
SELECT…FROM EMP WHERE EMPNO=’123’，由于隐式数据类型转换，to_char(EMPNO)=’123’，因此，
将不采用索引，一般在采用字符串拼凑动态SQL语句出现;
### 21.避免使用困难的正规表达式。
例如select * from customer where zipcode like “98___”，即便在zipcode上建立了索引，在
这种情况下也还是采用顺序扫描的方式。如果把语句改成select * from customer where zipcode>
”98000″，在执行查询时就会利用索引来查询，显然会大大提高速度;
### 22.尽量明确的完成SQL语句。
尽量少让数据库工作。比如写SELECT语句时，需要把查询的字段明确指出表名。尽量不要使用SELECT * 语
句。组织SQL语句的时候，尽量按照数据库的习惯进行组织。

### 参考：
- http://blog.davidou.org/archives/609
- http://www.penglixun.com/tech/database/improve_sql_efficiency_16_ways.html
