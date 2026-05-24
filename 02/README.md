# 커뮤니티 서비스 백엔드 API

FastAPI로 구현한 커뮤니티 서비스 백엔드

---

## 기술 스택

| 기술 | 설명 |
|---|---|
| FastAPI | 파이썬 웹 프레임워크 |
| SQLModel | DB 테이블 정의 및 쿼리 ORM |
| SQLite | 로컬 데이터베이스 (나중에 mysql 등으로 대체 가능) |
| Gemini 2.5 Flash | 게시글/댓글 요약 LLM |
| uvicorn | ASGI 서버 |
| uv | 패키지 관리 도구 |

---

## 프로젝트 구조

```
02/
├── main.py              # 진입점 — 라우터 등록 및 서버 시작
├── app/
│   ├── database.py      # DB 연결, 테이블 모델, CRUD 함수
│   ├── schemas.py       # 요청/응답 Pydantic 모델
│   └── routers/
│       ├── posts.py     # 게시글 CRUD 라우터
│       ├── comments.py  # 댓글 CRUD 라우터
│       └── summary.py   # LLM 요약 라우터
├── .env                 # 환경변수 (API 키 등)
└── pyproject.toml       # 패키지 의존성 관리
```

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

### 5. 환경변수 설정

`.env` 파일을 루트에 생성하고 Gemini API 키 입력
Gemini API 키 받는 곳 https://aistudio.google.com/api-keys

```
GEMINI_API_KEY=your_api_key_here
```

### 6. 가상환경 활성화

```bash
source .venv/bin/activate
```

### 7. 서버 실행

```bash
uvicorn main:app --reload
```

> ✅ Swagger 문서: `http://127.0.0.1:8000/docs`

---

## 단계별 진행 과정

### 1단계: 메모리 기반 게시글 CRUD
`main.py` 하나에 FastAPI 앱과 게시글 CRUD를 인메모리 리스트로 구현했다. 서버를 재시작하면 데이터가 초기화되는 한계가 있었다.

### 2단계: 구조 분리 리팩토링
`main.py`가 길어지면서 역할별로 파일을 분리했다. 라우터는 `routers/`, Pydantic 모델은 `schemas.py`, 저장소는 `database.py`로 나눴다.

### 3단계: JSON 파일 저장으로 전환
인메모리 리스트 대신 JSON 파일에 데이터를 저장하도록 변경했다. 서버를 재시작해도 데이터가 유지되지만, 검색과 관리가 불편한 한계가 있었다.

### 4단계: SQLite + SQLModel DB 도입
JSON 파일 대신 SQLite DB를 SQLModel ORM으로 연결했다. 테이블을 파이썬 클래스로 정의하고, SQL 쿼리 없이 파이썬 코드로 DB를 다룰 수 있다는 점을 수업 때 배웠었고, 코드로 확인해 볼 수 있었다. `database.py`만 교체하고 나머지 구조는 그대로 유지했다.

### 5단계: Gemini API 연동
Gemini 2.5 Flash API를 연동해 게시글 요약 기능을 추가했다. API 키는 `.env` 파일로 관리하였다.

### 6단계: 댓글 CRUD + 댓글 요약
댓글 테이블을 추가하고 댓글 CRUD와 댓글 목록 요약 기능을 구현했다. 게시글과 댓글은 `post_id`로 연결했다.

---

## API 설계

### 게시글 (Posts)

| 기능 | 메서드 | 경로 | 요청 바디 | 응답 |
|---|---|---|---|---|
| 게시글 작성 | `POST` | `/posts` | `{"username": "...", "title": "...", "content": "..."}` | `201` + 생성된 게시글 |
| 게시글 목록 조회 | `GET` | `/posts` | 없음 | `200` + 게시글 배열 |
| 게시글 단건 조회 | `GET` | `/posts/{post_id}` | 없음 | `200` + 게시글 |
| 게시글 수정 | `PUT` | `/posts/{post_id}` | `{"title": "...", "content": "..."}` | `200` + 수정된 게시글 |
| 게시글 삭제 | `DELETE` | `/posts/{post_id}` | 없음 | `200` + `{"message": "deleted"}` |

#### 게시글 데이터 구조

```json
{
  "id": 1,
  "username": "ella",
  "title": "제목",
  "content": "내용"
}
```

---

### 댓글 (Comments)

| 기능 | 메서드 | 경로 | 요청 바디 | 응답 |
|---|---|---|---|---|
| 댓글 작성 | `POST` | `/posts/{post_id}/comments` | `{"username": "...", "content": "..."}` | `201` + 생성된 댓글 |
| 댓글 목록 조회 | `GET` | `/posts/{post_id}/comments` | 없음 | `200` + 댓글 배열 |
| 댓글 수정 | `PUT` | `/posts/{post_id}/comments/{comment_id}` | `{"content": "..."}` | `200` + 수정된 댓글 |
| 댓글 삭제 | `DELETE` | `/posts/{post_id}/comments/{comment_id}` | 없음 | `200` + `{"message": "deleted"}` |

#### 댓글 데이터 구조

```json
{
  "id": 1,
  "post_id": 1,
  "username": "ella",
  "content": "댓글 내용"
}
```

---

### LLM 요약

| 기능 | 메서드 | 경로 | 응답 |
|---|---|---|---|
| 게시글 요약 | `GET` | `/posts/{post_id}/summary` | `200` + 요약 텍스트 |
| 댓글 요약 | `GET` | `/posts/{post_id}/comments/summary` | `200` + 요약 텍스트 |

---

## 느낀 점

기존에 DB 연결 경험은 IntelliJ에서 Spring으로 작성된 프로젝트를 MySQL에 연결해본 것이 전부였는데, 이번 과제를 통해 SQLite와 SQLModel을 처음 접하게 됐다. 또한 파이썬으로 직접 서버를 작성해본 것도 처음이었다.

강사님께서 LLM 연동을 먼저 언급하셨지만, 실제 개발 과정에서 DB가 먼저 구축되어야 LLM이 데이터를 활용할 수 있다는 것이 더 와닿아 DB를 먼저 구현하는 방향으로 진행했다.

선택 과제였던 Ollama 연동은 이번에 해보지 못했지만, 나중에 기회가 되면 로컬 LLM을 직접 연결해보고 싶다.