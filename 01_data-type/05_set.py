# SET

# 중복을 허용하지 않으며 순서 없이 요소를 저장하는 컬렉션이다.
# 따라서 중복 제거가 필요할 때 유용하게 사용할 수 있다.
# {} 중괄호를 사용하여 집합을 생성한다.

ohgifaffers = {'pig', 'squirrel', 'baer', 'gorilla', 'pig'}
print(ohgifaffers)

# 리스트로 set 생성
another_safari_set = set(['monkey', 'tiger', 'wolf'])
print(another_safari_set)

mixed_set = {1, 'bear', (1,2,3)}
print(mixed_set)

ohgifaffers.remove('pig')
print(ohgifaffers)

ohgifaffers.add('pig')
print(ohgifaffers)

#SET 메소드

#1. update()
ohgifaffers1 = set(["monkey",'tiger','wolf'])
print(ohgifaffers1)
ohgifaffers1.update(["monkey",'wolf','tiger','squirrel'])
print(ohgifaffers1)

# 2. discard()
ohgifaffers1.discard('pig')                                     #값이 존재하지 않아도 에러를 발생시키 않는다.

# 3.pop()
ohgifaffers1.pop()                                              #집합의 순서를 보장하지 않기 때문에 어떤 것이 제거될지 알 수 없다.
print(ohgifaffers1)

# 4.clear()
ohgifaffers1.clear()
print(ohgifaffers1)

# 5.union() : 두 set 합집합
javaTeam = {'gorilla', 'tiger', 'monkey'}
pythonTeam = {'pig', 'bear', 'gorilla', 'tiger'}

ohgifaffers2 = javaTeam.union(pythonTeam)                       #중복을 제외한 합집합
print(ohgifaffers2)

# 6. intersection() : 두 set 자료형의 교집합을 반환
print(javaTeam.intersection(pythonTeam))

# 7.defference() : 좌향을 기준으로 우향의 차집합을 반환한다.
print(javaTeam.difference(pythonTeam))

# 8.copy() : 대상 set을 복사하여 반환한다.
javaTeam1 = javaTeam.copy()
print(id(javaTeam))
print(id(javaTeam1))