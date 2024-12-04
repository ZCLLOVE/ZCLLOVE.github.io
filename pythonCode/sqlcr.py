import pandas as pd


# 读取 Excel 文件，假设文件路径是原始字符串
def generate_sql_from_uuids(excel_file_path):
    # 读取 Excel 文件
    df = pd.read_excel(excel_file_path)

    # 假设 UUID 在第一列
    uuids = df.iloc[:, 0]

    # SQL 模板
    sql_template = "INSERT INTO SYS_OMS_CACHE(fd_id, FD_ORG_ELEMENT_ID, FD_APP_NAME, FD_OP_TYPE) VALUES('{}', '{}', 'qiye163', '1');"

    # 遍历 UUID 并生成 SQL 语句
    for uuid in uuids:
        sql = sql_template.format(uuid, uuid)
        print(sql)


# 调用函数，传入文件路径（示例）
generate_sql_from_uuids(r'C:\Users\29510\Desktop\Q.xls')
