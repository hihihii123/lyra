import pdfplumber
import json
import re


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
    current_subtopic = None
    collect_objectives = False
    text = []

    for page in pdf.pages[3:6]:
        text += [i.rsplit(" ",1)[0] for i in page.extract_text().split("\n")] # Removes page number
    
    tempdata = []

    n = 0
    while n < len(text):
        possible = text[n]
        if "Chapter" in possible:
            chapterdata = {"chaptername": possible, "subtopics": []} # Sets structure for mains
            n += 1
            while n < len(text) and "Chapter" not in text[n]:
                if "." in text[n]:
                    chapterdata["subtopics"].append({"name": text[n], "objectives": [], "content": []}) # Structure for each subtopic
                n += 1
            chapters.append(chapterdata)
        else:
            n += 1  
            

    content_match = re.compile(r"^(\d+\.\d+)\s")   # + is one or more of \d=int, \s=char
    objective_match = re.compile(r"^\d+\.\d+\.\d+")
    def is_learning_outcomes(line):
        upper = line.upper()
        return "LEARNING" in upper and "OUTCOME" in upper

    for page in pdf.pages[7:]:
        text = page.extract_text(x_tolerance=6, y_tolerance=6) or ""
        text = (cleanLines(text.split("\n")))

    
        for t in text:
            text = t.strip()

            if not text:
                continue

            cmatch = content_match.match(text) # does it match pattern
            if cmatch:
                cnum = cmatch.group(1)   # matches first () in pattern
                for chapter in chapters:
                    for sub in chapter["subtopics"]:
                        if sub["name"].startswith(cnum):
                            current_subtopic = sub
                            
                collect_objectives = False
                continue


            # Check if is learning outcomes
            if is_learning_outcomes(text):
                collect_objectives = True
                continue

            if collect_objectives and objective_match.match(text):
                if current_subtopic:
                    current_subtopic["objectives"].append(text)
                continue

            # Stop collecting if line matches objective
            if collect_objectives and not objective_match.match(text):
                collect_objectives = False

            if current_subtopic:
                current_subtopic["content"].append(text)
                

with open("resources/DATA.json", "w", encoding="utf-8") as fout:
    json.dump(chapters, fout, indent=2, ensure_ascii=False)
    print("Saved json")