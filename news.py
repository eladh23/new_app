from flask import Blueprint ,render_template

news_blueprint = Blueprint('news',__name__, url_prefix="/news")

@news_blueprint.route('/') 
def news() :
      return render_template("news.html")

@news_blueprint.route('/global') 
def news_global() :
      return "<p>This is  Global news </p> "