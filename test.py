import Dir
import DateTimeInfo

# dirInfo.GetAllFiles('','','2017-07-24-00-00','2017-07-24-00-23')
# 获取指定文件及文件夹的测试——暂时注释
# date_temp=dirInfo.Str2Date('2017-07-24-00-00')
# dirInfo.GetAllFiles('ss','ss','2017-07-24-00-00','2017-07-24-00-23')
dirInfo=Dir.DirectoryInfo()
dtInfo=DateTimeInfo.DateTimeInfo('','')
dtInfo.get_date_list()

