import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os
COLORS = ['#3e1008', '#767c7b', '#075dcd', '#339244', '#c1ebd0', '#a91e4e', '#8c293c', '#5766be', '#67f30d', '#dd6627', '#1228a8', '#981ee5', '#091a44', '#c73724', '#19130b', '#e095e4', '#1ed604', '#61495d', '#aad3fa', '#63cebf', '#a8a13d', '#8df13d', '#3f47f6', '#308a06', '#5b665f', '#5c2202', '#2059d0', '#ce1b4d', '#c7b716', '#f09624', '#779339', '#558730', '#b632f6', '#01b7fc', '#7d2656', '#5227d1', '#eb74fd', '#3b74e6', '#25aaf8', '#353d0d', '#069116', '#719768', '#73753c', '#e1332d', '#d7a709', '#70fecc', '#0ec46c', '#c41fdc', '#000783', '#a9a119']

class Data:
    def __init__(self, path):
        self.dataframe = pd.read_csv(path)

    def getHeader(self):
        return list(self.dataframe.columns)

    def extract(self, column, dates):
        self.title = dates[0]+"~"+dates[1]+" 변화량"
        query = (self.dataframe['time']>=dates[0]) & (self.dataframe['time']<=dates[1])
        return list(map(float, self.dataframe.loc[query, column]))
    def extractDate(self, dates):
        query = (self.dataframe['time']>=dates[0]) & (self.dataframe['time']<=dates[1])
        return list(self.dataframe.loc[query, 'time'])
    
    def show(self, dates, datas, label=False):
        global COLORS
        plt.rc('font', family ='Malgun Gothic')
        plt.title = self.title
        plt.figure(figsize=(20,10), dpi=100)
        i=0
        for column, data in datas.items():
            plt.plot(dates, data, color=COLORS[i], label=column)
            i+=1
        plt.xlabel('시간')
        if label:
            plt.ylabel(label)
        plt.legend()
        plt.show()
    
    def date_range(self, start, end):
        start = datetime.strptime(start, "%Y-%m-%d")
        end = datetime.strptime(end, "%Y-%m-%d")
        dates = [(start + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end-start).days+1)]
        return dates

if __name__ == "__main__":
    pythonpath = os.path.dirname(os.path.realpath(__file__))
    commandLevel = 0
    while True:
        if commandLevel < 1:
            print("파일 이름 혹은 경로를 입력해주세요 ")
            print('종료 : 0')
            path = input('>>>')
            if path == '0': break
            try:
                path = pythonpath+"\\"+path
                print(path)
                data = Data(path)
            except:
                print("잘못된 이름 혹은 경로입니다")
                continue
            print()
        if commandLevel <2:
            header = data.getHeader()
            for i in range(1, len(header)):
                print("%2d : %s"%(i, header[i]))
            print("="*30)
            print('검색할 데이터를 선택해주세요')
            print('여러 데이터 선택은 공백을 기준으로 합니다')
            print('이전 : 0')
            print('종료 : -1')
            columns = input('>>>')
            if columns == -1 : break
            elif columns == 0 : 
                commandLevel = 0
                continue
            columns = columns.split(" ")
            columns = list(map(int, columns))
            for boolean in map(lambda n: not(n>0 and n<len(header)), columns):
                if boolean:
                    print('잘못된 번호가 입력되었습니다')
                    commandLevel == 1
                    continue

            columns = list(map(lambda idx: header[idx],columns))
            print(columns)
        if commandLevel <3:
            print("기간을 입력 해주세요")
            print("이전 : 0")
            print("종료 : -1")
            print("형식 : yyyy-mm-dd ~ yyyy-mm-dd")
            dates = input(">>>")
            if dates == "-1": break
            elif dates == '0':
                commandLevel=1
                continue
            dates = dates.split(" ~ ")
            datas = {}

            error = False
            
            for column in columns:
                if column ==' ': continue
                try:
                    d = data.extract(column, dates)
                    datas[column] = d
                except Exception as e:
                    print("기간이 잘못 입력되었습니다")
                    print(e)
                    commandLevel == 2
                    error = True
                    break
            dates = data.extractDate(dates)
            if error:
                continue
            data.show(dates, datas)

        break