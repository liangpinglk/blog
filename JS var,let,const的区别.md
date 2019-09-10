## JS var,let,const的区别
>逛知乎看到的，自己之前理解的也不是很透彻，该[文章](https://zhuanlan.zhihu.com/p/82005698)通过介绍JS引擎解析不同声明方式变量的过程，让人对三者的区别有了更好的了解。
### 通过var声明的变量过程
``` js
console.log(a);//输出结果为 undefined
var a = 'xu';
console.log(a);//输出结果为 xu
```
#### 过程如下
1. var声明的变量会提升到最顶部，创建出a变量​
2. 创建完a变量后会初始化为undefined
3. 开始执行代码
4. 将变量值赋值给a变量

所以，为什么在var声明变量之前输出这个变量为undefined的原因就一目了然了
### 通过let声明变量的过程
``` js
let a = 'xu1'//1
{
    console.log(a);//2
	//抛出错误Uncaught ReferenceError: Cannot access 'a' before initialization
    let a = 'xu2';//3
    a = 'xu3'//4
}
let a = 'xu4'//5
//Uncaught SyntaxError: Identifier 'a' has already been declared
```
1. let声明变量a
2. 块作用域内a未声明会报错
3. 块作用域内let声明变量a
4. 块作用域内对变量进行重新赋值
5. 变量a被let声明后再次声明，会报错，被let声明的变量无法重复声明

### 通过const声明的变量
``` js
const a = 123;
console.log(a);
a = 321;
//Uncaught TypeError: Assignment to constant variable.
```
> const 和 let只有一个区别，那就是 const 声明变量的过程只有两步创建和初始化，但没有赋值过程。因为没有赋值过程，所以无法给const声明的变量进行重新赋值，这就是为什么重新给变量赋值后会抛出错误的原因。
### const 和 let 具有块级作用域
``` js
{
   var a = 'xu1';
   let b = 'xu2';
   const c = 'xu3';
}
console.log(a);
//输出结果 xu1
console.log(b);
//抛出错误 ReferenceError: b is not defined
console.log(c);
//抛出错误 ReferenceError: c is not defined
```
由此可见，const 和 let 声明的变量只限于当前作用域，在外部作用域是无法访问到的，那么另一个问题就来了，它们两者声明的变量是属于window呢？
``` js
let a = 'xu1'
const b = 'xu2'
var c = 'xu3'
console.log(window.a)//undefined
console.log(window.b)//undefined
console.log(window.c)//xu3
```
在全局作用域中使用var或者不使用var声明的变量都是属于window的，而let和const不是
