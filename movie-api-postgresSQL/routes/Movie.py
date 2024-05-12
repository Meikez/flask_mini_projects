from flask import Blueprint, jsonify, request

from models.MovieModel import MovieModel
from models.entities.Movie import Movie
import uuid
main = Blueprint('movie_blueprint',__name__)


@main.route('/')
def get_movies():
    try:
        movies = MovieModel.get_movies()
        return jsonify(movies)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/<id>')
def get_movie(id):
    try:
        movie = MovieModel.get_movie(id)
        if movie is not None:
            return jsonify(movie)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_movie():
    try:
        print(request.json)
        title = request.json['title']

        duration = int(request.json['duration'])

        released = request.json['released']

        # TODO: add validations
        movie_id = uuid.uuid4()

        movie = Movie(str(movie_id), title, duration, released)

        rows_numbers = MovieModel.add_movie(movie)
        print(rows_numbers)
        if rows_numbers == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': 'Error in the insert'}), 500

    except Exception as ex:
        return jsonify({'message': str(ex) + "ES ACA BOBO"}), 500


@main.route('/delete/<id>', methods=['POST'])
def delete_movie(id):
    try:
        movie = Movie(id)

        rows_affected = MovieModel.delete_movie(movie)
        if rows_affected == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': 'Error in the delete'}), 400

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_movie(id):
    try:
        title = request.json['title']
        duration = int(request.json['duration'])
        released = request.json['released']
        # TODO: add validations
        movie = Movie(id,title,duration,released)

        rows_numbers = MovieModel.update_movie(movie)
        if rows_numbers == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': 'The movie was not updated'}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500