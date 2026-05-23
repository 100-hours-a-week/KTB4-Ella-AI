from fastapi import APIRouter
from app.schemas import PostInput, PostUpdate, PostResponse
from app.database import load_posts, add_post, update_post_db, delete_post_db

router = APIRouter()


# 게시글 작성
@router.post("/posts", response_model=PostResponse, status_code=201)    # responseBody의 구조를 맞춤
def create_post(post: PostInput):   # PostInput 모델: 요청 바디의 구조와 타입을 검증 (DB 모델과 겹치지 않도록 PostInput이라는 별도의 모델을 만들어서 사용)
    return add_post(post.username, post.title, post.content)    # add post 함수로 DB에 게시글 추가


# 게시글 목록 조회
@router.get("/posts", response_model=list[PostResponse])
def get_posts():
    return load_posts()


# 게시글 단건 조회
@router.get("/posts/{post_id}", response_model=PostResponse)
def get_post(post_id: int):
    posts = load_posts()
    for post in posts:
        if post.id == post_id:
            return post
    return {"error": "Post not found"}


# 게시글 수정
@router.put("/posts/{post_id}", response_model=PostResponse)
def update_post(post_id: int, post: PostUpdate):
    updated = update_post_db(post_id, post.title, post.content)
    if updated:
        return updated
    return {"error": "Post not found"}


# 게시글 삭제
@router.delete("/posts/{post_id}")
def delete_post(post_id: int):
    deleted = delete_post_db(post_id)
    if deleted:
        return {"message": "deleted"}
    return {"error": "Post not found"}