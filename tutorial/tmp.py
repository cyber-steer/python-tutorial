struct ='''if 조건식:
    print('조건입 참입니다')
else:
    print('조건입 거짓입니다')'''
print(struct.find('조건식'))
struct=struct.replace('조건식','True')
print(struct)