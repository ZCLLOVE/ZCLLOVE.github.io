import os
import pandas as pd


def process_excel_files(folder_path):
    # 存储结果的 Java StringBuilder 代码
    result = []

    # 遍历文件夹中的所有文件
    for file_name in os.listdir(folder_path):
        # 判断文件是否是Excel文件
        if file_name.endswith(('.xlsx', '.xls')):
            file_path = os.path.join(folder_path, file_name)

            try:
                # 读取Excel文件，只读取前四列
                df = pd.read_excel(file_path, usecols=[0, 1, 2, 3])

                # 去除每个单元格前后空格
                df = df.applymap(lambda x: str(x).strip() if isinstance(x, str) else x)

                # 将每一行的四列数据合并成一个以`;`分隔的字符串
                for index, row in df.iterrows():
                    # 检查第一列是否包含`\`，如果有，取`\`后面的部分
                    if '/' in str(row[0]):
                        row[0] = str(row[0]).split('/')[-1]  # 获取`\`后面的部分

                    # 构建行字符串
                    row_string = ";".join(str(value) for value in row)

                    # 构建 Java StringBuilder 语句
                    result.append(f'sb.append("{row_string}\\n");')

            except Exception as e:
                print(f"无法处理文件 {file_name}，错误: {e}")

    # 返回 Java 语句的集合
    return "\n".join(result)


# 示例用法
folder_path = r'C:\Users\29510\Desktop\库编码等'  # 修改为你的文件夹路径
result_string = process_excel_files(folder_path)

# 打印最终结果
print(result_string)
