#gemini

from flask import Flask, request,render_template
import google.generativeai as genai
import os

app=Flask(__name__)

# google api is from https://makersuite.google.com

# Run locally based on the configuration file, uncomment the following two lines
#app.config.from_pyfile("config.py", silent=True) 
#api_key=app.config['SECRET_KEY']

# Run in colab, the uncomment the following two lines
#from google.colab import userdata
#api_key = userdata.get('makersuite')

# Run in render.com or locally based on the environment variable, then uncomment the following line. MAKESUITE_API_KEY need to add into Enviornment Variables
api_key = os.getenv('MAKERSUITE_API_KEY')

genai.configure(api_key=api_key)
model= genai.GenerativeModel("gemini-2.0-flash-001") #gemini-1.5-flash

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
        r= model.generate_content(q)
        r=r.text
    return(render_template("gemini_reply.html", r=r))

if __name__=="__main__":
    app.run()