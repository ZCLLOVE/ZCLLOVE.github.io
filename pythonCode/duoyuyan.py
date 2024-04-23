import pandas as pd
import pyexcel as p
import re

def translate_excel(source_path, dictionary_path):
    # 字典
    df_dict = pd.read_excel(dictionary_path)
    my_dict = {'是|1':'true|1','否|2':'false|2','否|0':'false|0','是|1否|2':'true|1\nfalse|2'}
    # 遍历DataFrame的每一行
    for i in range(len(df_dict)):
        # 使用第X列的值作为键 0开始
        key_1 = str(df_dict.iloc[i, 0]).replace(" ", "")
        # 第X列的值作为字典的值
        value = df_dict.iloc[i, 1]
        # 将键值对添加到字典中
        my_dict[key_1] = value

        # # 如果第二列有内容，则使用第二列的值作为键
        # if pd.notna(df_dict.iloc[i, 1]):
        #     key_2 = str(df_dict.iloc[i, 1]).replace(" ", "")
        #     # 将键值对添加到字典中
        #     my_dict[key_2] = value
    print(my_dict)
    update_excel_from_dict(source_path,my_dict)


def update_excel_from_dict(excel_path, update_dict):
    # 使用pyexcel读取.xls文件
    sheet = p.get_sheet(file_name=excel_path)

    # 假设第一行代表列的数量，检查是否有足够的列
    if len(sheet.row_at(0)) < 8:
        print("Excel文件中没有足够的列来进行更新。")
        return

    # 遍历Excel的每一行
    for row_index in range(sheet.number_of_rows()):
        row = sheet.row_at(row_index)
        # 获取第7列的值并去除所有空格

        key = re.sub(r'\s+', '', str(row[2]))
        # 从字典中获取对应的值，如果不存在就返回None
        value = update_dict.get(key, None)
        # 如果找到了对应的值，更新第X列
        if value is not None:
            sheet[row_index, 11] = str(value)  # 此处将值转换为字符串类型
    # 保存更新后的Excel文件
    sheet.save_as(excel_path)
    print("Excel文件已更新。")


# 源文件和字典文件的路径
source_file_path = r'C:\Users\29510\Desktop\员工账户无重复值-全2.xlsx'  # 请根据实际源文件名称调整
dictionary_file_path = r'C:\Users\29510\Desktop\字典.xlsx'  # 请根据实际字典文件名称调整

translate_excel(source_file_path,dictionary_file_path)