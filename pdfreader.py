import pdfplumber
import json
import re


def cleanLines(text):
    result = []
    temp = ""

    # Joins spacing between sentences
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

    # Removes page number
    for page in pdf.pages[3:6]:
        text += [i.rsplit(" ",1)[0] for i in page.extract_text().split("\n")]
    
    # Sets structure to populate
    n = 0
    while n < len(text):
        possible = text[n]
        if "Chapter" in possible:
            chapterdata = {"chaptername": possible, "subtopics": []} # Structure for main chapters
            n += 1
            while n < len(text) and "Chapter" not in text[n]:
                if "." in text[n]:
                    chapterdata["subtopics"].append({"name": text[n], "objectives": [], "content": []}) # Structure for each subtopic
                n += 1
            chapters.append(chapterdata)
        else:
            n += 1  
            
    objective_match = re.compile(r"\d+\.\d+\.\d+\s+.+")  # + is one or more of \d=int, \s=char

    # Populate content & objectives
    for page in pdf.pages[7:]:
        text = page.extract_text(x_tolerance=6, y_tolerance=6) or ""
        text = (cleanLines(text.split("\n")))
    
        for t in text:
            if not t:
                continue
            for chapter in chapters:
                for sub in chapter["subtopics"]:
                    if sub["name"] in t:
                        current_subtopic = sub
                        collect_objectives = False
                        continue

            # Check if is learning outcomes
            if "LLEEAARRNNIINNGG OOUUTTCCOOMMEESS" in t:
                collect_objectives = True
                
            if collect_objectives:  # Numbered objective
                if objective_match.search(t):
                    if current_subtopic:
                        current_subtopic["objectives"].append(objective_match.search(t).group(0))
                        
                else:
                    collect_objectives = False  # Stop collecting 

            # Populate content
            if current_subtopic:
                current_subtopic["content"].append(t)
        

with open("resources/DATA.json", "w", encoding="utf-8") as fout:
    json.dump(chapters, fout, indent=2, ensure_ascii=False)
    print("Saved json")