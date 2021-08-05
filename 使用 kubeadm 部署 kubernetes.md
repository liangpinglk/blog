## 使用kubeadm部署k8s
### 说明
- 系统环境
```shell
lmf@lmf:~$ cat /etc/issue
Ubuntu 18.04.5 LTS \n \l

lmf@lmf:~$ cat /proc/meminfo | grep MemTotal
MemTotal:        4015812 kB

lmf@lmf:~$ cat /proc/cpuinfo | grep model\ name
model name      : Intel(R) Core(TM) i5-10500 CPU @ 3.10GHz
model name      : Intel(R) Core(TM) i5-10500 CPU @ 3.10GHz
model name      : Intel(R) Core(TM) i5-10500 CPU @ 3.10GHz
model name      : Intel(R) Core(TM) i5-10500 CPU @ 3.10GHz
```
### 安装docker
- 该步骤参考[清华大学 Docker Community Edition 镜像使用帮助](https://mirrors.tuna.tsinghua.edu.cn/help/docker-ce/)， 如果已安装请忽略
- 确保 Cgroup Driver 为systemed  
![图一：docker 信息](https://raw.githubusercontent.com/liangpinglk/note/master/picture/deploy-k8s/docker-info.png)
- 设置docker 的Cgroup Driver 为systemd
```shell
sudo mkdir -p /etc/docker

sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://m0m3chw3.mirror.aliyuncs.com"],
  "exec-opts": ["native.cgroupdriver=systemd"]
}
EOF

sudo systemctl daemon-reload
sudo systemctl restart docker
```
###  安装kubelet kubeadm kubectl
```shell
sudo apt-get update && sudo apt-get install -y apt-transport-https
curl https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | sudo apt-key add -

cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main
EOF

sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
```
### 部署
```
 sudo kubeadm init   --apiserver-advertise-address=192.168.60.51   --image-repository registry.aliyuncs.com/google_containers    --pod-network-cidr=10.244.0.0/16
```
> --apiserver-advertise-address 填本机ip  
 
部署成功后会显示如下：

 ![图二：k8s部署成功提示](https://raw.githubusercontent.com/liangpinglk/note/master/picture/deploy-k8s/success-info.png) 

### 


### 参考
#### 使用到的参考
- [使用 kubeadm 部署 kubernetes](https://yeasy.gitbook.io/docker_practice/setup/kubeadm)
- [kubernetes安装最新步骤 centos7](http://gaodongfei.com/archives/centos7-install-kubernetes)
- [Ubuntu 20.04 LTS 安装 k8s 报错 failed to pull image coredns:v1.8.0](https://blog.csdn.net/yilovexing/article/details/118487858)
#### 下面这个参考，安装过程中遇到过类似的问题，后来服务器重装，按照本文的步骤，没有下面的问题了
- [初始化kubeadm init报curl -sSL http://localhost:10248/healthz‘ failed with error: Get http://localhost](https://blog.csdn.net/weixin_41831919/article/details/108330129)