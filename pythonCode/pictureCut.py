from PIL import Image
import os
#裁剪成正方形
def crop_to_square(img):
    width, height = img.size
    size = min(width, height)
    left = (width - size) / 2
    top = (height - size) / 2
    right = (width + size) / 2
    bottom = (height + size) / 2
    return img.crop((left, top, right, bottom))

def resize_images_in_folder(folder_path, size):
    count = 0
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img = Image.open(os.path.join(folder_path, filename))
            # 转换为RGB模式 如果是png也可以转成jpg输出
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            img = crop_to_square(img)
            img = img.resize(size, Image.LANCZOS)
            newName = "a" + str(count) +'.png'
            img.save(os.path.join(folder_path, newName))
            count += 1
folder_path = 'C:\\Users\\29510\\Desktop\\照片'
size=(240, 240)
# 使用方法
resize_images_in_folder(folder_path,size)
