# python의 기본 자료형()과 자료구조()
# ,python에서 #은 한줄 주석, 여러줄 주석은 지원하지 않는다.

# 기본 자료형
# 1.숫자형
#  int   : 정수 값을 가지는 자료형
#  float : 소수 값을 가지는 자료형

num1 = 1
num2 = 3.14

print(type(num1))
print(type(num2))

# 연산
num3 = 11
num4 = 7

print(num3 + num4)
print(num3 - num4)
print(num3 * num4)
print(num3 / num4)
print(num3 % num4)

# 몫만 구하는 연산
print(num3 // num4)

# 제곱 연산
base = 9
exponent = 3
print(base ** exponent)

# 2. 논리형(Bool)
bool1 = True
bool2 = False

print(type(bool1))
print(type(bool2))

# 3. 문자형(String), '', "" 둘다 사용 가능
fruit = 'apple'
print(fruit)

capasity = str(300)
print(capasity)

#삼중 따옴표 : 텍스트를 여러줄로 안의 내용들을 출력가능
print("""
      Long 코트보다 긴건?
      double 코트
      짧은건?
      int 패딩
""")

# 문자열은 index를 가지고 있어 인덱싱을 통해 원하는 위치의 문자 하나를 추출할 수 있다.
# 띄어쓰기도 문자열에 포함 됨.
address = '대한민국 서울시 서초구'
print(address[5])
print(address[9])

#슬라이싱
print(address[9:])     #9번 인덱스부터 끝까지
print(address[5:8])    #5번 인덱스부터 8번 인덱스까지
print(address[1:12:4]) #1번부터 12번 인덱스까지, 4개씩 건너 띄어서
print(address[::-1])   #문자열 뒤집기
print(address[-3:])    #뒤에서 3번째부터 끝까지

# 문자열 *(곱하기) 연산
subject = 'python'
print(subject * 3)

#문자열 관련 메소드
# 1. replace() : 문자열을 치환하는 메소드이다.
enroll_date = '2024/12/16'
rep_enroll_date = enroll_date.replace("/", "-")
print(rep_enroll_date)

#2.strip() : 제거할 문자 집합을 지정하는 메소드
origin = 'ohgiraffers'
with_white_space = '    oh giraffers'
print(with_white_space.strip())
print(with_white_space.strip('  o'))
print(with_white_space.strip('  os'))

# 3.대소문자 관련 메소드
origin_str = 'hELLO wORLD!'
print(origin_str.upper())
print(origin_str.lower())
print(origin_str.capitalize())  #맨 첫번째 문자만 대문자로 치환해줌.

# 4.문자형 포맷
# 변수 포맷을 이용하여 문자열에 변수 갑을 삽입할 수 있다.
# 변수 포맷 종류
  # %s : 문자열
  # %c : 문자
  # %d : 정수
  # %f : 실수

x = 10
print("x is %d" % x)  #어떤 변수와 매칭 시키는지 지정하기 위해 변수 앞에 %를 붙인다.

y = 'code'
print("y is %s" % y)

print("x is {0}"         .format(x))       #{}, 즉 중괄호 안에 인덱스 번호(순서)를 지정하여 변수를 매칭하고 출력 할수 있다.
print("x is {0} y is {1}".format(x, y))    #x is 10 y is code

#형 변환
#암시적 형 변환
print(True + 3)   #정수는 True는 1, False는 0
print(3 + 5.0)    #자동 float로 형변환 됨.
#print(3 + '5')   #이건 명시적으로 형변환 해야 한다.

#명시적 형 변환
print(int('3') + 4)
print(float('3'))

print(str(1))
print(str(1.0))
print(str({1, 2, 3}))