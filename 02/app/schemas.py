# SQLModel 방식에서는 DB 모델이 Pydantic 모델의 역할도 같이 함. 따라서 별도의 Pydantic 모델이 필요하지 않음.
# Pydantic 모델 : 데이터의 구조와 타입을 정의하는 모델

from sqlmodel import SQLModel

# 게시글 생성 요청 바디
class PostInput(SQLModel):
    username: str
    title: str
    content: str

# 게시글 수정 요청 바디
class PostUpdate(SQLModel):
    title: str
    content: str

# 게시글 응답 모델
class PostResponse(SQLModel):
    id: int
    username: str
    title: str
    content: str