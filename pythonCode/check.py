import json

# 辅助函数用于收集键
def collect_keys(json_object, key_set):
    if isinstance(json_object, dict):
        for k, v in json_object.items():
            if '.' in k:
                k = k.split('.')[-1]
            key_set.add(k)
            collect_keys(v, key_set)
    elif isinstance(json_object, list):
        for item in json_object:
            collect_keys(item, key_set)

# JSON字符串
json_string = ''''''
input_string = ''''''

# 将JSON字符串转为Python字典
json_object = json.loads(json_string)

# 将所有的键收集到一个集合中
key_set = set()
collect_keys(json_object, key_set)

def find_missing_keys(key_set, input_string):
    return {key for key in key_set if key not in input_string}

missing_keys = find_missing_keys(key_set, input_string)
print('Missing keys:', missing_keys)