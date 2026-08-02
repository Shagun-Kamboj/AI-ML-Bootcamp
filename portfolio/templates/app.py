from flask import Flask, render_template

from scrapper.collegedunia import scrap_colleges
from scrapper.amazon_laptops import scrap_laptops
from scrapper.books_to_scrape import scrape_books
from scrapper.the_meal_db import fetch_cookie_recipes
from scrapper.random_duck import fetch_duck
from scrapper.fake_store_api import fetch_products
from scrapper.json_placeholder import fetch_posts
from scrapper.cat_api import fetch_cats
from scrapper.yahoo_finance import scrape_yahoo_finance
from scrapper.hockey_team import fetch_hockey_teams
from scrapper.quotes_to_scrape import quotes_to_scrape
from scrapper.indeed_parser import scrape_indeed
from scrapper.ambitionbox import scrape_ambitionbox
from scrapper.nike_store import scrape_nike
#from scrapper.ambitionbox import scrape_ambitionbox

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/webscraping")
def webscraping():
    return render_template("webscraping.html")


@app.route("/static_scraping")
def static_scraping():
    return render_template("static_scraping.html")


@app.route("/dynamic_scraping")
def dynamic_scraping():
    return render_template("dynamic_scraping.html")


@app.route("/api_scraping")
def api_scraping():
    return render_template("api_scraping.html")

@app.route("/collegedunia")
def collegedunia():
    return render_template("collegedunia.html")

@app.route("/mealdb")
def mealdb():

    result = fetch_cookie_recipes()

    if result["success"]:
        return render_template(
            "the_meal_db.html",
            recipes=result["recipes"]
        )

    return render_template(
        "the_meal_db.html",
        error=result["error"]
    )

@app.route("/random_duck")
def random_duck():

    result = fetch_duck()

    if result["success"]:
        return render_template(
            "random_duck.html",
            ducks=result["ducks"]
        )

    return render_template(
        "random_duck.html",
        error=result["error"]
    )

@app.route("/fakestore")
def fakestore():

    result = fetch_products()

    if result["success"]:
        return render_template(
            "fake_store_api.html",
            products=result["products"]
        )

    return render_template(
        "fake_store_api.html",
        error=result["error"]
    )

@app.route("/jsonplaceholder")
def jsonplaceholder():

    result = fetch_posts()

    if result["success"]:
        return render_template(
            "json_placeholder.html",
            posts=result["posts"]
        )

    return render_template(
        "json_placeholder.html",
        error=result["error"]
    )

@app.route("/catapi")
def catapi():

    result = fetch_cats()

    if result["success"]:
        return render_template(
            "cat_api.html",
            cats=result["cats"]
        )

    return render_template(
        "cat_api.html",
        error=result["error"]
    )
@app.route("/static_scraping/hockey_team")
def hockey_team():

    teams = fetch_hockey_teams()

    return render_template(
        "hockey_team.html",
        teams=teams
    )

@app.route("/static_scraping/ambitionbox")
def static_scraping_ambitionbox():

    companies = scrape_ambitionbox()

    return render_template(
        "ambitionbox.html",
        companies=companies
    )
    
@app.route("/dynamic_scraping/yahoo_finance")
def yahoo_finance():

    stocks = scrape_yahoo_finance()

    return render_template(
        "yahoo_finance.html",
        stocks=stocks
    )

@app.route("/dynamic_scraping/quotes_to_scrape")
def quotes_page():

    quotes = quotes_to_scrape()

    return render_template(
        "quotes_to_scrape.html",
        quotes=quotes
    )
@app.route("/imdb_scraper")
def imdb_scraper():
    return render_template("imdb_scraper.html")


@app.route("/dynamic_scraping/nike_store")
def nike_store():

    products = scrape_nike()

    return render_template(
        "nike_store.html",
        products=products
    )

@app.route("/dynamic_scraping/indeed_parser")
def indeed_parser():

    jobs = scrape_indeed()

    return render_template(
        "indeed_parser.html",
        jobs=jobs
    )
#@app.route("/amazon")
#def amazon():
 #   laptops = scrap_laptops()
  #  return render_template("amazon_laptops.html", laptops=laptops)

@app.route("/ai_journey")
def ai_journey():
    return render_template("ai_journey.html")





@app.route('/static_scraping/collegedunia')
def static_scraping_collegedunia():
    colleges = scrap_colleges()
    return render_template("collegedunia.html", colleges = colleges)

@app.route("/static_scraping/amazon_laptops")
def static_scraping_amazon_laptops():
    laptops = scrap_laptops()
    return render_template("amazon_laptops.html", laptops=laptops)

@app.route("/static_scraping/books_to_scrape")
def static_scraping_books_to_scrape():
    books = scrape_books()
    return render_template("books_to_scrape.html",books = books)

if __name__ == "__main__":
    app.run(debug=True, port=5004,host="0.0.0.0")