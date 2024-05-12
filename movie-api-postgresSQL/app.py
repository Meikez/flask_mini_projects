from flask import Flask
from config import config
from routes import Movie
app = Flask(__name__)


def not_found(error):
    return "<h1>Not found! </h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])


    # Blueprints
    app.register_blueprint(Movie.main,url_prefix='/api/movies')

    # Error handlers
    #app.register_error_handler(404, not_found)
    app.run()