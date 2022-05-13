import json
from flask import Flask

with open('candidates.json', encoding="utf-8") as f:
    candidates_data = json.load(f)


def index():
    page = """"""
    for can in candidates_data:
        page += f"""имя: {can["name"]} \n skills: {can["skills"]} \n"""
    return page

app = Flask(__name__)

@app.route('/')
def index_page():
    return index()

# def page_index():
#     return (candidates_data)


app.run()

