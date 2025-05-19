#gemini

from flask import Flask, request,render_template
import os
from ollama import Client

client = Client(
    host='http://localhost:11434',
    headers={'x-some-header': 'some-value'}
    )

app=Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return(render_template("gemini.html"))

@app.route("/gemini", methods=["GET", "POST"])
def gemini():
    return(render_template("gemini.html"))

@app.route("/gemini_reply", methods=["GET", "POST"])
def gemini_reply():
    r=None
    if request.method=='POST':
        q=request.form.get('q')
        print(f"{q}")
        r= client.chat(
                model='deepseek-r1:1.5b',
                messages=[
                {
                'role': 'user',
                'content': q
                }
                ]
            )

        r=r['message']['content']
    return(render_template("gemini_reply.html", r=r))

if __name__=="__main__":
    app.run()