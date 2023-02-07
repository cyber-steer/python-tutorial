import os # 운영체제 명령어 여기선 콘솔화면 지우기 위해 사용
from itertools import product # 행렬 조합 ['a','b'] 과 [1,2,3]  => [('a',1),('a',2),('a',3),('b',1),('b',2),('b',3),]
from Data import Data # 직접 만든 클래스로 차트를 그리기 위한 전반적인 코드
from command import * # 직접 만든 모듈로 사용자 입력을 위한 안내문

if __name__ == "__main__":
    # ==================================== 데이터 초기 설정 =============================================
    os.system('cls') # 콘솔 화면 초기화
    path = "tubine/2_T5_data.CSV" # 데이터를 읽을 csv파일 경로
    csv = Data(path) # 객체 생성
    columList = csv.head() # 전체 칼럼 명

    # ----------------터빈의 숫자를 추출--------------------------------------
    # turbinNumberList =set(map((lambda column: column.split(" ")[0]), colums)) # 아래 코드와 동일하지만 람다식 사용
    turbinNumberList = set(map(columnName, columList))
    turbinNumberList = list(turbinNumberList)
    turbinNumberList.sort()
    # ------------------['터빈1번','터빈2'...]----------------------------------

    #-----------------터빈의 데이터를 추출
    # turbinDataList =set(map((lambda column: " ".join(reversed(column.split(" ")[-1:0:-1]))), colums)) # 아래 코드와 동일하지만 람다식 사용
    turbinDataList = set(map(columnData, columList))
    turbinDataList = list(turbinDataList)
    turbinDataList.sort()
    commandLevel = 0
    # ------------------['베어링 X축 진동', '베어링 Y축 진동', '베어링 금속 온도']----------------------------------
    # ==================================================================================================
    while True:
        # 터빈 종류 선택-----------------------------------------------------
        if commandLevel < 1:
            columNames = commandSelectData(turbinNumberList)
            if columNames == 0: break
            elif columNames ==-1: 
                commandLevel = 0
                continue

        # 터빈 데이터 선택-----------------------------------------------------
        if commandLevel <2:
            columDatas = commandSelectData(turbinDataList, '이전')
            while columDatas == -1:
                columDatas = commandSelectData(turbinDataList, '이전')
            if columDatas == 0 :
                commandLevel = 0
                continue

        # 날짜 선택 -----------------------------------------------------
        if commandLevel <3:
            timeType = commandSelectTimeType()
            while timeType == -1:
                timeType = commandSelectTimeType()
            if timeType == 0:
                commandLevel = 1
                continue
            else: commandLevel = 0
        if commandLevel <4:
            times = commandSelectTime(timeType)
            while times == -1:
                times = commandSelectTime(timeType)
            if times == 0:
                commandLevel = 2
                continue
            else: commandLevel = 0
        # ------------------------------------------------------
        colums = []
        for i in product(columNames,columDatas,repeat=1):
            colums.append(i[0]+" "+i[1])
        datas = []
        for colum in colums:
            datas.append(csv.extract(colum, times))
        data = {}
        for itemName, itemData in zip(colums, datas):
            data[itemName] = itemData
        times = csv.extract('time', times)
        csv.show('plot', times, data)
        # break