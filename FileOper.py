import os
import re

# def endWith(*endstring):
#     """
#     """
#         ends = endstring
#         def run(s):
#                 f = map(s.endswith,ends)
#                 if True in f: return s
#         return run

def getFilterFiles(sourcePath,regular):
    """根据原始路径以及正则匹配条件，
    返回满足条件的 文件名-路径 字典
    """
    dic={}
    # 遍历指定路径下的所有文件
    for root,dirs,files in os.walk(sourcePath):
        for filename in files:
            # 对每一个文件通过正则进行匹配
            if(re.match(regular,filename)):
                # 若满足条件则将文件名称及路径存入字典中
                path=os.path.join(sourcePath,filename)
                dic[filename]=path
    return dic


