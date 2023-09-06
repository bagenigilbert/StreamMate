# Import necessary modules and classes
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from . import Base  # Import the Base class for model definitions

# Define a SQLAlchemy model for the 'movies' table
class Movie(Base):
    __tablename__ = 'movies'  # Define the table name in the database
    id = Column(Integer, primary_key=True, index=True)  # Primary key column
    title = Column(String, index=True, unique=True)  # Movie title, indexed and unique
    overview = Column(String)  # Movie plot or description
    release_date = Column(String)  # Movie release date
    vote_average = Column(Float)  # Average user rating for the movie
    poster_path = Column(String)  # Path to the movie's poster image
    ratings = relationship('UserRating', back_populates='movie')  # Define a relationship to 'user_ratings'

# Define a SQLAlchemy model for the 'user_ratings' table
class UserRating(Base):
    __tablename__ = 'user_ratings'  # Define the table name in the database
    id = Column(Integer, primary_key=True, index=True)  # Primary key column
    user_id = Column(Integer, ForeignKey('users.id'))  # Foreign key referencing 'users' table
    movie_id = Column(Integer, ForeignKey('movies.id'))  # Foreign key referencing 'movies' table
    rating = Column(Integer)  # User's rating for a movie
    user = relationship('User', back_populates='ratings')  # Define relationships to 'users' and 'movies'

# Define a SQLAlchemy model for the 'users' table
class User(Base):
    __tablename__ = 'users'  # Define the table name in the database
    id = Column(Integer, primary_key=True, index=True)  # Primary key column
    username = Column(String, index=True, unique=True)  # User's username, indexed and unique
    email = Column(String, unique=True, index=True)  # User's email address, unique and indexed
    hashed_password = Column(String)  # Hashed user password for security
    ratings = relationship('UserRating', back_populates='user')  # Define a relationship to 'user_ratings'
