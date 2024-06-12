## centos7 yum无法正常工作
> 今天下午，领导让我处理个问题，说有个实习生使用的服务器yum无法使用了，让我帮着处理下。

我连接上服务器，看了下，报了类似下面的错误：
```
There was a problem importing one of the Python modules
required to run yum. The error leading to this problem was:
 
  No module named yum
```
我google了下，发现很多人说是python重新安装导致的，果然，是实习生自己重新安装了python，但是按照网上的说法，编辑/usr/bin/yum(whhich yum得到)，更改第一行为当前可用的pyhton，依然不行。我进入python终端，导入yum，依然提示没有module，于是我尝试着怎么安装yum包。在pypi上搜索了下yum，发现有一堆东西，不太清楚哪个是正确的，后来发现了个blog，和我遇到的问题几乎一样，于是按照blog上的提示试了下，果然ok。
### 卸载python
```shell
rpm -qa| grep python| xargs rpm -ev --allmatches --nodeps
whereis python |xargs rm -frv
```
### 卸载yum
```shell
rpm -qa|grep yum|xargs rpm -ev --allmatches --nodeps
whereis yum |xargs rm -frv
```
### 下载rmp包  
适用于centos7
```shell
wget http://mirrors.ustc.edu.cn/centos/7/os/x86_64/Packages/libxml2-python-2.9.1-6.el7_2.3.x86_64.rpm
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/libxml2-python-2.9.1-6.el7.4.x86_64.rpm
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/rpm-4.11.3-43.el7.x86_64.rpm
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/rpm-build-4.11.3-43.el7.x86_64.rpm
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/rpm-build-libs-4.11.3-43.el7.x86_64.rpm
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/rpm-libs-4.11.3-43.el7.x86_64.rpm
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/rpm-sign-4.11.3-43.el7.x86_64.rpm
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/rpm-python-4.11.3-43.el7.x86_64.rpm
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/python-2.7.5-88.el7.x86_64.rpm
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/dbus-python-devel-1.1.1-9.el7.x86_64.rpm
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/python-libs-2.7.5-88.el7.x86_64.rpm
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/python-pycurl-7.19.0-19.el7.x86_64.rpm
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/python-setuptools-0.9.8-7.el7.noarch.rpm
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/python-urlgrabber-3.10-10.el7.noarch.rpm
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/python-iniparse-0.4-9.el7.noarch.rpm
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/python-backports-1.0-8.el7.x86_64.rpm
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/python-backports-ssl_match_hostname-3.5.0.1-1.el7.noarch.rpm
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/python-chardet-2.2.1-3.el7.noarch.r
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/python-ipaddress-1.0.16-2.el7.noarch.rpm
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/python-kitchen-1.1.1-5.el7.noarch.rpm
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/python-virtualenv-15.1.0-2.el7.noarch.rpm
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/yum-3.4.3-167.el7.centos.noarch.rpm
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/yum-metadata-parser-1.1.4-10.el7.x86_64.rpm
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/yum-utils-1.1.31-53.el7.noarch.rpm
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/yum-plugin-fastestmirror-1.1.31-53.el7.noarch.rpm
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/yum-plugin-protectbase-1.1.31-53.el7.noarch.rpm
wget http://mirrors.163.com/centos/7/os/x86_64/Packages/yum-plugin-aliases-1.1.31-53.el7.noarch.rpm
```
### 安装更新rpm包
```shell
rpm -Uvh --force --nodeps --replacepkgs *.rpm
```
之后就可以正常使用了（如果不行可退出当前终端，重新进入再看下）
## 参考
[centos下重装yum的踩坑之旅](https://www.codenong.com/cs106649714/)