from fastapi import APIRouter
from app.schemas import Post
from app.database import posts

router = APIRouter()


# 게시글 작성
@router.post("/posts", status_code=201)
def create_post(post: Post):
    new_post = {
        "id": len(posts) + 1,  # 현재 리스트 길이 + 1을 id로 사용
        "username": post.username,
        "title": post.title,
        "content": post.content
    }
    posts.append(new_post)
    return new_post


# 게시글 목록 조회
@router.get("/posts")
def get_posts():
    return posts


# 게시글 단건 조회
@router.get("/posts/{post_id}")
def get_post(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return post
    return {"error": "Post not found"}


# 게시글 수정 (전체 필드 교체)
@router.put("/posts/{post_id}")
def update_post(post_id: int, post: Post):
    for p in posts:
        if p["id"] == post_id:
            p["title"] = post.title
            p["content"] = post.content
            return p
    return {"error": "Post not found"}


# 게시글 삭제
@router.delete("/posts/{post_id}")
def delete_post(post_id: int):
    for i, p in enumerate(posts):
        if p["id"] == post_id:
            posts.pop(i)  # 인덱스로 리스트에서 제거
            return {"message": "deleted"}
    return {"error": "Post not found"}