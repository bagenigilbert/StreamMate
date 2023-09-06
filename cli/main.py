# Import necessary libraries and modules
import click
import requests # For making HTTP requests
from STREAMMATE.db import Session, User, Movie, UserRating  # Import SQLAlchemy models

#define the CLI command group
@click.group()
def cli():
    pass

# Register command for user registration
@click.command()
@click.option('--username', prompt=True, help='Your username')
@click.option('--email', prompt=True, help='Your email')
@click.password_option(help='Your password')
def register(username, email, password):
        # Create an SQLAlchemy session

