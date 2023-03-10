#==============================================================================
# 변수란 변할수 있는 값으로 언제든 다른값으로 대체 가능
# 단일값 데이터에는 int(정수), float(실수), c(복소수), str(문자열)이 있고
# 다중값 데이터에는 list(리스트), tuple(튜플), dict(딕셔너리), set(집합)이 있다
#==============================================================================

#==============================================================================
#                                   변수 할당
#-----------------------------------------------------------------------------
# 변수명 = 값
# 변수 할당은 좌측에 변수명 우측에 값을 적는 형태이다
#-----------------------------------------------------------------------------
i = 10                          # 정수 할당
f = 3.14                        # 실수 할당
c = 1+1j                        # 복소수 할당
st = "hello"                    # 문자열 할당
l = [i,f,c,st]                  # 리스트 할당
t = (i,f,c,st,l)                # 튜플 할당
d = {"key":"value", i:l, st:f}  # 딕셔너리 할당, 값에 다중값(list, tuple, dict, set)은 사용불가
s = {i,f,c,st}                  # 집합 할당, 다중값은 할당 불가
print("="*20,"변수할당","="*20)
print(f'{type(i)} i : {i}')
print(f'{type(f)} f : {f}')
print(f'{type(c)} c : {c}')
print(f'{type(st)} st : {st}')
print(f'{type(l)} l : {l}')
print(f'{type(t)} t : {t}')
print(f'{type(d)} d : {d}')
print(f'{type(s)} s : {s}')
print("="*50)
#==============================================================================
print()
#==============================================================================
#                               기본적인 연산
#-----------------------------------------------------------------------------
# 변수명, 변수명, .... 변수명 = 값, 값, .... 값
# 한번에 여러 변수에 할당하는것도 가능하다
#------------------------------------------------------------------------------
a,b = 2, 3     # 변수 할당
print("="*20,"기본 연산","="*20)
print(f'a : {a}\tb : {b}')
print("-"*50)
print("a + b :",a+b)      # 덧셈 연산
print("a - b :",a-b)      # 빼기 연산
print("a * b :",a*b)      # 곱하기 연산
print("a / b :",a/b)      # 나누기 연산
print("a % b :",a%b)      # 나머지 연산
print("a ** b :",a**b)     # 제곱 연산
print("a // b :",a//b)     # 몫 연산
print("="*50)
#==============================================================================
print()
#==============================================================================
#                           문자열 연산
#-----------------------------------------------------------------------------
# 문자열은 덧셈과 곱셈이 가능하다
#------------------------------------------------------------------------------
a, b = "hello", "world"
print("="*20,"문자열 연산","="*20)
print(f'a : {a}\tb : {b}')
print("-"*50)
print(f'a + b : {a+b}')     # 문자열끼리 덧셈
print(f'a * 3 : {a*3}')     # 문자열에 숫자 곱
#==============================================================================
print()
#==============================================================================
#                           리스트 연산
#-----------------------------------------------------------------------------
# 리스트도 덧셈과 곱셈이 가능하다
# 리스트는 특정 항목에 대해 직접적인 수정이 가능하다
#------------------------------------------------------------------------------
a = [1,2,3,4,5]
b = ['a','b','c','d','e']
print("="*20,"리스트 연산","="*20)
print(f'a : {a}\tb : {b}')
print("-"*50)
print(f'a + b : {a+b}')
print(f'a * 3 : {a*3}')
a[0] = 0
print(f'a[0] =0 : {a}')
#==============================================================================
print()
#==============================================================================
#                           튜플 연산
#-----------------------------------------------------------------------------
# 튜플도 덧셈과 곱셈이 가능하다
#------------------------------------------------------------------------------
a = (1,2,3,4,5)
b = ('a','b','c','d','e')
print("="*20,"튜플 연산","="*20)
print(f'a : {a}\tb : {b}')
print("-"*50)
print(f'a + b : {a+b}')
print(f'a * 3 : {a*3}')
#==============================================================================

