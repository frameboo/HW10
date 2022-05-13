import json
from flask import Flask

with open('candidates.json', encoding="utf-8") as f:
    candidates_data = json.load(f)

app = Flask(__name__)


@app.route('/')
def index_page():
    page = ""
    for c in candidates_data:
        page += "Имя кандидата: " + c["name"] + "\n"
        page += "Позиция кандидата: " + c["position"] + "\n"
        page += "Навыки: " + c["skills"] + "\n" + "\n"
    return "<pre>" + page + "</pre>"


@app.route("/candidates/<int:x>")
def page_candidate(x):
    page = ""
    for i in candidates_data:
        if x == i["id"]:
            img_src = i["picture"] + "\n"
            page += "Имя кандидата: " + i["name"] + "\n"
            page += "Позиция кандидата: " + i["position"] + "\n"
            page += "Навыки: " + i["skills"] + "\n" + "\n"

    return f"<img src = {img_src}>" + "\n" + "<pre>" + page + "</pre>"

@app.route("/skills/<xx>")
def page_skills(xx):
    page = ""
    for i in candidates_data:
        skil_list = i["skills"].lower().split(", ")
        if xx.lower() in skil_list:
            page += "Имя кандидата: " + i["name"] + "\n"
            page += "Позиция кандидата: " + i["position"] + "\n"
            page += "Навыки: " + i["skills"] + "\n" + "\n"
    return "<pre>" + page + "</pre>"


app.run()

