import pandas as pd


# 读取Excel文件
def generate_insert_statements(excel_file):
    # 读取Excel文件
    df = pd.read_excel(excel_file)

    # 检查表头是否符合预期
    required_columns = ['fd_model_name', 'fd_gui_dang_qi_xian', 'kbm', 'qzh', 'fd_model_id']
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"Excel文件中缺少必要的列: {required_columns}")

    # 构建插入SQL语句
    insert_statements = []
    for _, row in df.iterrows():
        # 从行中提取字段值
        fd_model_name = row['fd_model_name']
        fd_gui_dang_qi_xian = row['fd_gui_dang_qi_xian']
        kbm = row['kbm']
        qzh = row['qzh']
        fd_model_id = row['fd_model_id']

        # 生成SQL语句
        insert_statement = f"""
        INSERT INTO KM_LIGHTDATA_MAIN (fd_id, fd_model_name, fd_gui_dang_qi_xian, kbm, qzh, fd_model_id)
        VALUES ('{fd_model_id}', '{fd_model_name}', '{fd_gui_dang_qi_xian}', '{kbm}', '{qzh}', '{fd_model_id}');
        """
        insert_statements.append(insert_statement)

    return insert_statements


# 打印生成的所有INSERT语句
def print_insert_statements(excel_file):
    try:
        insert_statements = generate_insert_statements(excel_file)
        for stmt in insert_statements:
            print(stmt)
    except Exception as e:
        print(f"发生错误: {e}")


# 示例：传入Excel文件路径
if __name__ == "__main__":
    excel_file_path = r'C:\Users\29510\Desktop\cs.xlsx'  # 替换为你的文件路径
    print_insert_statements(excel_file_path)
