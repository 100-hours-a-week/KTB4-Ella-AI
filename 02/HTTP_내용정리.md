# HTTP 정리

## 1. HTTP란?

**HyperText Transfer Protocol**의 약자로, 클라이언트와 서버가 데이터를 주고받기 위한 규칙(프로토콜)이에요.

- 가장 대표적인 클라이언트: **브라우저**
- plain text → **HyperText** 로 발전
- 현재는 텍스트(HTML, CSS, JS)뿐만 아니라 이미지(JPG, PNG 등) 바이너리 파일도 전송 가능

---

## 2. 클라이언트 & 서버

```
클라이언트 (요청) ←————————→ 서버 (응답)
     브라우저                   백엔드 서버
```

- **클라이언트**: 요청을 보내는 주체 (브라우저, curl, requests 등)
- **서버**: 요청을 받아 응답을 돌려주는 주체
- 서버는 24시간 운영되며 **무한 루프(event loop)** 를 돌고 있음

---

## 3. HTTP URL 구조

```
https://example.com:80/posts?id=3
  │         │         │   │     │
스킴    도메인(호스트) 포트 경로  쿼리스트링
```

| 구성요소 | 설명 | 예시 |
|---|---|---|
| 스킴 | 프로토콜 종류 | `https` |
| 도메인 | 서버 주소 | `example.com` |
| 포트 | 서버 내 종착지 구분 (HTTP 기본값: 80, HTTPS: 443) | `:80` |
| 경로 | 요청하는 리소스 위치 | `/posts` |
| 쿼리스트링 | 추가 파라미터 | `?id=3` |

---

## 4. HTTP Message 구조

### Request Message (클라이언트 → 서버)

```
POST /posts HTTP/1.1
Content-Type: application/json

{"title": "제목", "content": "내용"}
```

### Response Message (서버 → 클라이언트)

```
HTTP/1.1 201 Created
Content-Type: application/json

{"id": 1, "title": "제목", "content": "내용"}
```

> 헤더와 바디는 `\r\n\r\n` 으로 구분

---

## 5. HTTP 요청 메서드 ⭐

| 메서드 | 역할 | 본문(Body) |
|---|---|---|
| `GET` | 조회 (읽기) | ❌ |
| `POST` | 생성 (쓰기) | ✅ |
| `PUT` | 전체 수정 | ✅ |
| `PATCH` | 부분 수정 | ✅ |
| `DELETE` | 삭제 | 선택 |

### GET: 클라이언트가 서버에 정보를 보내는 방법

```
경로 매개변수 (Path Variable):   /posts/3
질의 매개변수 (Query String):    /posts?id=3
```

### PUT vs PATCH

- `PUT`: 리소스 **전체**를 교체
- `PATCH`: 리소스 **일부**만 수정
- ex) 게시글에서 제목만 바꾸고 싶으면 `PATCH`가 더 적절

---

## 6. HTTP 상태코드 ⭐

| 코드 | 분류 | 대표 예시 |
|---|---|---|
| `2xx` | 성공 | `200 OK`, `201 Created` |
| `3xx` | 리다이렉션 | `301 Moved Permanently` |
| `4xx` | 클라이언트 오류 | `400 Bad Request`, `404 Not Found` |
| `5xx` | 서버 오류 | `500 Internal Server Error` |

### 자주 쓰는 상태코드

| 코드 | 의미 | 언제 쓰나 |
|---|---|---|
| `200` | OK | 일반적인 성공 |
| `201` | Created | POST 요청으로 생성 성공 시 |
| `400` | Bad Request | 클라이언트가 잘못된 요청을 보낸 경우 |
| `401` | Unauthorized | 인증이 필요한 경우 |
| `403` | Forbidden | 권한이 없는 경우 |
| `404` | Not Found | 리소스를 찾을 수 없는 경우 |
| `422` | Unprocessable Entity | 유효성 검사 실패 (FastAPI에서 자주 등장) |
| `500` | Internal Server Error | 서버 내부 오류 |

> 오류의 판단 주체는 **서버** — 서버가 400/500을 결정함

---

## 7. HTTP 동작 흐름
 
```
[클라이언트]                        [서버]
    │                                  │
    │── TCP 연결 (3-way handshake) ──▶│
    │                                  │
    │── HTTP Request ────────────────▶│
    │      GET /index.html HTTP/1.1    │
    │                                  │
    │◀─── HTTP Response ──────────────│
    │       200 OK + HTML Body         │
    │                                  │
    │── 연결 종료 (or Keep-Alive) ───▶│
```

---

## 8. REST API

**이름(URI 경로) + 교환 방식(HTTP 메서드) + 메시지 형식(JSON)** 의 조합

| CRUD | HTTP 메서드 |
|---|---|
| Create | `POST` |
| Retrieve | `GET` |
| Update | `PUT` / `PATCH` |
| Delete | `DELETE` |

### REST의 핵심 원칙

- **무상태(Stateless)**: 서버가 클라이언트 상태를 저장하지 않음
- **자원 기반 URL**: `/getUser` ❌ → `/users/1` ✅

---

## 9. JSON

**JavaScript Object Notation** — 서버와 클라이언트 간 데이터 교환의 표준

```json
{
  "id": 1,
  "title": "제목",
  "content": "내용",
  "username": "ella"
}
```

- Key-Value 쌍으로 이루어진 데이터 형식
- 배열(`[]`) 포함 가능
- 과거엔 XML이 표준이었으나 현재는 JSON이 주류 (XML : JSON ≈ 20 : 80)