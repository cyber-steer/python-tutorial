import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
colors = ['#3e1008', '#767c7b', '#075dcd', '#339244', '#c1ebd0', '#a91e4e', '#8c293c', '#5766be', '#67f30d', '#dd6627', '#1228a8', '#981ee5', '#091a44', '#c73724', '#19130b', '#e095e4', '#1ed604', '#61495d', '#aad3fa', '#63cebf', '#a8a13d', '#8df13d', '#3f47f6', '#308a06', '#5b665f', '#5c2202', '#2059d0', '#ce1b4d', '#c7b716', '#f09624', '#779339', '#558730', '#b632f6', '#01b7fc', '#7d2656', '#5227d1', '#eb74fd', '#3b74e6', '#25aaf8', '#353d0d', '#069116', '#719768', '#73753c', '#e1332d', '#d7a709', '#70fecc', '#0ec46c', '#c41fdc', '#000783', '#a9a119']

class Data():
    def __init__(self, path):
        self.dataframe=pd.read_csv(path)
        self.shape = self.dataframe.shape
        # self.dataframe['time'] = pd.to_datetime(self.dataframe['time'], format="%Y/%m/%d %H:%M")
    def show(self):
        print(self.dataframe)
    def head(self):
        return list(self.dataframe.columns)
    def header(self, n=-1):
        if n == -1 : n = self.shape[0]
        print(self.dataframe.head(n))
    def tail(self, n=-1):
        if n == -1 : n = self.shape[0]
        print(self.dataframe.tail(n))
    def extract(self, column, times):
        # query = (self.dataframe['time']>='2020-03-13 07:50') & (self.dataframe['time']<"2020-04-13 09:00")
        timeType, query = self.getQuery(times)
        if column == 'time':
            timeData = list(self.dataframe.loc[query, column])
            match timeType:
                case 1:
                    timeData = list(map(lambda time: time[:4],timeData))
                case 2:
                    timeData = list(map(lambda time: time[:7],timeData))
                case 3:
                    timeData = list(map(lambda time: time[:10],timeData))
                case 4:
                    timeData = list(map(lambda time: time[11:],timeData))
            timeData = set(timeData)
            timeData = list(timeData)
            timeData.sort()
            return timeData
        
        else:
            return self.dataAvg(timeType, times, column)
    def show(self, graph, x, datas):
        global colors
        plt.rc('font', family ='Malgun Gothic')
        plt.title = self.title
        fig, charLeft = plt.subplots()
        fig.set_size_inches(10,10)
        fig.dpi = 500
        charLeft.set_title(self.title)
        plt.xlabel('시간')
        temperature = False
        for colum in datas.keys():
           if '온도' in colum:
               temperature = True
        if temperature:
            charRight = charLeft.twinx()
            charRight.set_ylabel('온도')
        i=0
        j=-1
        for colum, data in datas.items():
            match graph:
                case 'plot':
                    if '온도' in colum:
                        charRight.plot(x, data, color=colors[j], label=colum)
                        j -=1
                    else:
                        charLeft.plot(x, data, color=colors[i], label=colum)
                        i+=1
        left = charLeft.legend(bbox_to_anchor=(-0.05,1), loc='upper right')
        charLeft.set_ylabel('진동')
        if temperature:
            right = charRight.legend(bbox_to_anchor=(1.05,1), loc='upper left')
        if temperature:
            legnedData = (left, right)
        else:
            legnedData = (left,)
        plt.tight_layout()
        plt.show()
    def getQuery(self, times):
        if len(times) == 1:
            timeType = 4
            time = times[0]
            title = time+" 하루 변화율"
            query = (self.dataframe['time']>=(time+' 00:00')) & (self.dataframe['time']<(time+" 23:59"))
        else:
            start = times[0]
            end = times[1]
            match len(times[0]):
                case 4:
                    timeType = 1
                    title = times[0]+"~"+times[1]+" 년도별 변화량"
                    query = (self.dataframe['time']>=(start+'-01-01 00:00')) & (self.dataframe['time']<(end+"-12-31 23:59"))
                case 7:
                    timeType = 2
                    title = times[0]+"~"+times[1]+" 달별 변화량"
                    query = (self.dataframe['time']>=(start+'-01 00:00')) & (self.dataframe['time']<(end+"-31 23:59"))
                case 10:
                    timeType = 3
                    title = times[0]+"~"+times[1]+" 일별 변화량"
                    query = (self.dataframe['time']>=(start+' 00:00')) & (self.dataframe['time']<(end+" 23:59"))
        self.setTile(title)
        return (timeType, query)
    def dataAvg(self, timeType, times, colum):
        if timeType != 4:
            end = times[1]
        start = times[0]
        match timeType:
            case 1:
                start +="-01-01"
                end +="-12-31"
            case 2:
                start +="-01"
                month = end[-2:]
                match month:
                    case '02':
                        end +="-28"
                    case '04'|'06'|'07'|'11':
                        end +="-30"
                    case _:
                        end +="-28"
        if timeType == 4:
            dateList = times
        else :
            dateList = self.date_range(start, end)
        querys = []
        match timeType:
            case 1:
                dateList = list(map(lambda date: date[:4], dateList))
                dateList = set(dateList)
                dateList = list(dateList)
                dateList.sort()
                for year in dateList:
                    querys.append((self.dataframe['time']>=(year+"-01-01 00:00")) & (self.dataframe['time']<=(year+"-12-31 23:59")))
            case 2:
                dateList = list(map(lambda date: date[:7], dateList))
                dateList = set(dateList)
                dateList = list(dateList)
                dateList.sort()
                for month in dateList:
                    querys.append((self.dataframe['time']>=(month+"-01 00:00")) & (self.dataframe['time']<=(month+"-31 23:59")))
            case 3|4:
                for date in dateList:
                    querys.append((self.dataframe['time']>=(date+" 00:00")) & (self.dataframe['time']<=(date+" 23:59")))
        dataList = []
        for query in querys:
            data = list(map(float, self.dataframe.loc[query, colum]))
            if timeType == 4:
                return data
            if not len(data)==0:
                dataList.append(sum(data)/len(data))
        return dataList       
    def setTile(self,title):
        self.title = title
    def date_range(self, start, end):
        start = datetime.strptime(start, "%Y-%m-%d")
        end = datetime.strptime(end, "%Y-%m-%d")
        dates = [(start + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end-start).days+1)]
        return dates