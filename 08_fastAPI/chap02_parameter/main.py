from fastapi import FastAPI

app = FastAPI()

# 경로 매개변수
# URL 경로에 들어가는 매개변수

#@app.get("/users/{user_id}")
#def get_user(user_id):
#    return {"user_id" : user_id}

#인터프리트 언어라서 순서가 중요. 두번째에 위치하면 위에 int 때문에 타입에러가 남
#에러가 안 나려면 첫번째에 위치해야 함.
@app.get("/users/aaa")
def get_current_user():
    return {"user_id" : 123}

# 타입을 정의하려면?
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id" : user_id}

# 경로의 순서 문제 이해
# 동작이 순서에 따라 실행되기 때문

# 쿼리 매개변수

# 호스트주소/path? 뒤에 오는 변수들을 쿼리 매개변수 라고 한다.
# 각 매개변수는 & 기호로 구분되고 key = value 쌍으로 정의된다.
#@app.get("/users")
#def get_users(limit: int, name: str):
#   return {"limit": limit, "name":name}

#http://127.0.0.1:8000/users?limit=123&name=asd
#http://localhost:8000/docs
@app.get("/users")
def get_users(limit:int = 100): #기본값 지정
    return {"limit":limit}

# 다음과 같이 앱 실행 시 포트 지정 가능.
# uvicorn main:app --port=8000 --reload