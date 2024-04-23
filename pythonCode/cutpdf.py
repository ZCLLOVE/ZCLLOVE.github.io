import PyPDF2


def copy_pdf(input_pdf_path, output_pdf_path):
    # 打开输入的 PDF 文件
    with open(input_pdf_path, "rb") as input_pdf_file:
        # 创建 PDF 阅读器
        pdf_reader = PyPDF2.PdfReader(input_pdf_file)

        # 创建 PDF 写入器
        pdf_writer = PyPDF2.PdfWriter()

        # 只选择前 30 页
        for page_num in range(min(30, len(pdf_reader.pages))):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

        # 保存新的 PDF 文件
        with open(output_pdf_path, "wb") as output_pdf_file:
            pdf_writer.write(output_pdf_file)

input_pdf_path = r"C:\Users\29510\Desktop\a.pdf"
output_pdf_path = r"C:\Users\29510\Desktop\b.pdf"  # 输出的文件路径
copy_pdf(input_pdf_path, output_pdf_path)

print("PDF 已成功复制前 30 页。")
