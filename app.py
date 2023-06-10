from flask import Flask, render_template 
from news import news_blueprint

app = Flask(__name__)
app.register_blueprint(news_blueprint)

@app.route("/") 
def main_page() :
    print("hello world")
    return "<p> this is the MY MAIN PAGE</p>"

@app.route("/news") 
def news() :
      print("hello world")
      return render_template('news.html')

@app.route("/sports") 
def sports() :
    print("hello world")
    return "<p> this is the SPORTS</p>"

@app.route("/weather") 
def weather() :
    print("hello world")
    return "<p> this is the WEATHER</p>"

if __name__ == '__main__':
    app.run(debug=True, port=9000)