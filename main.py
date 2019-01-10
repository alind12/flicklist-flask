from flask import Flask
import random

app = Flask(__name__)

app.config['DEBUG'] = True
# displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()
    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + str(movie[0]) + "</li>"
    content += "</ul>"

    # 2nd random movie for the next day
    content += "<h1>Tommorrow's Movie</h1>"
    content += "<ul>"
    content += "<li>" + str(movie[1]) + "</li>"
    content += "</ul>"

    return content


#Randomly chooses one of the movies and returns it:
def get_random_movie():
    movie_list = ["Aqua Man", "Batman Vs. Superman", "Green Mile", "Bugs Life", "Joker"]
    rand_movie = random.sample(movie_list, 2)
    return rand_movie


app.run()