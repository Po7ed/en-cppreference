import os, json, re

roots = ["en", "zh"]
res = []

for base in roots:
    for root, dirs, files in os.walk(base):
        for f in files:
            if not f.endswith(".html"):
                continue

            path = os.path.join(root, f)
            # URL 从仓库根目录开始
            url = "/" + os.path.normpath(path).replace("\\", "/")

            try:
                txt = open(path, encoding="utf-8", errors="ignore").read()
            except:
                continue

            m = re.search(r"<title>(.*?)</title>", txt, re.I | re.S)
            title = m.group(1).strip() if m else f

            res.append({"title": title, "url": url})

with open("search.json", "w", encoding="utf-8") as fd:
    json.dump(res, fd, ensure_ascii=False)

