import argparse
import requests
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from termcolor import colored
import bcrypt

# Constants
API_KEY = '3fd2be6f0c70a2a598f084ddfb75487c'
BASE_URL = 'https://api.themoviedb.org/3'

# Rated Movies List
rated_movies = []

# SQLAlchemy setup
Base = declarative_base()
engine = create_engine('sqlite:///movie_db.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

# Database Models
class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    overview = Column(String)
    release_date = Column(String)
    vote_average = Column(Float)
    recommended = Column(Boolean, default=False)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String)
    password = Column(String)

Base.metadata.create_all(engine)

# User Authentication Functions
def register_user():
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = input("Create a password: ")
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    if session.query(User).filter_by(username=username).first():
        print(colored("Username already exists. Please choose a different username.", 'red'))
    else:
        new_user = User(username=username, email=email, password=hashed_password.decode('utf-8'))
        session.add(new_user)
        session.commit()
        print(colored(f"Welcome, {username}! Your account has been created successfully.", 'green'))

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user = session.query(User).filter_by(username=username).first()

    if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        print(colored(f"Welcome back, {username}!", 'green'))
        return True
    else:
        print(colored("Login failed. Please check your credentials.", 'red'))
        return False

# Movie Search Functions
def search_movies():
    if not login_user():
        print(colored("You must log in to search for movies.", 'red'))
        return

    search_query = input("Enter a movie title or keyword to search: ")
    endpoint = '/search/movie'
    params = {
        'api_key': API_KEY,
        'query': search_query,
    }

    try:
        response = requests.get(BASE_URL + endpoint, params=params)
        response.raise_for_status()

        movies = response.json()['results']

        if not movies:
            print(colored("No movies found for the given query.", 'yellow'))
            return

        display_movie_search_results(movies)

    except requests.exceptions.RequestException as e:
        print(colored(f"Error fetching movie search results: {e}", 'red'))

def display_movie_search_results(movies):
    print(colored("Search Results:", 'cyan'))
    for i, movie in enumerate(movies, start=1):
        print(colored(f"{i}. {movie['title']} ({movie['release_date']})", 'yellow'))
        print(colored(f"Overview: {movie['overview']}", 'magenta'))
        print(colored(f"Vote Average: {movie['vote_average']}", 'green'))
        print("---")

# Rate Movie Function
def rate_movie():
    if not login_user():
        print(colored("You must log in to rate a movie.", 'red'))
        return

    movie_id = input("Enter the movie ID: ")
    rating = input("Rate the movie (1-10): ")

    # Check if the movie with the given ID exists in the database
    movie = session.query(Movie).filter_by(id=movie_id).first()

    if not movie:
        print(colored("Movie not found. Please enter a valid movie ID.", 'red'))
        return

    # Update the movie's rating in the database
    movie.vote_average = float(rating)
    session.commit()

    print(colored(f"Thank you for rating the movie! You gave it a rating of {rating} stars.", 'green'))

# View Favorites Function
def view_favorites():
    if not login_user():
        print(colored("You must log in to view your favorite movies.", 'red'))
        return

    favorite_movies = session.query(Movie).filter_by(recommended=True).all()

    if not favorite_movies:
        print(colored("You haven't added any favorite movies yet.", 'yellow'))
    else:
        print(colored("Your Favorite Movies:", 'cyan'))
        for i, movie in enumerate(favorite_movies, start=1):
            print(colored(f"{i}. {movie.title} ({movie.release_date})", 'yellow'))
            print(colored(f"Overview: {movie.overview}", 'magenta'))
            print(colored(f"Vote Average: {movie.vote_average}", 'green'))
            print("---")

# Add Recommendation Function
def add_recommendation():
    if not login_user():
        print(colored("You must log in to add a recommended movie.", 'red'))
        return

    movie_name = input("Enter the name of the recommended movie: ")

    # Implement your logic to add the movie as a recommendation here
    new_movie = Movie(title=movie_name, recommended=True)
    session.add(new_movie)
    session.commit()
    print(colored(f"{movie_name} has been added to your favorites.", 'green'))

# Get Recommendations Function
def get_recommendations():
    if not login_user():
        print(colored("You must log in to get movie recommendations.", 'red'))
        return

    recommended_movies = session.query(Movie).filter_by(recommended=True).all()

    if not recommended_movies:
        print(colored("No recommendations available at the moment.", 'yellow'))
    else:
        print(colored("Recommended Movies:", 'cyan'))
        for i, movie in enumerate(recommended_movies, start=1):
            print(colored(f"{i}. {movie.title}", 'yellow'))
            print("---")

# View Profile Function
def view_profile():
    if not login_user():
        print(colored("You must log in to view your profile.", 'red'))
        return

    username = input("Enter your username: ")
    user_info = session.query(User).filter_by(username=username).first()

    if user_info:
        print(colored("User Profile:", 'cyan'))
        print(colored(f"Username: {user_info.username}", 'yellow'))
        print(colored(f"Email: {user_info.email}", 'yellow'))
    else:
        print(colored("User not found.", 'red'))

# Recommend Best Movies Function
def recommend_best_movies():
    if not login_user():
        print(colored("You must log in to get movie recommendations.", 'red'))
        return

    best_movies = [
        "The Shawshank Redemption",
        "The Godfather",
        "The Dark Knight",
        "Pulp Fiction",
        "Schindler's List",
        "Forrest Gump",
        "Fight Club",
        "Inception",
        "The Matrix",
        "The Lord of the Rings: The Fellowship of the Ring",
        "The Silence of the Lambs",
    ]

    print(colored("Recommended Best Movies:", 'cyan'))
    for i, movie in enumerate(best_movies, start=1):
        print(colored(f"{i}. {movie}", 'yellow'))
        print("---")

# View Rated Movies Function
def view_rated_movies():
    if not login_user():
        print(colored("You must log in to view your rated movies.", 'red'))
        return

    rated_movies = session.query(Movie).filter(Movie.vote_average.isnot(None)).all()

    if not rated_movies:
        print(colored("You haven't rated any movies yet.", 'yellow'))
    else:
        print(colored("Your Rated Movies:", 'cyan'))
        for i, movie in enumerate(rated_movies, start=1):
            print(colored(f"{i}. {movie.title} ({movie.release_date})", 'yellow'))
            print(colored(f"Overview: {movie.overview}", 'magenta'))
            print(colored(f"Vote Average: {movie.vote_average}", 'green'))
            print("---")

# Delete Favorite Function
def delete_favorite():
    if not login_user():
        print(colored("You must log in to delete a movie from your favorites.", 'red'))
        return

    favorite_movies = session.query(Movie).filter_by(recommended=True).all()

    if not favorite_movies:
        print(colored("You haven't added any favorite movies yet.", 'yellow'))
        return

    print(colored("Your Favorite Movies:", 'cyan'))
    for i, movie in enumerate(favorite_movies, start=1):
        print(colored(f"{i}. {movie.title} ({movie.release_date})", 'yellow'))
        print(colored(f"Overview: {movie.overview}", 'magenta'))
        print(colored(f"Vote Average: {movie.vote_average}", 'green'))
        print("---")

    try:
        movie_index = int(input("Enter the number of the movie to delete: ")) - 1

        if 0 <= movie_index < len(favorite_movies):
            movie_to_delete = favorite_movies[movie_index]

            confirm = input(f"Are you sure you want to delete '{movie_to_delete.title}' from your favorites? (yes/no): ")

            if confirm.lower() == 'yes':
                session.delete(movie_to_delete)
                session.commit()
                print(colored(f"'{movie_to_delete.title}' has been deleted from your favorites.", 'green'))
            else:
                print(colored(f"'{movie_to_delete.title}' was not deleted.", 'yellow'))
        else:
            print(colored("Invalid movie number. No movie was deleted.", 'yellow'))

    except ValueError:
        print(colored("Invalid input. No movie was deleted.", 'yellow'))

# Main Function
def main():
    parser = argparse.ArgumentParser(description='Movie Recommendation CLI')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    register_parser = subparsers.add_parser('register', help='Register a new user')
    login_parser = subparsers.add_parser('login', help='Log in as an existing user')
    search_parser = subparsers.add_parser('search', help='Search for movies')
    rate_parser = subparsers.add_parser('rate', help='Rate a movie')
    view_favorites_parser = subparsers.add_parser('view-favorites', help='View user\'s favorite movies')
    add_recommendation_parser = subparsers.add_parser('add-recommendation', help='Add a recommended movie to favorites')
    get_recommendations_parser = subparsers.add_parser('get-recommendations', help='Get movie recommendations')
    view_profile_parser = subparsers.add_parser('view-profile', help='View user\'s profile')
    recommend_best_parser = subparsers.add_parser('recommend-best', help='Recommend the best movies')
    delete_parser = subparsers.add_parser('delete', help='Delete a movie from favorites')
    view_rated_parser = subparsers.add_parser('view-rated', help='View your rated movies')

    args = parser.parse_args()

    if args.command == 'register':
        register_user()
    elif args.command == 'login':
        login_user()
    elif args.command == 'search':
        search_movies()
    elif args.command == 'rate':
        rate_movie()
    elif args.command == 'view-favorites':
        view_favorites()
    elif args.command == 'add-recommendation':
        add_recommendation()
    elif args.command == 'get-recommendations':
        get_recommendations()
    elif args.command == 'view-profile':
        view_profile()
    elif args.command == 'recommend-best':
        recommend_best_movies()
    elif args.command == 'delete':
        delete_favorite()
    elif args.command == 'view-rated':
        view_rated_movies()

if __name__ == '__main__':
    main()
