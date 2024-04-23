import pandas as pd
import math

def excel_to_sql_where_clause(excel_path, column_index, sql_head, batch_size=1000):
    # 读取Excel文件
    df = pd.read_excel(excel_path)

    # 检查指定列的索引是否有效
    if column_index >= len(df.columns):
        raise ValueError(f"Column index '{column_index}' is out of range.")

    # 初始化一个集合来存储唯一值
    unique_values = set()

    # 遍历指定列中的每一行
    for value in df.iloc[:, column_index]:
        if pd.notnull(value):  # 确保该行不是空值
            # 分割逗号分隔的值并去除空格
            split_values = [item.strip() for item in str(value).split(',')]
            unique_values.update(split_values)

    # 将唯一值列表化
    unique_values_list = list(unique_values)

    # 计算需要生成的批次数
    num_batches = math.ceil(len(unique_values_list) / batch_size)

    # 构建 SQL WHERE 子句
    where_clauses = []
    for i in range(num_batches):
        # 每批次的值
        batch_values = unique_values_list[i * batch_size:(i + 1) * batch_size]
        where_clause = f"fd_travel_no IN ({','.join([repr(val) for val in batch_values])})"
        where_clauses.append(where_clause)

    # 使用 OR 将多个 IN 子句连接起来
    full_where_clause = " OR ".join(where_clauses)

    # 构建最终的 SQL 语句
    full_sql = f"{sql_head} WHERE {full_where_clause}"

    return full_sql

# 示例调用
excel_path = r'C:\Users\29510\Desktop\444.xlsx'
column_index = 1  # 使用索引选择列, 索引从0开始
sql_head = "UPDATE fssc_travel_applicat SET fd_status = '1'"

sql_query = excel_to_sql_where_clause(excel_path, column_index, sql_head, batch_size=1000)

# 打印生成的 SQL 语句
print(sql_query)
