from flask import Flask, render_template, request
import wikipedia
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search",methods=['GET','POST'])
def search_query():
    search_query = request.form.get('query')
    try:
        summary = wikipedia.summary(search_query)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return ("There  are many types please specify in detail and search again")

if __name__ == "__main__":
    app.run(use_reloader= True, debug= True)
