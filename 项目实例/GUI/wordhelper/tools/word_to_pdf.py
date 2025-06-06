import os
# from docxtopdf import convert
import pypandoc
from PyPDF2 import PdfFileReader


def word_to_pdf(file_list, target_path):
    """
    把word文件转成pdf文件
    :param file_list: 要转换的word文件列表
    :param target_path: 转换后的pdf文件存放路径
    :return:
    """
    target_list = []
    for file in file_list:
        # 文件名
        file_name = os.path.basename(file)
        # 文件名和后缀
        file_name, file_ext = os.path.splitext(file_name)
        # 目标文件路径
        target_file = os.path.join(target_path, file_name + ".pdf")
        try:
            # 转换
            pypandoc.convert_file(file, "pdf", outputfile=target_file)
            # 转换后的PDF文件列表
            target_list.append(target_file)
        except Exception as e:
            print("转换失败", e)
            return False
    return target_list


def word_to_pdf_1(file_list):
    """
    把word文件转成pdf文件,并统计PDF的页码数量
    :param file_list: 要转换的word文件列表
    :return:
    """
    total_pages = 0
    value_list = []
    for file in file_list:
        # 文件名
        file_name = os.path.basename(file)
        # 文件名和后缀
        file_name, file_ext = os.path.splitext(file_name)
        # 目标文件路径
        target_file = os.path.join(os.path.dirname(file), file_name + ".pdf")
        # 转换
        try:
            pypandoc.convert_file(file, "pdf", outputfile=target_file)
            # 统计PDF的页码数量
            if os.path.exists(target_file):
                pages = get_pdf_page_number(target_file)
                total_pages += pages
                value_list.append((file, str(pages)))
                os.remove(target_file)
            else:
                print("转换失败")
                return False
        except:
            print("转换失败")
            return False
    return total_pages, value_list


def get_pdf_page_number(path):
    """
    获取PDF的页码数量
    :param path: PDF文件路径
    :return:
    """
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        page_count = pdf.getNumPages()
    return page_count
