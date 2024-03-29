## git rebase 

### 修改某次提交
![p1](picture/git-rebase/p1.png)
初始仓库如上图，我们修改 提交 ‘3’, 执行命令
> [!TIP]
> 如果要改变第一次的提价内容，那么应该执行命令 ``` git rebase -i --root ```

```
git rebase -i HEAD~2
```
弹出如下图，修改pick 为r(reword)，退出并保存  
![p2](picture/git-rebase/p2.png)  
弹出下图commit信息编辑框，将提交内容修改为‘three’，退出并保存  
![p3](picture/git-rebase/p3.png)  
修改后的效果如下  
![p4](picture/git-rebase/p4.png) ![p5](picture/git-rebase/p5.png)

### 合并两次提交
![p4](picture/git-rebase/p4.png)
初始仓库信息如上图，执行命令
```
git rebase -i HEAD~3
```
分别修改为r 和 s
![p6](picture/git-rebase/p6.png)
然后保存会弹出编辑框
![p7](picture/git-rebase/p7.png)
编辑后推出，效果如下
![p8](picture/git-rebase/p8.png)
