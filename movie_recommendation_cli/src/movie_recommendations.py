import argparse
import requests
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from termcolor import colored  # Import termcolor for styled text
import bcrypt  # For secure password hashing

# Replace 'YOUR_API_KEY' with your actual TMDb API key
API_KEY = '3fd2be6f0c70a2a598f084ddfb75487c'

# Define the base URL for TMDb API
BASE_URL = 'https://api.themoviedb.org/3'

# SQLAlchemy setup
Base = declarative_base()
engine = create_engine('sqlite:///movie_db.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

# Define the Movie table
class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    overview = Column(String)
    release_date = Column(String)
    vote_average = Column(Float)
    recommended = Column(Boolean, default=False)  # Add a recommended column

# Define the User table
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String)
    password = Column(String)

def register_user():
    # Simulate user registration
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = input("Create a password: ")

    # Hash the user's password before storing it
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Check if the username already exists
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user:
        print(colored("Username already exists. Please choose a different username.", 'red'))
    else:
        # Create a new user
        new_user = User(username=username, email=email, password=hashed_password.decode('utf-8'))
        session.add(new_user)
        session.commit()
        print(colored(f"Welcome, {username}! Your account has been created successfully.", 'green'))

def login_user():
    # Simulate user login
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Retrieve the user's hashed password from the database
    user = session.query(User).filter_by(username=username).first()

    if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        print(colored(f"Welcome back, {username}!", 'green'))
        return True
    else:
        print(colored("Login failed. Please check your credentials.", 'red'))
        return False

def search_movies():
    if not login_user():
        print(colored("You must log in to search for movies.", 'red'))
        return

    # Simulate searching for movies
    search_query = input("Enter a movie title or keyword to search: ")

    # Define the endpoint for searching movies
    endpoint = '/search/movie'

    # Define the query parameters
    params = {
        'api_key': API_KEY,
        'query': search_query,
    }

    try:
        # Make an API request to search for movies
        response = requests.get(BASE_URL + endpoint, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors

        movies = response.json()['results']

        if not movies:
            print(colored("No movies found for the given query.", 'yellow'))
            return

        # Display movie search results
        print(colored("Search Results:", 'cyan'))
        for i, movie in enumerate(movies, start=1):
            print(colored(f"{i}. {movie['title']} ({movie['release_date']})", 'yellow'))
            print(colored(f"Overview: {movie['overview']}", 'magenta'))
            print(colored(f"Vote Average: {movie['vote_average']}", 'green'))
            print("---")

    except requests.exceptions.RequestException as e:
        print(colored(f"Error fetching movie search results: {e}", 'red'))

def rate_movie():
    if not login_user():
        print(colored("You must log in to rate a movie.", 'red'))
        return

    # Simulate rating a movie
    movie_id = input("Enter the movie ID: ")
    rating = input("Rate the movie (1-10): ")

    # Simulate rating confirmation (you can implement actual rating logic)
    print(colored(f"Thank you for rating the movie! You gave it a rating of {rating} stars.", 'green'))

def view_favorites():
    if not login_user():
        print(colored("You must log in to view your favorite movies.", 'red'))
        return

    # Simulate retrieving and displaying user's favorite movies
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

def add_recommendation():
    if not login_user():
        print(colored("You must log in to add a recommended movie.", 'red'))
        return

    # Simulate adding a recommended movie to favorites
    movie_name = input("Enter the name of the recommended movie: ")

    # Simulate adding the movie to favorites (you can implement actual logic)
    new_movie = Movie(title=movie_name, recommended=True)
    session.add(new_movie)
    session.commit()
    print(colored(f"{movie_name} has been added to your favorites.", 'green'))

def get_recommendations():
    if not login_user():
        print(colored("You must log in to get movie recommendations.", 'red'))
        return

    # Simulate getting movie recommendations
    recommended_movies = session.query(Movie).filter_by(recommended=True).all()

    if not recommended_movies:
        print(colored("No recommendations available at the moment.", 'yellow'))
    else:
        print(colored("Recommended Movies:", 'cyan'))
        for i, movie in enumerate(recommended_movies, start=1):
            print(colored(f"{i}. {movie.title}", 'yellow'))
            print("---")

def view_profile():
    if not login_user():
        print(colored("You must log in to view your profile.", 'red'))
        return

    # Simulate retrieving and displaying user's profile information
    username = input("Enter your username: ")
    user_info = session.query(User).filter_by(username=username).first()

    if user_info:
        print(colored("User Profile:", 'cyan'))
        print(colored(f"Username: {user_info.username}", 'yellow'))
        print(colored(f"Email: {user_info.email}", 'yellow'))
    else:
        print(colored("User not found.", 'red'))

def main():
    parser = argparse.ArgumentParser(description='Movie Recommendation CLI')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Create "register" subcommand
    register_parser = subparsers.add_parser('register', help='Register a new user')

    # Create "login" subcommand
    login_parser = subparsers.add_parser('login', help='Log in as an existing user')

    # Create "search" subcommand
    search_parser = subparsers.add_parser('search', help='Search for movies')

    # Create "rate" subcommand
    rate_parser = subparsers.add_parser('rate', help='Rate a movie')

    # Create "view-favorites" subcommand
    view_favorites_parser = subparsers.add_parser('view-favorites', help='View user\'s favorite movies')

    # Create "add-recommendation" subcommand
    add_recommendation_parser = subparsers.add_parser('add-recommendation', help='Add a recommended movie to favorites')

    # Create "get-recommendations" subcommand
    get_recommendations_parser = subparsers.add_parser('get-recommendations', help='Get movie recommendations')

    # Create "view-profile" subcommand
    view_profile_parser = subparsers.add_parser('view-profile', help='View user\'s profile')

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

if __name__ == '__main__':
    main()
