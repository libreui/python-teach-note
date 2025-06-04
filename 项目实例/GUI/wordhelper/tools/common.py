import os
import re


def git_file_names(filepath='', file_ext='all'):
    """获取文件列表"""
    filelist_out = []
    for filename in os.listdir(filepath):
        fi_d = os.path.join(filepath, filename)
        if file_ext == 'all':
            if os.path.splitext(fi_d)[1] in ['.doc', '.docx']:
                filelist_out.append(fi_d)
        else:
            if file_ext == 'all':
                filelist_out.append(fi_d)
            elif os.path.splitext(fi_d)[1] == file_ext:
                filelist_out.append(fi_d)
            else:
                pass
    filelist_out.sort(key=index_sort)
    return filelist_out


def index_sort(elem):
    a = re.findall(r"第\d章", elem)
    if not a:
        return float('inf')
    else:
        return int(a[0][1:-1])
