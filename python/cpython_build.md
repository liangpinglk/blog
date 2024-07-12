# CPython build

```shell
pip install cython
```

## 编译

> 在项目目录下执行`python setup.py build_ext --inplace`这样会在py（pyc）文件对应的路径生成对应的c和.so 文件

```python
from typing import Generator

from setuptools import setup
from Cython.Build import cythonize
import os


def find_all_file(file_path: str, target_ext: str = None) -> Generator:
    """
    传入文件路径获取所有子文件路径
    :param file_path:
    :param target_ext:
    :return:
    """
    if os.path.isfile(file_path):
        yield file_path
    for root, ds, fs in os.walk(file_path):
        for f in fs:
            if not target_ext:
                yield root + '/' + f if root else f
            if target_ext and f.split('.')[-1].lower() == target_ext:
                yield root + '/' + f if root else f


# 指定要编译的源文件，包括子目录中的文件
source_files = list(find_all_file(os.getcwd(), 'py'))

setup(
    ext_modules=cythonize(source_files),
)
# python setup.py build_ext --inplace
```

## 清理文件

在实际交付中，编译好后，需要将不想干的文件清理掉，执行`python clear.py`


```python
import os
import shutil
from typing import Generator


def find_all_file(file_path: str, target_ext: str = None) -> Generator:
    """
    传入文件路径获取所有子文件路径
    :param file_path:
    :param target_ext:
    :return:
    """
    if os.path.isfile(file_path):
        yield file_path
    for root, ds, fs in os.walk(file_path):
        for f in fs:
            if not target_ext:
                yield root + '/' + f if root else f
            if target_ext and f.split('.')[-1].lower() == target_ext:
                yield root + '/' + f if root else f


def rm_file(all_file):
    for i in all_file:
        print(i)
        if os.path.basename(i) not in ["setup.py", "clear.py"]:
            os.remove(i)


rm_file(find_all_file(os.getcwd(), target_ext='py'))
rm_file(find_all_file(os.getcwd(), target_ext='c'))
# rm_file(find_all_file(os.getcwd(), target_ext='so'))
shutil.rmtree("build")
```