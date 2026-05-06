import json
from pathlib import Path

# 当前脚本所在目录：中华成语
BASE_DIR = Path(__file__).resolve().parent
TXT_PATH = BASE_DIR / "成语大全(18744).txt"
JSON_PATH = BASE_DIR / "chengyu_all_simple.json"


def txt_to_json():
    if not TXT_PATH.exists():
        raise FileNotFoundError(f"找不到成语大全文件: {TXT_PATH}")

    idioms = []
    with TXT_PATH.open("r", encoding="utf-8") as f:
        for idx, line in enumerate(f, start=1):
            text = line.strip()
            if not text:
                continue
            idioms.append({"id": idx, "text": text})

    with JSON_PATH.open("w", encoding="utf-8") as f:
        json.dump(idioms, f, ensure_ascii=False, indent=2)

    print(f"已从 {TXT_PATH.name} 读取 {len(idioms)} 条成语，写入 {JSON_PATH.name}")


if __name__ == "__main__":
    txt_to_json()
