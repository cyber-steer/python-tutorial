#==============================================================================
# 특정한 코드를 반복시키기 위한 문이다
# 크게 while문과 false문이 있다
#==============================================================================


#==============================================================================
#                           반복문의 기본 구조
#------------------------------------------------------------------------------
# for 변수명 in 다중값데이터: 의 구조를 가진다
# in이라는 키워드는 원래 어떠한 값이 있는지 검색하는 키워드지만
# in과 for키워드를 같이 쓰면 데이터를 하나씩 가져와서 밑에 코드를 실행하게 된다
# 이때 가져온 데이터는 '변수명'에 할당되어 for문 안 코드에서 사용할수 있다
#
# while 조건식:의 구조를 가진다
# 조건식은 True나 False가 나올수 있는 식을 넣어야하고
# 조건식의 결과가 True일 동안 while문 내의 코드를 반복하게 된다
# while문은 특정한 이벤트가 발생하기 전까지 계속 프로그램을 돌리기위해 많이 쓴다
# 하지만 while문을 잘못쓰면 무한루프를 돌아 강제로 종료해야만 하는 불상사가 일어날수도 있다
#==============================================================================
print("="*20,"반복문의 기본 구조","="*20)
print("-"*20,"for문의 기본구조","-"*20)
print('''for variable in sequence:
    print("실행할 코드")''')
print("-"*20,"while문의 기본구조","-"*20)
print('''while 조건식:
    print("실행할 코드")''')
print("="*50)
#==============================================================================
print()
#==============================================================================
#                           for문
#------------------------------------------------------------------------------
# for문은 어떤 다중값을 가지는 데이터 타입에서 데이터를 하나씩 꺼내와 실행한다
# 다중값을 가지는 데이터 타입을 쉽게 만들기 위해 range()를 많이 쓴다
#------------------------------------------------------------------------------
print("="*20,"for문","="*20)
l = [1,2,3,4,5]
print(f'l : {l}')
print("-"*50)
for i in l:
    print(f'i : {i}')
print("="*50)
#==============================================================================
print()
#==============================================================================
#                           for문
#------------------------------------------------------------------------------
# while문은 조건식이 참일동안 무한히 실행 된다
# 그러니 적절하게 while문을 벗어날수 있도록 해야 한다
#------------------------------------------------------------------------------
print("="*20,"while문","="*20)
i = 0
print(f'i : {i}')
print("-"*50)
while i<5:
    i += 1
    print(f'i : {i}')
print("="*50)
#==============================================================================