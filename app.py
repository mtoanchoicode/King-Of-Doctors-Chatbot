from flask import Flask, render_template, request
import os
from openai import OpenAI

client = OpenAI(
   api_key=os.environ.get("API_KEY"),
)

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods =["POST"])
def api():
    message = request.json.get("message")
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are 'King Of Doctor' always say \"Hello I'm King Of Doctor\", a pharmacist assistant. For the symptom user give, you need to suggest 1 medicine and some information about that medicine including 5 things medicine name, dosage, side effects, indications, contraindications. Give the anwser within 500 tokens"},
            {"role": "user", "content": message}
        ],
        max_tokens=200
    )

    if completion.choices[0].message != None:
        return completion.choices[0].message.content

    else :
        return 'Failed to Generate response!'
    
if __name__ == '__main__':
    app.run()