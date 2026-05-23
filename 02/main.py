from fastapi import FastAPI
from app.routers import posts, summary
from app.database import init_db

app = FastAPI()

# 서버 시작할 때 DB 초기화
init_db()   # 테이블이 없으면 생성, 있으면 그냥 넘어감

# 게시글 라우터 등록
app.include_router(posts.router)

# 요약 라우터 등록
app.include_router(summary.router)