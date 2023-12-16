# PDF_Word_Converter
简介

PDF_Word_Converter 是一个用于将 PDF 文档转换为 Word 文档的 Python 工具。它基于 Python 编写，利用强大的 PDF 和文本处理库，为用户提供了一种简便的方式来将 PDF 文件转换为可编辑的 Word 文档。
功能特点

    PDF 到 Word 转换： 将 PDF 文件转换为 Microsoft Word 格式，方便用户进行编辑和格式调整。
    文本提取： 提取 PDF 文件中的文本内容，保留原始格式和布局。
    简单易用： 使用简单的命令行接口，使用户能够轻松地执行转换操作。

系统要求

    Python 3.x
    依赖库：docx2pdf、pdf2docx

安装

使用以下命令安装所需的依赖库：

bash

pip install docx2pdf pdf2docx

用法

bash

python pdf_word_converter.py input.pdf output.docx

    input.pdf 是要转换的 PDF 文件路径。
    output.docx 是输出的 Word 文件路径。

示例

bash

python pdf_word_converter.py 


注意事项

    请确保输入的 PDF 文件没有加密，否则无法进行转换。
    该工具可能无法完美保留 PDF 中的所有格式，尤其是复杂布局和图形。

贡献

欢迎贡献代码、报告问题或提出建议。在贡献之前，请阅读 贡献指南。
许可证

本项目采用 MIT 许可证。

感谢使用 PDF_Word_Converter！如有任何疑问或建议，请随时联系我们。
