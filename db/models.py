#import necessary modules and classes

from sqlalchemy import Column, Integer, String,Float,ForeignKey
from sqlalchemy.orm import relationship
from . import Base # Import the Base class for model definitions

# Define a SQLAlchemy model for the 'movies' table

class Movie(Base):

    __tablename__ = 'movies'  # Define the table name in the database
    

