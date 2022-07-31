#while문 맨 처음으로 돌아가기
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0 : continue
    print(a)

#무한 루프
#while True:
#수행할 문장1
#수행할 문장2

while True:
    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")

#for문
#1.전형적인 for문
test_list = ['one','two','three']
for i in test_list:
    print(i)