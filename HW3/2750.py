a = set() ##set 함수를 사용하는 이유는 중복 거를 수 있으므로
b = int(input())
for i in range(b): ## 새로 알게 된 tip : 여러줄을 넣을 땐 b로 넣기
    a.add(int(input())) ## tip : 순수 input 그대로 넣어야 함 b를 넣으면 덩어리로 들어가기 때문에 인식을 못함
c = list(a)
for k in range(len(c)):
    print(c[k])
