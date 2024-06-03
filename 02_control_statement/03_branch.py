# 분기문

# else 문
# 정상적으로 모든 루프가 종료된 후 else 안에 있는 내용이 실행된다.

for x in [1, 2, 3]:
    print(x)
else:
    print('끝')         # 모든 루프가 실행 된 뒤에 처리되는 부분, 정상적으로 종료되었을 때만

# continue 문
# 반복문 안에서 continue를 만나면 다음 실행문은 실행되지 않고 다음 반복문으로 넘어간다.
# 특정 순간을 생략하고 진행하기 위해 사용된다.
for i in range(3):
    if i == 1:
        continue
    print(i)

# break 문
# 반복문을 종료할 때 사용한다.
# break를 만나면 남은 과정은 모두 취소된다.

for x in [1,2,3]:
    if x == 2:
        print("끝1")
        break
    else:
        print(x)