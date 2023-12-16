import os
from tkinter import Tk, Label, Button, filedialog
from pdf2docx import Converter
from docx2pdf import convert

def select_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[('PDF 文件', '*.pdf')])
    pdf_file_label.config(text=file_path)

def select_word_file():
    file_path = filedialog.askopenfilename(filetypes=[('Word 文件', '*.docx *.doc')])
    word_file_label.config(text=file_path)

def convert_pdf_to_docx():
    pdf_file = pdf_file_label.cget("text")
    if pdf_file:
        docx_file = os.path.splitext(pdf_file)[0] + ".docx"
        cv = Converter(pdf_file)
        cv.convert(docx_file, start=0, end=None)
        cv.close()
        result_label.config(text="PDF转换为Word完成。")
    else:
        result_label.config(text="请先选择一个PDF文件。")

def convert_docx_to_pdf():
    word_file = word_file_label.cget("text")
    if word_file:
        pdf_file = os.path.splitext(word_file)[0] + ".pdf"
        convert(word_file, pdf_file)
        result_label.config(text="Word转换为PDF完成。")
    else:
        result_label.config(text="请先选择一个Word文件。")

# 创建GUI界面
root = Tk()
root.title("文件转换")

# 选择PDF文件按钮和标签
pdf_select_button = Button(root, text="选择PDF文件", command=select_pdf_file)
pdf_select_button.pack(pady=10)
pdf_file_label = Label(root, text="未选择文件")
pdf_file_label.pack()

# 选择Word文件按钮和标签
word_select_button = Button(root, text="选择Word文件", command=select_word_file)
word_select_button.pack(pady=10)
word_file_label = Label(root, text="未选择文件")
word_file_label.pack()

# 转换按钮和结果标签
pdf_to_docx_button = Button(root, text="将PDF转换为Word", command=convert_pdf_to_docx)
pdf_to_docx_button.pack(pady=10)

docx_to_pdf_button = Button(root, text="将Word转换为PDF", command=convert_docx_to_pdf)
docx_to_pdf_button.pack(pady=10)

result_label = Label(root, text="")
result_label.pack()

root.mainloop()