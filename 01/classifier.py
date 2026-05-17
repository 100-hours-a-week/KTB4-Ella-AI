# 확장자 → 폴더 이름 매핑 규칙
EXTENSION_MAP = {
    # 이미지
    ".jpg": "이미지",
    ".jpeg": "이미지",
    ".png": "이미지",
    ".gif": "이미지",
    ".bmp": "이미지",
    ".webp": "이미지",
    ".svg": "이미지",

    # 문서
    ".pdf": "문서",
    ".doc": "문서",
    ".docx": "문서",
    ".ppt": "문서",
    ".pptx": "문서",
    ".xls": "문서",
    ".xlsx": "문서",
    ".txt": "문서",
    ".hwp": "문서",
    ".md": "문서",

    # 영상
    ".mp4": "영상",
    ".mov": "영상",
    ".avi": "영상",
    ".mkv": "영상",
    ".wmv": "영상",

    # 음악
    ".mp3": "음악",
    ".wav": "음악",
    ".flac": "음악",
    ".aac": "음악",

    # 압축
    ".zip": "압축",
    ".rar": "압축",
    ".tar": "압축",
    ".gz": "압축",
    ".7z": "압축",

    # 코드
    ".py": "코드",
    ".js": "코드",
    ".ts": "코드",
    ".html": "코드",
    ".css": "코드",
    ".java": "코드",
    ".c": "코드",
    ".cpp": "코드",
    ".json": "코드",
    ".xml": "코드",
    ".sh": "코드",

    # 설치 파일
    ".exe": "설치 파일",
    ".dmg": "설치 파일",
    ".pkg": "설치 파일",
}


def get_category(filename: str) -> str:
    """
    파일명을 받아서 어느 카테고리(폴더)에 넣을지 반환.
    매핑에 없는 확장자면 '기타'로 분류.
    """
    _, ext = os.path.splitext(filename)
    return EXTENSION_MAP.get(ext.lower(), "기타")


# os 모듈은 sorter.py에서 import하지만 여기서도 필요하므로 추가
import os