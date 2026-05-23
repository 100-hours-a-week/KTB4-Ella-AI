from fastapi import APIRouter
from app.schemas import CommentInput, CommentUpdate, CommentResponse
from app.database import load_comments, add_comment, update_comment_db, delete_comment_db

router = APIRouter()


# 댓글 작성
@router.post("/posts/{post_id}/comments", response_model=CommentResponse, status_code=201)
def create_comment(post_id: int, comment: CommentInput):
    return add_comment(post_id, comment.username, comment.content)


# 댓글 목록 조회
@router.get("/posts/{post_id}/comments", response_model=list[CommentResponse])
def get_comments(post_id: int):
    return load_comments(post_id)


# 댓글 수정
@router.put("/posts/{post_id}/comments/{comment_id}", response_model=CommentResponse)
def update_comment(post_id: int, comment_id: int, comment: CommentUpdate):
    updated = update_comment_db(comment_id, comment.content)
    if updated:
        return updated
    return {"error": "Comment not found"}


# 댓글 삭제
@router.delete("/posts/{post_id}/comments/{comment_id}")
def delete_comment(post_id: int, comment_id: int):
    deleted = delete_comment_db(comment_id)
    if deleted:
        return {"message": "deleted"}
    return {"error": "Comment not found"}