
# Word2PDF
> 本文主要介绍使用[Aspose.Words for Python via .NET](https://products.aspose.com/words/python-net/)工具，将Word转化为PDF。
## 安装
> 官方安装[教程](https://docs.aspose.com/words/python-net/installation/)
- Install aspose-words from pypi
    ```
    pip install aspose-words
    ```
- 系统支持，[详情](https://docs.aspose.com/words/python-net/system-requirements/)
    - Microsoft Windows
    - Linux
    - 不支持MacOS，如果在mac上跑，建议使用docker



## Convert Word to PDF code
```python
import traceback
import aspose.words as aw


def set_license(license_file_path='Aspose.Words.Python.NET.lic'):
    try:
        lic = aw.License()
        lic.set_license(license_file_path)
    except RuntimeError as err:
        print("There was an error setting the license: {0}".format(err))


def remove_element(doc, element_type) -> None:
    """
    移除指定元素，只要传入指定的node类型，会做全量的移除

    element_type:
    ex:
    aw.NodeType.HEADER_FOOTER
    """
    elements = doc.get_child_nodes(element_type, True)
    elements.clear()


def remove_footer(doc):
    """
    移除页脚
    :param doc:
    :return:
    """
    for section in doc:
        section = section.as_section()
        # Up to three different footers are possible in a section (for first, even and odd pages)
        # we check and delete all of them.
        footer = section.headers_footers.get_by_header_footer_type(aw.HeaderFooterType.FOOTER_FIRST)
        if footer:
            footer.remove()

        # Primary footer is the footer used for odd pages.
        footer = section.headers_footers.get_by_header_footer_type(aw.HeaderFooterType.FOOTER_PRIMARY)
        if footer:
            footer.remove()

        footer = section.headers_footers.get_by_header_footer_type(aw.HeaderFooterType.FOOTER_EVEN)
        if footer:
            footer.remove()


def remove_header(doc):
    """
    移除页脚
    :param doc:
    :return:
    """
    for section in doc:
        section = section.as_section()
        # Up to three different headers are possible in a section (for first, even and odd pages)
        # we check and delete all of them.
        header = section.headers_footers.get_by_header_footer_type(aw.HeaderFooterType.HEADER_FIRST)
        if header:
            header.remove()

        # Primary header is the footer used for odd pages.
        header = section.headers_footers.get_by_header_footer_type(aw.HeaderFooterType.HEADER_PRIMARY)
        if header:
            header.remove()

        header = section.headers_footers.get_by_header_footer_type(aw.HeaderFooterType.HEADER_EVEN)
        if header:
            header.remove()


def word2pdf_with_aspose(file_path: str, output_put_path: str,
                         convert_arg: dict = dict(remove_comment=True)) -> (bool, str):
    try:
        doc = aw.Document(file_path)
        if "remove_comment" in convert_arg and convert_arg['remove_comment'] == 'true':
            print("移除批注")
            remove_element(doc, aw.NodeType.COMMENT)
        if "accept_revision" in convert_arg and convert_arg['accept_revision'] == 'true':
            print("接受修订")
            doc.accept_all_revisions()
        if "remove_footer" in convert_arg and convert_arg['remove_footer'] == 'true':
            print("移除页脚")
            remove_footer(doc)  # 移除所有页脚
        if "remove_header" in convert_arg and convert_arg['remove_header'] == 'true':
            print("移除页眉")
            remove_header(doc)  # 移除所有页眉
        doc.save(output_put_path)
        return True, output_put_path
    except:
        return False, traceback.format_exc()


def main(file_path: str, output_path: str) -> None:
    # 设置license，传入license路径即可，默认值为 Aspose.Words.Python.NET.lic
    set_license()
    # 如果需要移除备注等，在这里修改参数即可
    convert_arg = dict(remove_comment='true', accept_revision='true', remove_footer='true', remove_header='true')
    is_success, pdf_path = word2pdf_with_aspose(file_path, output_path, convert_arg)
    print(is_success, pdf_path)


if __name__ == '__main__':
    main('test.docx', 'test.pdf')

```
## 参考文档
- [aspose words license 授权](https://docs.aspose.com/words/python-net/licensing/#license-applying-options)
- [aspose words 接受修订](https://docs.aspose.com/words/python-net/track-changes-in-a-document/)
- [aspose words 移除页脚(页眉)](https://docs.aspose.com/words/python-net/working-with-headers-and-footers/#how-to-remove-footers-but-leave-headers-intact)
- [aspose word 移除批注](https://docs.aspose.com/words/python-net/working-with-comments/)

## 其他
- 如果报错,不用担心，可以忽略，官方社区有[回答](https://forum.aspose.com/t/aspose-pydrawing-brushes-is-not-initialized/242611)
```
ImportError: the static field 'transparent' of type 'aspose.pydrawing.Brushes' is not initialized
Exception ignored in: 'FieldInitializationWarning'
ImportError: the static field 'alice_blue' of type 'aspose.pydrawing.Brushes' is not initialized
Exception ignored in: 'FieldInitializationWarning'
ImportError: the static field 'antique_white' of type 'aspose.pydrawing.Brushes' is not initialized
```