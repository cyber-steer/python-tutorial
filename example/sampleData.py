import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os
# matplotlib에서 지원하는 색상이 10개밖에 없어서 따로 색상리스트를 생성
COLORS = ['#3e1008', '#767c7b', '#075dcd', '#339244', '#c1ebd0', '#a91e4e', '#8c293c', '#5766be', '#67f30d', '#dd6627', '#1228a8', '#981ee5', '#091a44', '#c73724', '#19130b', '#e095e4', '#1ed604', '#61495d', '#aad3fa', '#63cebf', '#a8a13d', '#8df13d', '#3f47f6', '#308a06', '#5b665f', '#5c2202', '#2059d0', '#ce1b4d', '#c7b716', '#f09624', '#779339', '#558730', '#b632f6', '#01b7fc', '#7d2656', '#5227d1', '#eb74fd', '#3b74e6', '#25aaf8', '#353d0d', '#069116', '#719768', '#73753c', '#e1332d', '#d7a709', '#70fecc', '#0ec46c', '#c41fdc', '#000783', '#a9a119']

class Data:
    # 클래스 생성시 읽을 파일의 경로를 가져와서 dataframe생성
    def __init__(self, path):
        self.dataframe = pd.read_csv(path)

    # 칼럼명을 리스트로 반환
    def getHeader(self):
        return list(self.dataframe.columns)

    # 칼럼명과 기간을 정해주면 리스트로 데이터를 반환
    def extract(self, column, dates):
        self.title = dates[0]+"~"+dates[1]+" 변화량"
        query = (self.dataframe['time']>=dates[0]) & (self.dataframe['time']<=dates[1])
        return list(map(float, self.dataframe.loc[query, column]))

    # 기간이 정해지면 실제 데이터가 있는 기간을 반환
    def extractDate(self, dates):
        query = (self.dataframe['time']>=dates[0]) & (self.dataframe['time']<=dates[1])
        return list(self.dataframe.loc[query, 'time'])
    
    # matplotlib를 사용하여 차트를 출력
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
if __name__ == "__main__":
    # 현재 실행되는 .py의 경로를 추출
    pythonpath = os.path.dirname(os.path.realpath(__file__))

    # 현재 입력되는 명령어 위치를 저장. 이게 없다면 이전으로 돌아갈때 맨처음부터 입력해야함
    commandLevel = 0
    # 종료를 원할때까지 무한 루프를 돔
    while True:
        #----------------------------------------------------------------------------------
        # 검색할 CSV파일 이름을 입력 받아 처리
        if commandLevel < 1:
            print("파일 이름 혹은 경로를 입력해주세요 ")
            print('종료 : 0')
            path = input('>>>')

            # 종료를 원할시 반복문 탈출
            if path == '0': break
            try: # 에러날 경우 except밑의 코드를 실행시켜 프로그램이 멈추는 걸 방지
                path = pythonpath+"\\"+path
                print(path)
                data = Data(path) # CSV파일을 못읽을시 에러
            except:
                print("잘못된 이름 혹은 경로입니다")
                continue
            print()
        #----------------------------------------------------------------------------------
        # 지정한 CSV파일을 읽어 dataframe이 생성됨
        if commandLevel <2:
            # 칼렴명을 흭득하여 번호를 부여해 안내문 출력
            header = data.getHeader()
            for i in range(1, len(header)):
                print("%2d : %s"%(i, header[i]))
            print("="*30)
            print('검색할 데이터를 선택해주세요')
            print('여러 데이터 선택은 공백을 기준으로 합니다')
            print('이전 : 0')
            print('종료 : -1')
            columns = input('>>>')
            # 종료를 원할시 반복문 탈출
            if columns == -1 : break
            # 이전으로 돌아가길 원할 경우
            elif columns == 0 : 
                commandLevel = 0
                continue
            # 여러가지 칼럼을 선택했을시 숫자로 변경하여 리스트로 생성
            columns = columns.split(" ")
            columns = list(map(int, columns))
            # 각 번호가 칼럼의 범위를 벗어나진 않았는지 확인
            for boolean in map(lambda n: not(n>0 and n<len(header)), columns):
                if boolean:
                    print('잘못된 번호가 입력되었습니다')
                    commandLevel == 1
                    continue

            # 선택한 칼럼의 문자열을 흭득
            columns = list(map(lambda idx: header[idx],columns))
            print(columns)
        #----------------------------------------------------------------------------------
        # 데이터를 검색할 기간을 정함
        if commandLevel <3:
            print("기간을 입력 해주세요")
            print("이전 : 0")
            print("종료 : -1")
            print("형식 : yyyy-mm-dd ~ yyyy-mm-dd")
            dates = input(">>>")
            # 종료를 원할시 반복문 탈출
            if dates == "-1": break
            # 이전으로 돌아갈 경우
            elif dates == '0':
                commandLevel=1
                continue
            # 시작 날짜와 끝 날짜를 저장
            dates = dates.split(" ~ ")
            # 실제 데이터를 저장할 변수
            datas = {}
            # 에러 검출
            error = False
            
            # 칼럼명을 하나씩 꺼내와서 데이터를 추출
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
            # 날짜 기간을 추출
            dates = data.extractDate(dates)
        #----------------------------------------------------------------------------------
            # 에러가 있을경우 차트를 그리지않고 다시 돌아감
            if error:
                continue
            # 차트를 그려줌
            data.show(dates, datas)