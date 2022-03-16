[TOC]
## podman容器使用显卡
系统信息：
```
Distributor ID:	Ubuntu
Description:	Ubuntu 20.04.1 LTS
Release:	20.04
Codename:	focal
```
### Install NVIDIA Container Toolkit
``` 
 sudo apt install nvidia-container-toolkit
```
### 添加hook文件
> 该文件默认不存在，需要自己手动添加，创建相关目录和文件，然后将内容拷贝到文件中
```
cat  /usr/share/containers/oci/hooks.d/oci-nvidia-hook.json
{
    "version": "1.0.0",
    "hook": {
        "path": "/usr/bin/nvidia-container-toolkit",
        "args": ["nvidia-container-toolkit", "prestart"],
        "env": [
            "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
        ]
    },
    "when": {
        "always": true,
        "commands": [".*"]
    },
    "stages": ["prestart"]
}

```
###  Rootless Containers Setup
> 该步骤是为了让让无root权限的用户，在使用podman时，可以使用显卡
```
sudo sed -i 's/^#no-cgroups = false/no-cgroups = true/;' /etc/nvidia-container-runtime/config.toml
```
### 测试
```
podman run --rm --security-opt=label=disable \
     --hooks-dir=/usr/share/containers/oci/hooks.d/ \
     nvidia/cuda:11.0-base nvidia-smi

Thu Mar 10 09:38:45 2022       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.32.03    Driver Version: 460.32.03    CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce GTX 108...  Off  | 00000000:09:00.0 Off |                  N/A |
| 23%   33C    P8     8W / 250W |   6306MiB / 11178MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   1  GeForce GTX 108...  Off  | 00000000:0A:00.0 Off |                  N/A |
| 57%   84C    P2   148W / 250W |   9625MiB / 11178MiB |     97%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   2  GeForce GTX 108...  Off  | 00000000:43:00.0 Off |                  N/A |
| 32%   50C    P8    11W / 250W |   6210MiB / 11178MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   3  GeForce GTX 108...  Off  | 00000000:44:00.0 Off |                  N/A |
| 30%   47C    P8    11W / 250W |  10688MiB / 11176MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
+-----------------------------------------------------------------------------+

```
### 总结
在以上步骤ok后，后续启动容器，只要需要在podman run 的时候添加 ` --security-opt=label=disable   --hooks-dir=/usr/share/containers/oci/hooks.d/ `这两个参数即可。
### 参考链接
[nvidia container toolkit install guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#podman)
