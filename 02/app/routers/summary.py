import os
import requests
from fastapi import APIRouter
from dotenv import load_dotenv
from app.database import load_posts

load_dotenv()  # .env 파일에서 환경변수 불러오기

router = APIRouter()

# 환경변수에서 API 키 가져오기
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# Gemini API 요청 URL (API 키를 쿼리스트링으로 전달)
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"


def ask_gemini(prompt: str) -> str:
    # Gemini API에 POST 요청 — contents 안에 프롬프트 전달
    response = requests.post(
        GEMINI_URL,
        json={"contents": [{"parts": [{"text": prompt}]}]}
    )
    result = response.json()
    # 응답 구조: candidates → content → parts → text
    return result["candidates"][0]["content"]["parts"][0]["text"]


# 게시글 요약
@router.get("/posts/{post_id}/summary")
def summarize_post(post_id: int):
    posts = load_posts()
    for post in posts:
        if post.id == post_id:
            # 요약 요청 프롬프트 생성
            prompt = f"다음 게시글을 한 문장으로 요약해줘.\n제목: {post.title}\n내용: {post.content}"
            summary = ask_gemini(prompt)
            return {"summary": summary}
    return {"error": "Post not found"}