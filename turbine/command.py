
import os
from datetime import datetime

def columnName(column):
    columnItems = column.split(" ")
    return columnItems[0]
def columnData(column):
    columnItems = column.split(" ")
    columnItems = columnItems[-1:0:-1]
    columnItems = " ".join(columnItems)
    return " ".join(reversed(column.split(" ")[-1:0:-1]))
def commandSelectData(item, end='종료'):
    os.system('cls')
    for i in range(1, len(item)):
        print(f'{i}. {item[i]}')
    print(f"0. {end}")
    print("="*20)
    print("* 보고 싶은 데이터 목록을 정해주세요")
    print("* 여러개 입력시 공백으로 구분, 모든 데이터는 all")
    print("* ex)>>>1 2 3\t\t* ex)>>all")
    command = input(">>>")
    print('-'*20)
    print()
    if command == '0': return 0
    elif command in ['all', 'All', 'ALL'] : command = list(range(1,len(item)))
    else: command = command.strip().split(" ")
    try:
        colum = list(map(lambda number: item[int(number)], command))
    except:
        print("\t[공백이 하나가 아니거나 데이터 범위를 벗어났습니다]")
        return -1
    return colum
def commandSelectTimeType():
    os.system('cls')
    print("1. 년 단위 데이터")
    print("2. 월 단위 데이터")
    print("3. 일 단위 데이터")
    print("4. 하루치 데이터")
    print('0. 이전')
    try:
        command = int(input('>>>'))
    except:
        print('잘못된 입력입니다')
        return -1
    if command == 0:
        return 0
    elif command<1 and command>4:
        return -1
    
    print('-'*20)
    print()
    return command
def commandSelectTime(command):
    os.system('cls')
    match command:
        case 0: return 0
        case 1:
            print('년 단위는 yyyy ~ yyyy 로 입력해주세요')
            print('* ex)>>2020 ~ 2022\t\t* ex)>>>2021 ~ 2023')
            fomat = '%Y'
        case 2:
            print('월 단위는 yyyy-mm ~ yyyy-mm 로 입력해주세요')
            print('* ex)>>2020-01 ~ 2020-12\t\t* ex)>>>2020-03 ~ 2021-08')
            fomat = '%Y-%m'
        case 3:
            print('일 단위는 yyyy-mm-dd ~ yyyy-mm-dd 로 입력해주세요')
            print('* ex)>>2020-01-01 ~ 2020-12-31\t\t* ex)>>>2020-03-13 ~ 2021-08-20')
            fomat = '%Y-%m-%d'
        case 4:
            print('일 단위는 yyyy-mm-dd 로 입력해주세요')
            print('* ex)>>2020-03-31\t\t* ex)>>>2020-09-27')
            fomat = '%Y-%m-%d'
        case _:
            return -1
    print("0. 이전")
    commandTime = input('>>>')
    if commandTime == '0' : return 0
    times = commandTime.split(" ~ ")
    try:
        for time in times:
            datetime.strptime(time, fomat)
    except:
        print("형식에 맞지 않습니다")
        return -1
    print()
    return times