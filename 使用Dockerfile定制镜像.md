## 使用Dockerfile定制镜像
> 在开发中，docker是极其方便的，使开发者不必再担心因为不同环境而导致的各种问题，实现了一次创建
或配置，可以在任意地方运行。同时，通过阅读Dockerfile，可以使开发人员快速的了解项目的运行环境，
而且也方便运维人员进行自动化部署。
### 通过一个例子介绍一下Dockerfile
- 这个是我之前写的一个简单的Dockerfile
```
# 这里指定基础镜像
FROM python:3.7.4
# 拷贝文件到指定目录
COPY sources.list /etc/apt/sources.list
COPY . /parser-permit-report
# 指定工作目录，也就是接下来所进行的命令操作都在该目录下进行
WORKDIR /parser-permit-report
# 执行shell命令
RUN pip install -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt
# 默认的容器主进程的启动命令的。docker run 启动镜像时如果指定了其他命令，该命令不执行。
CMD ["python", "main.py"]
```
其实就是开发时，在一个新的物理机上所做的一些操作，在编写Dockerfile之前，我们可以通过基础镜像启动一个容器，然后在容器中执行一些操作，将所有的操作记录下来，成功的把项目跑起来后，整合所有操作到Dockerfile中，最后再通过build构建镜像，docker run启动容器，来测试Dockerfile是否ok。
