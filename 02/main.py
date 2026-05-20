from fastapi import FastAPI
from app.routers import posts

app = FastAPI()

# 게시글 라우터 등록
app.include_router(posts.router)