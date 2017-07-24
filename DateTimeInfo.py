# coding=utf-8
from datetime import datetime,timedelta

class DateTimeInfo:
    
    def __init__(self,startDateTime,finishDateTime):
        """构造函数根据传入的起始及终止时间来初始化对应的私有变量
        """
        # 此处还需要修改为获取今日往前推7日的时间
        self.__defaultDateTime=datetime.now
        self.__startDateTime=startDateTime,
        self.__finishDateTime=finishDateTime

    # 根据起始时间获取中间时刻的集合
    def get_date_list(self,startDate,finishDate):
        """
        获取日期列表
        :param start: 开始日期
        :param end: 结束日期
        :return:
        """
        if startDate is None:
            startDate=self.__defaultDateTime
        if finishDate is None:
            finishDate=datetime.now
        date=[]
        for d in gen_dates(startDate,(finishDate-startDate).hours):
            date.append(d)
        return date

    def gen_dates(sourceDate, hours):
        day = timedelta(hours=1)
        for i in range(hours):
            yield sourceDate + hours*i
