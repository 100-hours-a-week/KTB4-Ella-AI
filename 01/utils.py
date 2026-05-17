import os
import shutil


def get_files(path: str) -> list[str]:
    """
    지정된 폴더에서 파일 목록만 반환 (하위 폴더 제외).
    """
    entries = os.listdir(path)
    files = [
        f for f in entries
        if os.path.isfile(os.path.join(path, f))
        and not f.startswith(".")  # 숨김 파일 제외
    ]
    return files


def move_file(src_path: str, dest_folder: str, filename: str) -> None:
    """
    파일을 목적지 폴더로 이동.
    목적지 폴더가 없으면 자동으로 생성.
    """
    os.makedirs(dest_folder, exist_ok=True)
    dest_path = os.path.join(dest_folder, filename)

    # 같은 이름의 파일이 이미 있으면 파일명 뒤에 숫자를 붙여서 중복 방지
    if os.path.exists(dest_path):
        base, ext = os.path.splitext(filename)
        counter = 1
        while os.path.exists(dest_path):
            dest_path = os.path.join(dest_folder, f"{base}_{counter}{ext}")
            counter += 1

    shutil.move(src_path, dest_path)


def print_preview(plan: dict[str, list[str]]) -> None:
    """
    dry-run 모드: 실제 이동 없이 어떻게 정리될지 출력.
    plan = { "카테고리명": ["파일1", "파일2", ...] }
    """
    print("\n[미리보기] 아래와 같이 정리됩니다:\n")
    for category, files in sorted(plan.items()):
        print(f"  📁 {category}/")
        for f in files:
            print(f"      {f}")
    print()


def print_summary(results: dict[str, int], total: int) -> None:
    """
    실제 이동 완료 후 결과 요약 출력.
    results = { "카테고리명": 이동된_파일_수 }
    """
    print(f"\n✅ 총 {total}개 파일 정리 완료!\n")
    for category, count in sorted(results.items()):
        print(f"  {category}: {count}개")
    print()