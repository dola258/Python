from flask import Flask
from flask.templating import render_template
import movie_api as ma
import temp_bs as tempbs


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", movies = ma.callMovieApi(), temps = tempbs.temp() ) # default가 1이라서 안넣어도 1로 된다. 

if __name__ == "__main__":
    app.run(debug=True)

