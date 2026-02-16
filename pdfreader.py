import pdfplumber
import json


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

    return (result if result else "")

def cleanTable():
    pass


chapters = []
with pdfplumber.open("resources/Computing Textbook.pdf") as pdf:
    text = []
    for page in pdf.pages[3:6]:
        text += [i.rsplit(" ",1)[0] for i in page.extract_text().split("\n")] # removes page number
    
    tempdata = []

    n = 0
    while n < len(text):
        possible = text[n]
        if "Chapter" in possible:
            chapterdata = {"chaptername": possible, "subtopics": []}
            n += 1
            while n < len(text) and "Chapter" not in text[n]:
                if "." in text[n]:
                    chapterdata["subtopics"].append({"name": text[n], "content": []})
                n += 1
            chapters.append(chapterdata)
        else:
            n += 1  
            

    # /TODO/
    for page in pdf.pages[7:]:
        text = page.extract_text(x_tolerance=6, y_tolerance=6) or ""
        text = (cleanLines(text.split("\n")))

        

with open("resources/DATA.json", "w", encoding="utf-8") as fout:
    json.dump(chapters, fout, indent=2, ensure_ascii=False)
    print("Saved json")