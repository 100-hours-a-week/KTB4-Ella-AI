# 커뮤니티 서비스 백엔드 API
 
FastAPI로 구현한 커뮤니티 서비스 백엔드
 
---
 
## 시작하기
 
### 1. 레포지토리 클론
 
```bash
git clone {레포지토리 주소}
cd 02
```
 
### 2. uv 설치
 
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
 
### 3. PATH 등록
 
```bash
source $HOME/.local/bin/env
```
 
### 4. 패키지 설치
 
```bash
uv sync
```
 
### 5. 가상환경 활성화
 
```bash
source .venv/bin/activate
```
 
### 6. 서버 실행
 
```bash
uvicorn main:app --reload
```
 
> Swagger 문서: `http://127.0.0.1:8000/docs`
 
---

# API 설계 (메모리 기반)
 
## 게시글 (Posts)
 
| 기능 | 메서드 | 경로 | 요청 바디 | 응답 |
|---|---|---|---|---|
| 게시글 작성 | `POST` | `/posts` | `{"title": "...", "content": "...", "username": "..."}` | `201` + 생성된 게시글 |
| 게시글 목록 조회 | `GET` | `/posts` | 없음 | `200` + 게시글 배열 |
| 게시글 단건 조회 | `GET` | `/posts/{post_id}` | 없음 | `200` + 게시글 |
| 게시글 수정 | `PUT` | `/posts/{post_id}` | `{"title": "...", "content": "..."}` | `200` + 수정된 게시글 |
| 게시글 삭제 | `DELETE` | `/posts/{post_id}` | 없음 | `200` + `{"message": "deleted"}` |
 
### 게시글 데이터 구조
 
```json
{
  "id": 1,
  "username": "ella",
  "title": "제목",
  "content": "내용"
}
```
 
---