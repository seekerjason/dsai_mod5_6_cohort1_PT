#gemini

from flask import Flask, request,render_template
import google.generativeai as genai
import os

app=Flask(__name__)

# google api is from https://makersuite.google.com
# Run locally, uncomment the following line
#app.config.from_pyfile("config.py", silent=True) 
#config.py contains the secret_key which is the api_key of gemini

# Run in colab, the uncomment the following two lines
#from google.colab import userdata
#api = userdata.get('makersuite')

# Run in render.com, then uncomment the following line. MAKESUITE_API_KEY need to add into Enviornment Variables
makersuite_api_key = os.getenv('MAKERSUITE_API_KEY')


genai.configure(api_key=app.config['SECRET_KEY'])
model= genai.GenerativeModel("gemini-1.5-flash") #gemini-2.0-flash-001

@app.route("/", methods=['GET', 'POST'])
def index():
    return(render_template("index.html"))

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