from pathlib import Path
import json
import sys

def read_lines(fp: Path):
    encodings = ("utf-8", "utf-8-sig", "gb18030")
    for enc in encodings:
        try:
            with open(fp, "r", encoding=enc) as f:
                return [line.strip() for line in f if line.strip()]
        except Exception:
            pass
    with open(fp, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8", errors="ignore")
    return [line.strip() for line in text.splitlines() if line.strip()]

def is_chinese(ch: str) -> bool:
    code = ord(ch)
    return (
        0x4E00 <= code <= 0x9FFF
        or 0x3400 <= code <= 0x4DBF
        or 0x20000 <= code <= 0x2A6DF
        or 0x2A700 <= code <= 0x2B73F
        or 0x2B740 <= code <= 0x2B81F
        or 0x2B820 <= code <= 0x2CEAF
        or 0xF900 <= code <= 0xFAFF
    )

def first_chinese_char(s: str):
    for ch in s:
        if is_chinese(ch):
            return ch
    return None

def main():
    base = Path(__file__).parent
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else base / "成语大全(18744).txt"
    out_chars = Path(sys.argv[2]) if len(sys.argv) > 2 else base / "成语首字集合.txt"
    out_map = Path(sys.argv[3]) if len(sys.argv) > 3 else base / "成语首字母映射.json"

    lines = read_lines(src)
    firsts = []
    for line in lines:
        ch = first_chinese_char(line)
        if ch:
            firsts.append(ch)
    unique_firsts = sorted(set(firsts))

    mapping = {}
    used_letters = []
    full_py = {}
    try:
        from pypinyin import lazy_pinyin, Style
        for ch in unique_firsts:
            py = lazy_pinyin(ch, style=Style.FIRST_LETTER)
            if py and py[0]:
                mapping[ch] = py[0].upper()
                fp = lazy_pinyin(ch)
                if fp and fp[0]:
                    full_py[ch] = fp[0]
        used_letters = sorted(set(mapping.values()))
        sorted_items = sorted(mapping.items(), key=lambda kv: (kv[1], full_py.get(kv[0], ""), kv[0]))
        mapping = {k: v for k, v in sorted_items}
    except Exception:
        mapping = {}
        used_letters = []

    with open(out_chars, "w", encoding="utf-8") as f:
        f.write("\n".join(unique_firsts))

    with open(out_map, "w", encoding="utf-8") as f:
        json.dump({"mapping": mapping, "count": len(unique_firsts), "letters": used_letters}, f, ensure_ascii=False, indent=2)

    print(str(out_chars))
    print(str(out_map))
    print(len(unique_firsts))

if __name__ == "__main__":
    main()