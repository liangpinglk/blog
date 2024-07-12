[apscheduler](https://apscheduler.readthedocs.io/)  
Advanced Python Scheduler (APScheduler) is a task scheduler and task queue system for Python. It can be used solely as a job queuing system if you have no need for task scheduling。


## demo
```python
import time
from datetime import datetime

from pytz import utc

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

jobstores = {
    # 'mongo': MongoDBJobStore(),
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}
scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)


def tick():
    print('Tick! The time is: %s' % datetime.now())


if __name__ == '__main__':
    # id,可以指定，不指定会默认生成，
    # replace_existing, 允许替换已存在的任务
    # 其他参数，查看add_job 源码
    scheduler.add_job(tick, 'interval', seconds=3, replace_existing=True, id='abc')
    scheduler.start()
    # 程序一直保持运行，后续的任务才会被执行
    while True:
        time.sleep(1)
    print('done')
```
## 分布式支持？
不支持分布式，任务会被重复执行，这个要根据实际场景确定是否使用。这是我一个朋友在用的，我简单了解了下，我朋友是用它来做定时任务的。
通过启动两个程序结果：
[![pipMw7Q.png](https://z1.ax1x.com/2023/10/13/pipMw7Q.png)](https://imgse.com/i/pipMw7Q)