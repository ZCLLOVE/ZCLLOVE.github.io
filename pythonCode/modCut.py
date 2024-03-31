import re

def extract_mod_numbers(input_string):
    # 使用正则表达式提取模组编号
    pattern = r"workshop-(\d+)"
    mod_numbers = re.findall(pattern, input_string)

    return mod_numbers

def format_output(mod_numbers):
    # 格式化输出
    output_lines = []
    for mod_number in mod_numbers:
        output_lines.append(f'ServerModSetup("{mod_number}")')
        output_lines.append(f'ServerModCollectionSetup("{mod_number}")\n')

    return '\n'.join(output_lines)

# 传入字符串示例
input_string = ''''''

# 提取模组编号
mod_numbers = extract_mod_numbers(input_string)

# 格式化输出
output_result = format_output(mod_numbers)

# 打印结果
print(output_result)
