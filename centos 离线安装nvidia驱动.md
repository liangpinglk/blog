## 离线安装nvidia驱动
### 驱动下载
[download](https://www.nvidia.com/Download/index.aspx)

### 驱动安装
```
bash NVIDIA-Linux-x86_64-510.108.03.run
```
### 验证
```
nvidia-smi 
```
### 离线安装nvidia-container-runtime
- 在上网机更新nvidia-container-runtime的yum源
```
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-container-runtime/$distribution/nvidia-container-runtime.list | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-runtime.list
````
- 离线下载nvidia-container-runtime安装包
```
yum install nvidia-container-runtime --downloadonly --downloaddir=./
```
- 利用rpm进行安装
```
sudo rpm -ivh ./* --nodeps
```
### 离线安装docker-compose
- [Install Compose standalone](https://docs.docker.com/compose/install/standalone/)

### docker api支持使用gpu
```
sudo tee /etc/docker/daemon.json <<EOF
{
    "runtimes": {
        "nvidia": {
            "path": "/usr/bin/nvidia-container-runtime",
            "runtimeArgs": []
        }
    }
}
EOF
```
```
sudo pkill -SIGHUP dockerd
```

## Refence
- [CentOS离线安装docker和nvidia-container-runtime](https://www.jianshu.com/p/1402d88c300f) 