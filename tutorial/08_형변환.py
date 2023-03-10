#==============================================================================
# 형변환이란 데이터타입을 변경하는 것이다
# 예시로 문자열 '1'을 숫자 1로 변경하거나 하는 것을 말한다
# 단일 데이터 타입은 서로 변환이 가능하다
# 다중 데이터 타입들끼리 데이터 변환이 가능하다
# 딕셔너리같은 경우는 key와 value의 쌍으로 이루어져 있기때문에 주의가 필요하다
# 불린값음 0이나 데이터가 없을때만 flase를 반환하며 나머지는 true를 반환한다
#==============================================================================

#==============================================================================
#                           형변환 함수
#------------------------------------------------------------------------------
# int()
# float()
# str()
# list()
# tuple()
# dict()
# set()
#==============================================================================

#==============================================================================
#                           int에서의 변환
#------------------------------------------------------------------------------
# float로 변경할시 소수점이 붙게 된다
#------------------------------------------------------------------------------
x = 10
print("="*20,"int에서의 변환","="*20)
print(f'{type(x)}\tx : {x}')
print("-"*50)
print(f'float(x) : {float(x)}\t\t{type(float(x))}')
print(f'str(x) : {str(x)}\t\t{type(str(x))}')
print("="*50)
#==============================================================================
print()
#==============================================================================
#                           float에서의 변환
#------------------------------------------------------------------------------
# int로 변환시 소수점 자리는 버리게 된다
#------------------------------------------------------------------------------
x = 3.14
print("="*20,"float에서의 변환","="*20)
print(f'{type(x)}\tx : {x}')
print("-"*50)
print(f'int(x) : {int(x)}\t\t{type(int(x))}')
print(f'str(x) : {str(x)}\t\t{type(str(x))}')
print("="*50)
#==============================================================================
print()
#==============================================================================
#                           str에서의 변환
#------------------------------------------------------------------------------
# 소수점을 int로 바꾸기 위해선 먼저 float으로 변한한뒤 int로 변환해야 오류가 없다
#------------------------------------------------------------------------------
x = '314'
print("="*20,"str에서의 변환","="*20)
print(f'{type(x)}\tx : {x}')
print("-"*50)
print(f'int(x) : {int(x)}\t\t{type(int(x))}')
print(f'float(x) : {float(x)}\t{type(float(x))}')
print("="*50)
#==============================================================================
print()
#==============================================================================
#                           list에서의 변환
#------------------------------------------------------------------------------
x = [1,2,3]
print("="*20,"str에서의 변환","="*20)
print(f'{type(x)}\tx : {x}')
print("-"*50)
# print(f'int(x) : {int(x)}\t\t{type(int(x))}')
# print(f'float(x) : {float(x)}\t\t{type(float(x))}')
print(f'list(x) : {list(x)}\t{type(list(x))}')
print(f'tuple(x) : {tuple(x)}\t{type(tuple(x))}')
# print(f'dict(x) : {dict(x)}\t{type(dict(x))}')
print(f'set(x) : {set(x)}\t{type(set(x))}')
print(f'str(x) : {str(x)}\t{type(str(x))}')
print("="*50)
#==============================================================================
print()
#==============================================================================
#                           tuple에서의 변환
#------------------------------------------------------------------------------
x = (1,2,3)
print("="*20,"tuple에서의 변환","="*20)
print(f'{type(x)}\tx : {x}')
print("-"*50)
# print(f'int(x) : {int(x)}\t\t{type(int(x))}')
# print(f'float(x) : {float(x)}\t\t{type(float(x))}')
print(f'list(x) : {list(x)}\t{type(list(x))}')
print(f'tuple(x) : {tuple(x)}\t{type(tuple(x))}')
# print(f'dict(x) : {dict(x)}\t{type(dict(x))}')
print(f'set(x) : {set(x)}\t{type(set(x))}')
print(f'str(x) : {str(x)}\t{type(str(x))}')
print("="*50)
#==============================================================================
print()
#==============================================================================
#                           set에서의 변환
#------------------------------------------------------------------------------
x = {1,2,3}
print("="*20,"str에서의 변환","="*20)
print(f'{type(x)}\tx : {x}')
print("-"*50)
# print(f'int(x) : {int(x)}\t\t{type(int(x))}')
# print(f'float(x) : {float(x)}\t\t{type(float(x))}')
print(f'list(x) : {list(x)}\t{type(list(x))}')
print(f'tuple(x) : {tuple(x)}\t{type(tuple(x))}')
# print(f'dict(x) : {dict(x)}\t{type(dict(x))}')
print(f'set(x) : {set(x)}\t{type(set(x))}')
print(f'str(x) : {str(x)}\t{type(str(x))}')
print("="*50)
#==============================================================================
print()
#==============================================================================
#                           bool에서의 변환
#------------------------------------------------------------------------------
t, f = True, False
print("="*20,"bool에서의 변환","="*20)
print(f'{type(t)}\tt : {t}\tf :{f}')
print("-"*50)
print(f'int(t) : {int(t)}\t\t{type(int(t))}')
print(f'float(t) : {float(t)}\t\t{type(float(t))}')
print(f'str(t) : {str(t)}\t\t{type(str(t))}')
print("="*50)
#==============================================================================
print()
#==============================================================================
#                           문자열로 변환
#------------------------------------------------------------------------------
# 모든 데이터 타입은 문자열로 변환이 가능하다
#------------------------------------------------------------------------------
print("="*20,"문자열로 변환","="*20)
print(f'str(10) : {str(10)}\t\t\t{type(str(10))}')
print(f'str(3.14) : {str(3.14)}\t\t{type(str(3.14))}')
print(f'str([1,2,3]) : {str([1,2,3])}\t{type(str([1,2,3]))}')
print(f'str((1,2,3)) : {str((1,2,3))}\t{type(str((1,2,3)))}')
x = {'k':'v'}
print(f'str({x}) : {str(x)}\t{type(str(x))}')
print(f'str({1,2,3}) : {str({1,2,3})}\t{type(str({1,2,3}))}')
print("="*50)
#==============================================================================
print()
#==============================================================================
#                           dict로 변환
#------------------------------------------------------------------------------
# dict로 변경할시 key와 value값 쌍으로 들어가기 때문에
# 매개변수 값이 key와 value값 두개씩 들어간다
# dict.fromkeys(key, value) 함수를 이용해 key와 value쌍을 넘겨서 만들수 있다
# 반복문을 이용해 key로 넘기고 value값을 특정 값으로 할수도
# 반복문을 이요해 value로 넘기고 key값을 숫자로 넣을수도 있지만 다루진 않겠습니다
# 또는 zip을 이용해 묶을수 있지만 추후 다르도록 하겠습니다
#------------------------------------------------------------------------------
print("="*20,"dict로 변환 fromkeys()이용","="*20)
keyList = ['a','b','c']
d= dict.fromkeys(keyList, 0)
print(f'keyList:{keyList}')
print(f'dict.fromkeys(keyList, 0)\t{d}')
print("-"*50)
keyList = tuple(keyList)
d= dict.fromkeys(keyList, 0)
print(f'keyList:{keyList}')
print(f'dict.fromkeys(keyList, 0)\t{d}')
print("-"*50)
keyList = set(keyList)
d= dict.fromkeys(keyList, 0)
print(f'keyList:{keyList}')
print(f'dict.fromkeys(keyList, 0)\t{d}')
print("-"*50)
print("="*50)
#==============================================================================