## Element ui table selection 分页支持保存已经选中的数据，同时支持随时删除选中的数据，并设置默认选择
> 今天遇到一个需求，有一个表格，这个表格的数据支持翻页，然后，用户可以每次选择数据，选择之后，下次再回到该页面时依然和之前一样的状态，包括选中和非选中的数据。

我想了下，主要就是两点：  
1、每页的数据必须一样。当筛选条件相等时，后端分页时，进行排序，这样就可以保证每页数据都一致了，这个简单。  
2、每次选中后，需要将选中的数据保存，然后再回到该页面时，将保存的已选中的数据再次设置为选中。问题就出在这一步，我在这一步遇到了问题。
### 实现默认选择
 其实这个Element UI [官方文档](https://element.eleme.cn/#/zh-CN/component/table#duo-xuan)有写如何实现默认选中，但是这个demo中默认的是直接使用当前tableData的数据来实现的。而我这里分页后，数据已经不是tableData里的数据了，然后我发现这样对于自带的toggleRowSelection方法实现默认选中时是无法实现的，即使你传入的obj数据看着k，v都和tableData中的数据一样，依然是不行的（这里我猜测是数据的空间位置不一样，而Element UI table 在实现时判断数据是否存在判断的是数据存储的空间位置，而不是判断k，v，下面例子中，其中的切换第二、三行，我把数据稍微改了下，就是为了证明我的猜测，这个只针对第一页数据。包括数组的indexOf方法也是同理）。

 这里举例一个上面说到的indexOf的例子：
 ```javaScript
test = [{a:'b'}, {c:'d'}, {e:'f'}]
 //这样存在 
test.indexOf(test[1])
// 1
// 不存在obj数组，其实按照我们的需求判断，应该是存在的，kv一致
test.indexOf({c:'d'})
// -1
 ```

既然不是tableData的数据，无法实现默认选中，那么我们可以传入tableData的数据呀，这里就需要我们通过保存每一页选中的数据，然后遍历tableData，判断遍历的到的数据是否和选中的数据相同，如果相同，那么调用toggleRowSelection方法传入tableData[i]，这样就能实现默认选中了。具体实现方式就是这样，就是真正实现的时候需要考虑细节，比较麻烦。

实现代码[Element-table.html](https://github.com/liangpinglk/blog/blob/master/demo/element-ui-table/Element-table.html)  
实现效果：
![效果演示](https://raw.githubusercontent.com/liangpinglk/blog/master/demo/element-ui-table/demo.gif)




