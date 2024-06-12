## 纯前端下载数据Excel文档
> 之前在工作中有个需求是前端下载数据，我下载格式为csv（[之前的blog](https://juejin.im/post/6844904020641841166)），但是，现在又有新的需求了，说用户想要下载的数据未Excel。我最初的想法是后端生成Excel，然后放到服务器上，返回给前端一个下载链接，这样实现下载Excel文档，但是这样又要改前端，又要改后端，而且有好多处都需要修改，想想就头疼。那么有没有简单省事的办法，能不能在现在的基础上不修改后端，只稍微修改前端。我谷歌查了下，发现了[sheetjs](https://github.com/SheetJS/sheetjs)

## 用法：
- [vue-cli](https://cli.vuejs.org/zh/guide/creating-a-project.html#vue-create) 创建一个新的项目
- 安装sheetjs
```
npm install xlsx
```
- 实现效果
![效果演示](https://raw.githubusercontent.com/liangpinglk/blog/master/demo/frontend_download/demo.gif)
- [demo](https://github.com/liangpinglk/blog/tree/master/demo/frontend_download/excel_demo)  
demo使用了Element ui,安装使用参考[官方文档](https://element.eleme.cn/#/zh-CN/component/installation)
## 参考
[纯前端实现excel表格导入导出](https://segmentfault.com/a/1190000011057149)