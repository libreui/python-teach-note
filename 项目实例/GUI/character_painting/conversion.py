from PIL import Image, ImageDraw, ImageFont, ImageFile
import numpy as np

scale = 1  # 创建常数
# 定义字符画的字符集, 特殊字符、符号、小写字母、大写字母
default_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*_+-=;':,.?"


def picture_conversion(import_img, export_img=None, input_char="", pix_distance=""):
    """
    图片转换
    :param import_img: 导入的图片
    :param export_img: 导出的图片
    :param input_char: 输入的字符
    :param pix_distance: 清晰度 [清晰, 一般, 字符]，[3, 4, 5]
    :return:
    """
    img = Image.open(import_img)
    # 创建画布对象数组
    img_width, img_height = img.size

    canvas_array = np.ndarray((img_height, img_width, 3), dtype=np.uint8)
    canvas_array.fill(255) # 填充白色
    new_image = Image.fromarray(canvas_array) # 根据画布创建新的图片
    img_draw = ImageDraw.Draw(new_image) # 创建画笔对象
    font = ImageFont.truetype("./img/unifont.otf", 10) # 创建字体对象

    if input_char == "":
        char_list = default_char
    else:
        char_list = list(input_char)
    if pix_distance == "清晰":
        pix_distance = 3
    elif pix_distance == "一般":
        pix_distance = 4
    elif pix_distance == "字符":
        pix_distance = 5

    print(pix_distance, char_list)

    # 开始绘制
    pix_count = 0
    table_len = len(char_list)
    for y in range(img_width):
        for x in range(img_height):
            if x % pix_distance == 0 and y % pix_distance == 0:
                # 实现根据图片像素绘制字符
                img_draw.text((x*scale, y*scale),
                              char_list[pix_count % table_len],

                              font=font)
                pix_count += 1
    if export_img is not None:
        new_image.save(export_img)
    return True
