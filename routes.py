import uuid
from flask import (
     Blueprint, 
     current_app, 
     render_template, 
     session, 
     redirect, 
     request, 
     url_for      )
from forms import MovieForm 

pages = Blueprint(
    "pages", __name__, template_folder="templates", static_folder="static"
)


@pages.route("/")
def index():
    return render_template(
        "index.html",
        title="Movies Watchlist",
    )

@pages.route("/add", methods=["GET", "POST"])
def add_movie():
    form = MovieForm()

    if form.validate_on_submit():
        movie = {
            "_id" : uuid.uuid4().hex,
            "title" : form.title.data,
            "director" : form.director.data,
            "year" : form.year.data
            
        }
        
        current_app.db.movie.insert_one(movie)
        
        return redirect(url_for(".index"))
        
    return render_template("new_movie.html", title="Movies Watchlist - Add Movie", form=form)

@pages.get("/toggle_theme")
def toggle_theme():
    current_theme = session.get("theme")
    if current_theme == "dark":
        session["theme"] = "light"
    else:
        session["theme"] = "dark"
    return redirect(request.args.get('current_page'))