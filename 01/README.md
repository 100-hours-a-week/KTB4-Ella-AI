# 📂 파일 자동 분류기 (File Sorter)

지정한 폴더 안의 파일을 확장자 기준으로 자동 분류하는 CLI 프로그램입니다.

---

## 실행 환경

- Python 3.14.5
- 외부 라이브러리 없음

---

## 파일 구조

```
01/
├── sorter.py        # 메인 실행 파일
├── classifier.py    # 확장자 → 카테고리 분류 로직
├── utils.py         # 파일 이동 및 출력 유틸 함수
└── README.md
```

---

## 사용법

### 기본 실행 (현재 폴더 정리)
```bash
python3 sorter.py
```

### 폴더 지정
```bash
python3 sorter.py --path ~/Downloads
```

### 미리보기 (실제 이동 없이 결과 확인)
```bash
python3 sorter.py --path ~/Downloads --dry-run
```

---

## 분류 카테고리

| 카테고리 | 확장자 |
|--------|------|
| 이미지 | .jpg .jpeg .png .gif .bmp .webp .svg |
| 문서 | .pdf .doc .docx .ppt .pptx .xls .xlsx .txt .hwp .md |
| 영상 | .mp4 .mov .avi .mkv .wmv |
| 음악 | .mp3 .wav .flac .aac |
| 압축 | .zip .rar .tar .gz .7z |
| 코드 | .py .js .ts .html .css .java .c .cpp .json .xml .sh |
| 설치파일 | .dmg .pkg .exe |
| 기타 | 위 목록에 없는 확장자 |

---

## 실행 예시

```
📂 대상 폴더: /Users/byun/Downloads

✅ 총 5개 파일 정리 완료!

  문서: 1개
  설치파일: 2개
  이미지: 2개
```