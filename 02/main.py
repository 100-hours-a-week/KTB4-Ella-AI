from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 게시글 데이터 모델
class Post(BaseModel):
    username: str
    title: str
    content: str

# 인메모리 저장소
posts = []

# 게시글 작성
@app.post("/posts", status_code=201)
def create_post(post: Post):
    new_post = {
        "id": len(posts) + 1,
        "username": post.username,
        "title": post.title,
        "content": post.content
    }
    posts.append(new_post)
    return new_post

# 게시글 목록 조회
@app.get("/posts")
def get_posts():
    return posts

# 게시글 단건 조회
@app.get("/posts/{post_id}")
def get_post(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return post
    return {"error": "Post not found"}

# 게시글 수정
@app.put("/posts/{post_id}")
def update_post(post_id: int, post: Post):
    for p in posts:
        if p["id"] == post_id:
            p["title"] = post.title
            p["content"] = post.content
            return p
    return {"error": "Post not found"}

# 게시글 삭제
@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    for i, p in enumerate(posts):
        if p["id"] == post_id:
            posts.pop(i)
            return {"message": "deleted"}
    return {"error": "Post not found"}