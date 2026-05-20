# Pydantic 모델 : 데이터의 구조와 타입을 정의하는 모델

from pydantic import BaseModel

class Post(BaseModel):
    username: str
    title: str
    content: str