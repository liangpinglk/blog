openresty 有封装好的容器，我这里为了学习，自己拉了一个Ubuntu的基础镜像， 在此环境中，进行openresty的学习(如果不是在容器中进行学习开发的，记得有的命令会提示权限问题，记得使用root权限，命令前加sudo)。
``` bash
docker run -v /home/lmf/Develop/lua_develop:/lua_develop --name lua_develop -p 81:80 --restart always -d ubuntu:20.04 /bin/sh -c "while true; do echo hello world; sleep 1; done"
```

**本文有关openresty的内容，皆是出自openresty官方文档，稍微有一点更改与补充，文中内容出处都标出了超链接，可以点击查看原文，以下所有代码在[这里](https://github.com/liangpinglk/openresty-practice)可以找到**
## 安装
[OpenResty® Linux 包](https://openresty.org/cn/linux-packages.html)
``` bash
# 安装需要的工具
apt-get install -y lsb-release 
# 在系统中添加openresty的apt仓库
apt-get -y install --no-install-recommends wget gnupg ca-certificates
#  导入openresty的 GPG 密钥：
wget -O - https://openresty.org/package/pubkey.gpg | apt-key add -
# 添加官方 APT 仓库：
echo "deb http://openresty.org/package/ubuntu $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/openresty.list
# 安装openresty
apt update
apt-get -y install openresty
```
## Hello World
原文：[Hello World](https://openresty.org/cn/getting-started.html)
- 创建开发目录(此后所有的命令执行都在work目录下)
``` bash
mkdir ~/work
cd ~/work
mkdir logs/ conf/
```
- 在conf 目录下添加文件nginx.conf 
``` 
worker_processes  1;
error_log logs/error.log;
events {
    worker_connections 1024;
}
http {
    server {
        listen 80;
        location / {
            default_type text/html;
            content_by_lua_block {
                ngx.say("<p>hello, world</p>")
            }
        }
    }
}
```
- 启动nginx 服务
    - 配置环境变量
    ``` bash
    PATH=/usr/local/openresty/nginx/sbin:$PATH
    export PATH
    ```
    - 启动服务
    ``` bash
    nginx -p `pwd`/ -c conf/nginx.conf
    ```
    - 访问
    ``` bash
    root@7668fd5c1cfc:/lua_develop/work# curl 127.0.0.1
    <p>hello, world</p>
    ```
至此，我们就成功启动了第一个openresty 服务

## 基于openresty 的动态路由
原文：[基于openresty 的动态路由](https://openresty.org/cn/dynamic-routing-based-on-redis.html)
- 准备redis
> 使用docker创建一个redis容器
``` bash
docker run --name myredis -p 6379:6379 --restart always -d redis redis-server
```
- nginx conf(dynamic-routing-based-on-redis.conf)
``` 
worker_processes  1;
error_log logs/error.log info;

events {
    worker_connections 1024;
}

http {
    upstream apache.org {
        server apache.org;
    }

    upstream nginx.org {
        server nginx.org;
    }

    server {
        listen 80;

        location = /redis {
            internal;
            set_unescape_uri $key $arg_key;
            redis2_query get $key;
            redis2_pass 192.168.179.130:6379;
        }

        location / {
            set $target '';
            access_by_lua '
                local key = ngx.var.http_user_agent
                local res = ngx.location.capture(
                    "/redis", { args = { key = key } }
                )

                print("key: ", key)

                if res.status ~= 200 then
                    ngx.log(ngx.ERR, "redis server returned bad status: ",
                        res.status)
                    ngx.exit(res.status)
                end

                if not res.body then
                    ngx.log(ngx.ERR, "redis returned empty body")
                    ngx.exit(500)
                end

                local parser = require "redis.parser"
                local server, typ = parser.parse_reply(res.body)
                if typ ~= parser.BULK_REPLY or not server then
                    ngx.log(ngx.ERR, "bad redis response: ", res.body)
                    ngx.exit(500)
                end

                print("server: ", server)

                ngx.var.target = server
            ';

            proxy_pass http://$target;
        }
    }
}
```
- 启动服务
    - 首先进入在redis中添加数据
    ```
    192.168.179.130:6379> set foo apache.org
    OK
    192.168.179.130:6379> set bar nginx.org
    OK
    ```
    - 停止之前的服务（如果有的话）
    ``` bash
    nginx -p `pwd` -s stop
    ```
    - 启动服务
    ``` 
    root@7668fd5c1cfc:/lua_develop/work# nginx -p `pwd`/ -c conf/dynamic-routing-based-on-redis.conf 
    ```
- 测试
``` bash
curl --user-agent foo localhost
curl --user-agent bar localhost
```
## 在openresty中使用luarocks
> LuaRocks 是一个部署和管理 Lua 模块的系统。
- 安装
    - luajit 环境变量
    ``` bash
    PATH=/usr/local/openresty/luajit/bin:$PATH
    export PATH
    ```
    - 安装需要的包
    ``` bash
    apt install -y zip mak
    ```
    - 下载并安装luarocks，注意下载[最新版本](https://github.com/luarocks/luarocks/wiki/Download)
    ```
    wget https://luarocks.org/releases/luarocks-3.5.0.tar.gz
    tar -xzvf luarocks-2.0.4.1.tar.gz
    cd luarocks-2.0.4.1/
    ./configure
    make
    make install
    ```
- Example 通过luarocks安装lua MD5 库
    - 安装
    ```
    apt install -y gcc
    luarocks install md5
    ```
    - 配置openresty应用
    同样的work/conf目录下创建md5.conf
    ```
    worker_processes  1;   # we could enlarge this setting on a multi-core machine
    error_log  logs/error.log error;

    events {
        worker_connections  1024;
    }

    http {
        lua_package_path 'lua_src/?.lua;;';

        server {
            listen       80;
            server_name  localhost;

            location = /luarocks {
                content_by_lua '
                    local foo = require("foo")
                    foo.say("hello, luarocks!")
                ';
            }
        }
    }

    ```
    创建两个lua模块文件lua_src/foo.lua
    ``` lua
    module("foo", package.seeall)
    local bar = require "bar"
    ngx.say("bar loaded")
    function say (var)
        bar.say(var)
    end
    ```
    lua_src/bar.lua
    ``` lua
    module("bar", package.seeall)
    local rocks = require "luarocks.loader"
    local md5 = require "md5"
    ngx.say("rocks and md5 loaded")
    function say (a)
        ngx.say(md5.sumhexa(a))
    end
    ```
    - 开启nginx 服务
    ```
    nginx -p `pwd`/ -c conf/md5.conf
    ```
    - 测试
    第一次运行
    ``` 
    root@7668fd5c1cfc:/# curl http://localhost/luarocks
    rocks and md5 loaded
    bar loaded
    85e73df5c41378f830c031b81e4453d2
    ```
    后面再运行
    ```
    root@7668fd5c1cfc:/# curl http://localhost/luarocks
    85e73df5c41378f830c031b81e4453d2
    ```
    后续再运行，产生的数据和之前一样，这是因为lua nginx module 默认缓存了已经加载过的lua模块，并且这些叔叔数据的代码时在lua加载时运行的，因此他们将不会再执行。
    - ab 测试
    安装工具
    ``` bash
    apt-get install -y apache2-utils
    ```
    测试
    ```
    ab -c10 -n50000 http://127.0.0.1/luarocks
    ```