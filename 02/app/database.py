# 게시글 데이터를 담아두는 리스트

from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Optional

DB_FILE = "sqlite:///posts.db"  # 저장소 파일 경로 (SQLite DB 파일)

# DB 엔진 생성
engine = create_engine(DB_FILE)

# 게시글 테이블 모델
class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    title: str
    content: str

# 댓글 테이블 모델
class Comment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    post_id: int = Field(foreign_key="post.id")  # 게시글 외래키
    username: str
    content: str

# DB 초기화 — 테이블이 없으면 생성
def init_db():
    SQLModel.metadata.create_all(engine)

# 게시글 목록 불러오기
def load_posts():
    with Session(engine) as session:
        return session.exec(select(Post)).all()

# 게시글 추가
def add_post(username: str, title: str, content: str):
    with Session(engine) as session:
        post = Post(username=username, title=title, content=content)
        session.add(post)
        session.commit()
        session.refresh(post)
        return post

# 게시글 수정
def update_post_db(post_id: int, title: str, content: str):
    with Session(engine) as session:
        post = session.get(Post, post_id)
        if post:
            post.title = title
            post.content = content
            session.commit()
            session.refresh(post)
            return post
        return None

# 게시글 삭제
def delete_post_db(post_id: int):
    with Session(engine) as session:
        post = session.get(Post, post_id)
        if post:
            session.delete(post)
            session.commit()
            return True
        return False
    
# 댓글 목록 불러오기
def load_comments(post_id: int):
    with Session(engine) as session:
        return session.exec(select(Comment).where(Comment.post_id == post_id)).all()


# 댓글 추가
def add_comment(post_id: int, username: str, content: str):
    with Session(engine) as session:
        comment = Comment(post_id=post_id, username=username, content=content)
        session.add(comment)
        session.commit()
        session.refresh(comment)
        return comment


# 댓글 수정
def update_comment_db(comment_id: int, content: str):
    with Session(engine) as session:
        comment = session.get(Comment, comment_id)
        if comment:
            comment.content = content
            session.commit()
            session.refresh(comment)
            return comment
        return None


# 댓글 삭제
def delete_comment_db(comment_id: int):
    with Session(engine) as session:
        comment = session.get(Comment, comment_id)
        if comment:
            session.delete(comment)
            session.commit()
            return True
        return False