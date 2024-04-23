import pandas as pd
import pyexcel as p
import re
import tkinter as tk
from tkinter import filedialog, messagebox
import traceback


def translate_excel(source_path, dictionary_path, key_col, value_col, match_col, assign_col):
    # 字典
    df_dict = pd.read_excel(dictionary_path)
    my_dict = {}

    # 遍历DataFrame的每一行，根据用户提供的键列和值列构建字典
    for i in range(len(df_dict)):
        key_1 = str(df_dict.iloc[i, int(key_col)]).replace(" ", "")
        value = df_dict.iloc[i, int(value_col)]
        my_dict[key_1] = value

    # 判断文件类型，调用相应的处理函数
    if source_path.endswith('.xlsx'):
        update_xlsx_from_dict(source_path, my_dict, int(match_col), int(assign_col))
    elif source_path.endswith('.xls'):
        update_xls_from_dict(source_path, my_dict, int(match_col), int(assign_col))
    else:
        raise ValueError("文件格式不支持，请选择.xlsx或.xls文件")


def update_xlsx_from_dict(excel_path, update_dict, match_col, assign_col):
    df = pd.read_excel(excel_path)

    # 遍历Excel的每一行，获取第7列的值并去除所有空格
    for index, row in df.iterrows():
        key = re.sub(r'\s+', '', str(row[match_col]))  # 获取第3列（索引为2）的值并去除空格

        # 从字典中获取对应的值
        value = update_dict.get(key, None)

        # 如果字典中存在匹配的值，更新第12列（索引为11）的值
        if value is not None:
            df.at[index, df.columns[assign_col]] = str(value)  # 更新第12列的值

    # 保存更新后的Excel文件
    df.to_excel(excel_path, index=False)
    messagebox.showinfo("完成", "Excel文件已更新并保存。")
def update_xls_from_dict(excel_path, update_dict, match_col, assign_col):
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

        key = re.sub(r'\s+', '', str(row[match_col]))
        # 从字典中获取对应的值，如果不存在就返回None
        value = update_dict.get(key, None)
        # 如果找到了对应的值，更新第X列
        if value is not None:
            sheet[row_index, assign_col] = str(value)  # 此处将值转换为字符串类型
    # 保存更新后的Excel文件
    sheet.save_as(excel_path)
    messagebox.showinfo("完成", "Excel文件已更新并保存。")


# GUI部分
def open_file_dialog(entry):
    filepath = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    entry.delete(0, tk.END)
    entry.insert(0, filepath)


def run_program():
    source_path = source_entry.get()
    dictionary_path = dictionary_entry.get()
    key_col = key_col_entry.get()
    value_col = value_col_entry.get()
    match_col = match_col_entry.get()
    assign_col = assign_col_entry.get()

    if not all([source_path, dictionary_path, key_col, value_col, match_col, assign_col]):
        messagebox.showwarning("警告", "请填写所有字段。")
        return

    try:
        translate_excel(source_path, dictionary_path, key_col, value_col, match_col, assign_col)
    except Exception as e:
        error_message = f"程序运行中出现错误: {str(e)}\n详细信息:\n{traceback.format_exc()}"
        messagebox.showerror("错误", error_message)


# 创建窗口
window = tk.Tk()
window.title("Excel 字典更新工具")

# 字典文件路径
tk.Label(window, text="字典文件路径:").grid(row=0, column=0)
dictionary_entry = tk.Entry(window, width=50)
dictionary_entry.grid(row=0, column=1)
tk.Button(window, text="浏览", command=lambda: open_file_dialog(dictionary_entry)).grid(row=0, column=2)

# 源Excel文件路径
tk.Label(window, text="源Excel文件路径:").grid(row=1, column=0)
source_entry = tk.Entry(window, width=50)
source_entry.grid(row=1, column=1)
tk.Button(window, text="浏览", command=lambda: open_file_dialog(source_entry)).grid(row=1, column=2)

# 键列
tk.Label(window, text="键列（从0开始计数）:").grid(row=2, column=0)
key_col_entry = tk.Entry(window)
key_col_entry.grid(row=2, column=1)

# 值列
tk.Label(window, text="值列（从0开始计数）:").grid(row=3, column=0)
value_col_entry = tk.Entry(window)
value_col_entry.grid(row=3, column=1)

# 匹配列
tk.Label(window, text="匹配列（从0开始计数）:").grid(row=4, column=0)
match_col_entry = tk.Entry(window)
match_col_entry.grid(row=4, column=1)

# 赋值列
tk.Label(window, text="赋值列（从0开始计数）:").grid(row=5, column=0)
assign_col_entry = tk.Entry(window)
assign_col_entry.grid(row=5, column=1)

# 执行按钮
tk.Button(window, text="执行", command=run_program).grid(row=6, column=1)

# 运行窗口
window.mainloop()
