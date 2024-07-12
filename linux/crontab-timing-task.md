## crontab 定时任务
> 通过crontab 命令，我们可以在固定的间隔时间执行指定的系统指令或 shell script脚本。时间间隔的单位可以是分钟、小时、日、月、周及以上的任意组合。这个命令非常适合周期性的日志分析或数据备份等工作。

### 命令格式
``` shell
crontab [-u user] file crontab [-u user] [ -e | -l | -r]
```

### 命令参数
- -u user：用来设定某个用户的crontab服务；
- file：file是命令文件的名字,表示将file做为crontab的任务列表文件并载入crontab。如果在命令行中没有指定这个文件，crontab命令将接受标准输入（键盘）上键入的命令，并将它们载入crontab。
- -e：编辑某个用户的crontab文件内容。如果不指定用户，则表示编辑当前用户的crontab文件。
- -l：显示某个用户的crontab文件内容，如果不指定用户，则表示显示当前用户的crontab文件内容。
- -r：从/var/spool/cron目录中删除某个用户的crontab文件，如果不指定用户，则默认删除当前用户的crontab文件。
- -i：在删除用户的crontab文件时给确认提示。

### crontab的文件格式
分 时 日 月 星期 要运行的命令
- 第1列分钟0～59
- 第2列小时0～23（0表示子夜）
- 第3列日1～31
- 第4列月1～12
- 第5列星期0～7（0和7表示星期天）
- 第6列要运行的命令

### 常用方法

#### 创建crontab 文件
```shell
# 通过vi在文件中输入想要执行的命令
➜  ~ vi liantpingcron
# 将文件提交给crontab进程
➜  ~ crontab liantpingcron
```
#### 列出crontab 任务
``` shell
# 文件中的命令，每分钟执行一次
 ➜  ~ crontab -l
 * * * * * date >> ~/test
# 查看执行结果
➜  ~ tail -f ~/test
Mon Oct  7 19:00:00 CST 2019
Mon Oct  7 19:01:00 CST 2019
Mon Oct  7 19:02:00 CST 2019
Mon Oct  7 19:03:00 CST 2019
Mon Oct  7 19:04:00 CST 2019
Mon Oct  7 19:05:01 CST 2019
```

#### 直接编辑命令执行定时任务
``` shell
➜  ~ crontab -e
```
执行后会通过系统默认编辑器进入编辑界面，然后可以正常输入定时任务了

#### 删除任务
``` shell
➜  ~ crontab -l
 * * * * * date >> ~/test
 * * * * * date >> ~/test
 * * * * * date >> ~/test
➜  ~ crontab -r
➜  ~ crontab -l
crontab: no crontab for liangping
```
如果要删除一个，可通过crontab -e 进入编辑页面，然后一个一个删除

### 使用实例
``` shell
# 实例1：每1分钟执行一次myCommand
 * * * * * myCommand
# 实例2：每小时的第3和第15分钟执行
3,15 * * * * myCommand
# 实例3：在上午8点到11点的第3和第15分钟执行
3,15 8-11 * * * myCommand
# 实例4：每隔两天的上午8点到11点的第3和第15分钟执行
3,15 8-11 */2  *  * myCommand
# 实例5：每周一上午8点到11点的第3和第15分钟执行
3,15 8-11 * * 1 myCommand
# 实例6：每晚的21:30重启smb
30 21 * * * /etc/init.d/smb restart
# 实例7：每月1、10、22日的4 : 45重启smb
45 4 1,10,22 * * /etc/init.d/smb restart
# 实例8：每周六、周日的1 : 10重启smb
10 1 * * 6,0 /etc/init.d/smb restart
# 实例9：每天18 : 00至23 : 00之间每隔30分钟重启smb
0,30 18-23 * * * /etc/init.d/smb restart
# 实例10：每星期六的晚上11 : 00 pm重启smb
0 23 * * 6 /etc/init.d/smb restart
# 实例11：每一小时重启smb
 * */1 * * * /etc/init.d/smb restart
# 实例12：晚上11点到早上7点之间，每隔一小时重启smb
0 23-7 * * * /etc/init.d/smb restart
```

### 注意事项
- 新创建的cron job，不会马上执行，至少要过2分钟才执行。如果重启cron则马上执行。
- 谨慎使用crontab -r。它从Crontab目录（/var/spool/cron）中删除用户的Crontab文件。
- 在crontab中%是有特殊含义的，表示换行的意思。
- crontab 是无法继承系统环境变量的
> 比如你运行一个容器，指定了很多env配置，但是，通过crontab跑起来的任务是无法读到设置的env配置的

### 参考
该内容主要从[这里](https://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/crontab.html)整理而来。
