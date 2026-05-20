# 게시글 데이터를 담아두는 리스트

import json
import os

DB_FILE = "posts.json"

# JSON 파일에서 게시글 목록 불러오기
def load_posts():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# 게시글 목록을 JSON 파일에 저장
def save_posts(posts):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)