#==============================================================================
# 출력은 연산의 결과를 외부로 보내는 것
# 출력을 해주는 하드웨어로는 모니터, 프린터 등이 있다
# 입력은 연산을 위한 데이터를 외부에서 받아오는것
# 입력을 받아올수 있는 하드웨어로는 마우스, 키보드, 센서 등이 있다
# 모니터(콘솔)로 출력할때 쓰는 함수는 print()이다
#==============================================================================

#==============================================================================
#                           ''와 ""차이
#-----------------------------------------------------------------------------
# '와 "는 동일하지만 출력할때 "이나 '를 출력하고자 할때 차이가 생긴다
#-----------------------------------------------------------------------------
print("="*20,"따옴표 사용","="*20)
print('"큰 따옴표" 사용')
print("'작은 따옴표' 사용")
print("="*50)
#==============================================================================
print()
#==============================================================================
#                       다양한 출력 방식
#------------------------------------------------------------------------------
print("="*20,"다양한 출력 방식","="*20)
a, b, c = 10, 20, 30
# ,를 구분하여 출력
print("a :", a, "\tb :", b, "\tc :", c)

# 서식문자 사용
print("a : %d\tb : %d\tc : %d"%(a, b, c))

# format 사용
print("a : {}\tb : {}\tc : {}".format(a,b,c))
print("a : {1}\tb : {0}\tc : {2}".format(b,a,c))

# f스트링은 중괄호 "{}" 안에 변수명 기입
print(f"a : {a}\tb : {b}\tc : {c}")

print("="*50)
#==============================================================================
print()
#==============================================================================
#                       print()함수의 매개변수
#------------------------------------------------------------------------------
# print()함수는 sep의 기본값이 공백, end의 기본값은 줄바뀜
print("hello","world", sep=" ", end="\n")

print("hello",'world',sep=":/:", end="@@\n")
#==============================================================================