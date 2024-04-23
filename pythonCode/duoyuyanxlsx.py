import pandas as pd
import re


def translate_excel(source_path, dictionary_path):
    # 读取字典文件
    df_dict = pd.read_excel(dictionary_path)

    # 初始化字典，增加基本的键值对
    my_dict = {}

    # 遍历字典文件，构建字典
    for i in range(len(df_dict)):
        key_1 = str(df_dict.iloc[i, 0]).replace(" ", "")
        value = df_dict.iloc[i, 1]
        my_dict[key_1] = value

    print(my_dict)
    update_excel_from_dict(source_path, my_dict)


def update_excel_from_dict(excel_path, update_dict):
    # 读取Excel文件
    df = pd.read_excel(excel_path)


    # 遍历Excel的每一行，获取第7列的值并去除所有空格
    for index, row in df.iterrows():
        key = re.sub(r'\s+', '', str(row[0]))  # 获取第3列（索引为2）的值并去除空格

        # 从字典中获取对应的值
        value = update_dict.get(key, None)

        # 如果字典中存在匹配的值，更新第12列（索引为11）的值
        if value is not None:
            df.at[index, df.columns[1]] = str(value)  # 更新第12列的值

    # 保存更新后的Excel文件
    df.to_excel(excel_path, index=False)
    print("Excel文件已更新。")


# 源文件和字典文件的路径
source_file_path = r'C:\Users\29510\Desktop\2.xlsx'
dictionary_file_path = r'C:\Users\29510\Desktop\1.xlsx'

translate_excel(source_file_path, dictionary_file_path)
