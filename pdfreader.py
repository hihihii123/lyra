import pdfplumber
import re
import json

chapters = []

def cleanLines(text):
    result = []
    temp = ""

    for line in text:
        line = line.strip()
        if not line:
            continue
        if not line.endswith((".", "!", "?", ":", ";")):
            temp += " " + line
        else:
            temp += " " + line
            result.append(temp.strip())
            temp = ""

    if temp.strip():
        result.append(temp.strip())

    return result


with pdfplumber.open("resources/Computing Textbook.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text(x_tolerance=2, y_tolerance=2) or ""
        text = (text.split("\n"))

        for line in text:
            line = line.strip()
            if not line:
                continue

with open("DATA.json", "w", encoding="utf-8") as fout:
    json.dump(fout, indent=2, ensure_ascii=False)
    print("Saved to json")
