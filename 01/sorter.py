import argparse
import os

from classifier import get_category
from utils import get_files, move_file, print_preview, print_summary

# 건드리면 안 되는 시스템 보호 경로
PROTECTED_PATHS = [
    "/Applications",
    "/System",
    "/Library",
    "/usr",
    "/bin",
    "/sbin",
    "/etc",
    "/private",
]

def is_protected(path: str) -> bool:
    """보호된 시스템 경로인지 확인."""
    for protected in PROTECTED_PATHS:
        if path.startswith(protected):
            return True
    return False

def parse_args():
    """CLI 옵션 정의 및 파싱."""
    parser = argparse.ArgumentParser(
        description="📂 파일 자동 분류기 - 폴더 안의 파일을 확장자별로 정리합니다."
    )
    parser.add_argument(
        "--path",
        type=str,
        default=".",
        help="정리할 폴더 경로 (기본값: 현재 폴더)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="실제로 이동하지 않고 결과를 미리 보여줍니다.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    target_path = os.path.abspath(args.path)

    # 경로 유효성 확인
    if not os.path.isdir(target_path):
        print(f"❌ 오류: '{target_path}' 는 유효한 폴더가 아닙니다.")
        return
    
    # 보호된 시스템 경로 차단
    if is_protected(target_path):
        print(f"❌ 오류: '{target_path}' 는 보호된 폴더입니다. 정리할 수 없습니다.")
        return

    print(f"\n📂 대상 폴더: {target_path}")

    files = get_files(target_path)

    if not files:
        print("정리할 파일이 없습니다.")
        return

    # 파일별로 카테고리를 계산해서 plan 딕셔너리에 모음
    # plan = { "카테고리": ["파일1", "파일2", ...] }
    plan: dict[str, list[str]] = {}
    for filename in files:
        category = get_category(filename)
        if category not in plan:
            plan[category] = []
        plan[category].append(filename)

    # dry-run 모드: 미리보기만 출력하고 종료
    if args.dry_run:
        print_preview(plan)
        return

    # 실제 이동 실행
    results: dict[str, int] = {}
    for category, filenames in plan.items():
        dest_folder = os.path.join(target_path, category)
        for filename in filenames:
            src_path = os.path.join(target_path, filename)
            move_file(src_path, dest_folder, filename)

        results[category] = len(filenames)

    print_summary(results, total=len(files))


if __name__ == "__main__":
    main()