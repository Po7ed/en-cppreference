import os
import re
import json

def clean_title(t):
    s = " - cppreference.com"
    if t.endswith(s):
        return t[:-len(s)].strip()
    return t

def extract_title(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()
        m = re.search(r"<title>(.*?)</title>", text, re.IGNORECASE | re.DOTALL)
        if not m:
            return None
        raw = m.group(1).strip()
        return clean_title(raw)
    except:
        return None

def collect(dir_name, lang):
    out = []
    for root, _, files in os.walk(dir_name):
        for fn in files:
            if fn.lower().endswith(".html"):
                full = os.path.join(root, fn)
                title = extract_title(full)
                if not title:
                    continue
                url = os.path.relpath(full, ".").replace("\\", "/")
                out.append({"title": title, "url": url, "lang": lang})
    return out

en = collect("en", "en")
zh = collect("zh", "zh")

all_data = en + zh
with open("search.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

