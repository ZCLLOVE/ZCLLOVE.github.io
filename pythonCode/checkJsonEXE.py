import json
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox


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


def find_missing_keys(key_set, input_string):
    return {key for key in key_set if key not in input_string}


def execute():
    json_string = json_input.get("1.0", tk.END)
    input_string = input_text.get("1.0", tk.END)
    try:
        json_object = json.loads(json_string)
    except json.JSONDecodeError:
        messagebox.showerror("错误", "无效的JSON字符串")
        return

    key_set = set()
    collect_keys(json_object, key_set)
    missing_keys = find_missing_keys(key_set, input_string)
    result_text.delete("1.0", tk.END)
    result_text.insert("1.0", 'Missing keys: ' + ', '.join(missing_keys))


# 创建主窗口
root = tk.Tk()
root.title("JSON键检查器")

# 创建和布局控件
tk.Label(root, text="JSON字符串:").pack()
json_input = scrolledtext.ScrolledText(root, height=10)
json_input.pack()

tk.Label(root, text="字符串|源码:").pack()
input_text = scrolledtext.ScrolledText(root, height=20)  # 你可以根据需要设置高度
input_text.pack()

tk.Button(root, text="执行", command=execute).pack()

tk.Label(root, text="缺失的键:").pack()
result_text = scrolledtext.ScrolledText(root, height=5)
result_text.pack()

# 运行主事件循环
root.mainloop()
db = "pyinstaller --onefile --windowed checkJsonEXE.py"
