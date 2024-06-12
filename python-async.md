> 以下主要代码都来自chatgpt
## demo
```python
import asyncio
import time


async def say_hello(name):
    print(f"Hello, {name}")
    await asyncio.sleep(1)
    print(f"Goodbye, {name}")
    if name == 99:
        99 / 0


async def main():
    tasks = [say_hello("Alice"), say_hello("Bob"), say_hello("Charlie")]
    for i in range(10000):
        tasks.append(say_hello(i))

    results = await asyncio.gather(*tasks, return_exceptions=True)
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"Task {i} failed with exception: {result}")
        # else:
        #     print(f"Task {i} completed successfully")


if __name__ == '__main__':
    s = time.time()
    asyncio.run(main())
    print(f"use time {time.time() - s}")

```
## limit task demo
> 上面的无限制使用资源，资源不够了会出现意外情况，可以根据实际情况进行适当限制
```python
import asyncio
import time


async def limited_task(sem, name):
    async with sem:
        print(f"Running task {name}")
        await asyncio.sleep(1)
        print(f"Task {name} completed")


async def main():
    semaphore = asyncio.Semaphore(20)  # 同时运行的任务数限制为 20
    tasks = [limited_task(semaphore, i) for i in range(100)]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    s = time.time()
    asyncio.run(main())
    print(f"use time {time.time() - s}")

```