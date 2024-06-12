
# Excel2PDF
> 本文主要介绍使用[Aspose.Cells for Python via Java](https://products.aspose.com/cells/python-java/)工具，将Excel转化为PDF。如果想直接使用，可以直接使用 扩展column 章节的demom，代码中也有相关特性的注释。
## 安装
> 官方安装[教程](https://docs.aspose.com/cells/python-java/setup-environment-and-installation-guidelines/#python-version)
- Install Java
- Install Aspose.Cells for Python via Java from pypi
    ```
    pip install aspose-cells
    ```
## Conver Excel to PDF
### license 设置
> 这里写个函数，后续demo都会调用该函数。license可以去官方网站申请临时license试用
```python
def set_license(license_file_path='/usr/src/app/dist_model/license/Aspose.Cells.PythonviaJava.lic'):
    try:
        license = License()
        license.setLicense(license_file_path)
    except RuntimeError as err:
        print("There was an error setting the license: {0}".format(err))
```
### 简单的demo
```python
import jpype
jpype.startJVM()
from asposecells.api import Workbook, License
set_license()
workbook = Workbook('test.xls')
workbook.save('test.pdf')
jpype.shutdownJVM()
```
### 对与列过多的Excel
> 列过多，超出默认A4的宽度，转化成pdf后丢失数据的处理方法
```python
import jpype
jpype.startJVM()
from asposecells.api import Workbook, PdfSaveOptions, License
set_license()
workbook = Workbook('test.xls')
pdf_options = PdfSaveOptions()
pdf_options.setAllColumnsInOnePagePerSheet(True)  # excel 列过多，让pdf自动拓宽宽度
workbook.save('test.pdf')
jpype.shutdownJVM()
```
参考文档
- [Convert Excel to PDF](https://docs.aspose.com/cells/python-java/convert-excel-to-pdf/#advanced-conversion)
- [pdfsaveoptions](https://reference.aspose.com/cells/python-java/asposecells.api/pdfsaveoptions)
### 扩展 column
> 列过窄的情况下，转化成pdf会导致信息丢失
```python
import jpype
jpype.startJVM()
from asposecells.api import Workbook, PdfSaveOptions, License
set_license()
workbook = Workbook('test.xls')
pdf_options = PdfSaveOptions()
pdf_options.setAllColumnsInOnePagePerSheet(True)  # excel 列过多，让pdf自动拓宽宽度
pdf_options.setOnePagePerSheet(True)  # 将一个sheet 输出为一页, 如果为false，则会自动分页

worksheets = workbook.getWorksheets()  # 获取所有sheet
sheet_count = worksheets.getCount()  # 获取sheet的总个数
for i in range(sheet_count):
    single_sheet = worksheets.get(i)  # 获取单个sheet
    single_sheet.autoFitColumns()  # 对每列进行自适应，避免因cell过窄，导致cell 被cut
    single_sheet.autoFitRows()  # 同autoFitColumns

workbook.save('test.pdf')
jpype.shutdownJVM()
```
参考文档
- [Autofit Rows and Columns in Python](https://docs.aspose.com/cells/java/autofit-rows-and-columns-in-python/)
## 其他
- [github releases](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases)

