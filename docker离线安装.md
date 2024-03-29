## install docker engine  
[Install Docker Engine from binaries](https://docs.docker.com/engine/install/binaries/#install-static-binaries)
## 注意事项  
- 默认的docker根目录可能存在空间不足的情况，注意修改
```
dockerd --data-root /dev/docker_store
```
或者直接修改配置文件：
```
vim /etc/docker/daemon.json
```
```json
{
  "data-root": "path"
}

```

- 查看docker 默认的根目录
```
docker info | grep 'Root Dir'
```
## 开机自启动配置
-  systemd docker.service
``` shell
vim /etc/systemd/system/docker.service
```
```
[Unit]
Description=Docker Application Container Engine
Documentation=https://docs.docker.com
After=network-online.target firewalld.service
Wants=network-online.target
  
[Service]
Type=notify
# the default is not to use systemd for cgroups because the delegate issues still
# exists and systemd currently does not support the cgroup feature set required
# for containers run by docker
ExecStart=/usr/bin/dockerd
# -H tcp://0.0.0.0:2375 -H unix://var/run/docker.sock
ExecReload=/bin/kill -s HUP $MAINPID
# Having non-zero Limit*s causes performance problems due to accounting overhead
# in the kernel. We recommend using cgroups to do container-local accounting.
LimitNOFILE=infinity
LimitNPROC=infinity
LimitCORE=infinity
# Uncomment TasksMax if your systemd version supports it.
# Only systemd 226 and above support this version.
#TasksMax=infinity
TimeoutStartSec=0
# set delegate yes so that systemd does not reset the cgroups of docker containers
Delegate=yes
# kill only the docker process, not all processes in the cgroup
KillMode=process
# restart the docker process if it exits prematurely
Restart=on-failure
StartLimitBurst=3
StartLimitInterval=60s
  
[Install]
WantedBy=multi-user.target
```
- grant privilege
```shell
chmod +x /etc/systemd/system/docker.service

systemctl daemon-reload   //重载systemd下 xxx.service文件
systemctl start docker       //启动Docker
systemctl enable docker.service   //设置开机自启
```
- testing  docker
```shell
systemctl status docker   //查看Docker状态
docker -v                       //查看Docker版本
```
- reference  
[centos7离线安装docker](https://www.cnblogs.com/xiaochina/p/10469715.html)
## docker-compose 离线安装  
[doc](https://docs.docker.com/compose/install/standalone/#on-linux)
