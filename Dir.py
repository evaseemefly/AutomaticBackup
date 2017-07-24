import time,datetime
import FileOper

class DirectoryInfo:
    """"文件夹类
    """
    #原始路径
    __sourcePath=''
    #复制到的路径
    __targetPath=''

    def Str2Date(self,date_str):
        """将传入的str转换为date类型
        """
        return time.strptime(date_str, "%Y-%m-%d-%H-%M")

    def GetAllFiles(self,stationInfo,startDate_str,finishDate_str):
        """根据原路路径，以及海洋站的名称及后缀，根据时间范围获取所有的文件
        """
        # 根据传入的时间获取文件夹列表
        startDate=self.Str2Date(startDate_str) 
        finishDate=self.Str2Date(finishDate_str) 
        # 根据传入的海洋站名及后缀还有时间获取对应的文件夹路径列表
        # stationInfo:key 站名（其实设置为set即可，只有站代码即可）
        for value in stationInfo.items():
            # 获取正则表达式
            # 月日时.站代码
            # 072800.DYW
            
            # regular=
            FileOper.getFilterFiles()