from flask import Flask, render_template 
from news import news_blueprint

app = Flask(__name__)
app.register_blueprint(news_blueprint)

@app.route("/") 
def main_page() :
    print("hello world")
    news_arr = ["war in gaza", "eurovision start in 10" , "messi in israel" ]
    return render_template("main.html", news_arr = news_arr)

@app.route("/news") 
def news() :
      print("hello world")
      return render_template('news.html')

@app.route("/sports") 
def sports() :
    print("hello world")
    return render_template("sports.html")

@app.route("/weather") 
def weather() :
    print("hello world")
    return render_template("weather.html")

if __name__ == '__main__':
    app.run(debug=True, port=9000)