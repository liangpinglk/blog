## Jsonp
>今天写爬虫抓取[上海科创板](http://kcb.sse.com.cn/disclosure/)数据时发现其接口是通过Jsonp来获取的，于是对此进行了下了解。
### 什么是Jsonp
>JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，而JSONP（JSON with Padding）则是JSON 的一种“使用模式”，通过这种模式可以实现数据的跨域获取。
### Jsonp跨域的原理
>在同源策略下，在某个服务器下的页面是无法获取到该服务器以外的数据的，但img、iframe、script等标签是个例外，这些标签可以通过src属性请求到其他服务器上的数据。利用script标签的开放策略，我们可以实现跨域请求数据，当然，也需要服务端的配合。当我们正常地请求一个JSON数据的时候，服务端返回的是一串JSON类型的数据，而我们使用JSONP模式来请求数据的时候，服务端返回的是一段可执行的JavaScript代码。
### 实例
我们要跨域请求某个服务器上的数据:
``` json
{ "name":"Bill Gates", "age":62, "city":"Seattle" }
```
为了方便举例实现，我在可用的服务器上放置了一个静态文件，其内容为：
```JavaScript
foo({ "name":"Bill Gates", "age":62, "city":"Seattle" });
```
然后，我写了一个简单的html进行测试，使用ajax 获取jsonp数据实现数据的跨域请求：
```html
<html>
<head>
	<script src="https://cdn.staticfile.org/jquery/3.4.1/jquery.min.js"></script>
</head>
<div>
	<button onclick="self_test()">test</button>
</div>

<script>
	function foo(data) {
		console.log(data)
	}

	function self_test() {
		$.ajax({
			type: "get",
			url: 'http://d.epmap.org/static/test.txt?callback=?',
			dataType: "jsonp",
			success: function(data) {
			}
		})
	}
</script>
</html>
```
打开测试html页面，打开调试工具，然后点击test按钮，可以看到如下结果：
![](https://raw.githubusercontent.com/liangpinglk/note/master/picture/jsonp/console_result.png)
![](https://raw.githubusercontent.com/liangpinglk/note/master/picture/jsonp/request_info.png)
### 参考链接
**参考**:[jquery ajax jsonp](https://www.w3cschool.cn/json/4z2r1plk.html)
