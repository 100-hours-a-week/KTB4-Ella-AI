# API 설계 (1단계 - 메모리 기반)
 
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