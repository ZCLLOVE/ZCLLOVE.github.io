import pandas as pd

def txt_to_excel(txt_file_path, excel_file_path):
    # 读取txt文件，按行分割，并用';'分割每一行的数据
    with open(txt_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 处理每行数据，并将其按分号分割成四个部分
    data = [line.strip().split(';') for line in lines]

    # 创建DataFrame，列名分别为 1, 2, 3, 4
    df = pd.DataFrame(data, columns=[1, 2, 3, 4,5])

    # 将DataFrame写入到Excel文件
    df.to_excel(excel_file_path, index=False, engine='openpyxl')

    print(f"Excel文件已保存到：{excel_file_path}")

# 示例使用方法
txt_file_path = r'C:\Users\29510\Desktop\正式环境kbm配置.txt'  # 使用原始字符串
excel_file_path = r'C:\Users\29510\Desktop\zs.xlsx'   # 输出的Excel文件路径
txt_to_excel(txt_file_path, excel_file_path)
