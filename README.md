# Movie Recommendation CLI
### Author: Gilbert Bageni (gilbertwilber0@gmail.com)

The Movie Recommendation CLI is a command-line interface application designed to bring the magic of movies right to your terminal. It allows you to explore, rate, and manage your favorite movies, as well as receive personalized movie recommendations. Whether you're a film enthusiast or just looking for your next great watch, this CLI tool has got you covered.

## Movie Recommendation CLI Demo

Table of Contents
Features
Getting Started
Prerequisites
Installation
Usage
User Registration
User Login
Searching for Movies
Rating Movies
Viewing Your Favorites
Adding Recommendations
Getting Movie Recommendations
Viewing Your Profile
Discovering the Best Movies
Viewing Your Rated Movies
Deleting Favorites
Contributing
License
Acknowledgments

## Features
 User Registration and Authentication: Register a new user account or log in as an existing user to personalize your movie experience.

Movie Search: Explore a vast library of movies by searching for titles or keywords.

Movie Rating: Rate movies on a scale of 1 to 10, helping you keep track of your favorites.

Favorites Management: View your favorite movies and easily manage your collection.

Personalized Recommendations: Receive movie recommendations tailored to your preferences.

User Profile: Access and view your user profile information.

Discover the Best Movies: Get recommendations for the best movies of all time.

## Getting Started
### Prerequisites
Before you dive into the world of movies, make sure you have the following prerequisites met:

Python 3.x: The CLI is powered by Python, so you'll need a Python 3.x installation.

Required Python Libraries: Ensure that you have the necessary Python libraries installed. You can install them by running the following command:

pip install -r requirements.txt
## Installation
To get up and running with the Movie Recommendation CLI, follow these simple installation steps:

Clone the Repository: Begin by cloning this repository to your local machine:

git clone https://github.com/yourusername/movie-recommendation-cli.git
Navigate to the Project Directory: Move into the project directory:

cd movie-recommendation-cli
Create the Database: Run the following command to create the SQLite database:

python create_db.py
Now you're all set and ready to start exploring movies!

## Usage
The Movie Recommendation CLI offers a wide range of commands to enhance your movie experience. Below are some of the key functionalities explained in detail:

## User Registration
To create a new user account, use the following command:

python movie_recommendation.py register
Follow the prompts to enter your username, email, and password. Once registered, you'll be ready to access personalized features.

## User Login
Log in as an existing user using the following command:


python movie_recommendation.py login
Provide your username and password when prompted. This will grant you access to your saved preferences.

## Searching for Movies
Search for movies by title or keyword with:

python movie_recommendation.py search
Enter the movie title or keyword you're interested in, and watch the results appear.

## Rating Movies
Rate a movie on a scale of 1 to 10 by running:

python movie_recommendation.py rate
You'll be asked to input the movie ID and your rating. Share your opinions and contribute to the movie community!

## Viewing Your Favorites
To view your list of favorite movies, use:


python movie_recommendation.py 
## view-favorites
See which movies you've marked as your favorites and revisit their details.

Adding Recommendations
Add a recommended movie to your favorites with:


python movie_recommendation.py add-recommendation
Enter the name of the movie you want to recommend, and it will be added to your collection.

## Getting Movie Recommendations
Receive personalized movie recommendations with:


python movie_recommendation.py get-recommendations
Explore a list of movies curated just for you based on your preferences.

## Viewing Your Profile
Access your user profile information by running:


python movie_recommendation.py view-profile
Retrieve details about your username and email to keep your profile up-to-date.

## Discovering the Best Movies
Find recommendations for the best movies of all time with:


python movie_recommendation.py recommend-best
Explore a curated list of cinematic masterpieces that you won't want to miss.

## Viewing Your Rated Movies
See a list of movies you've rated with:


python movie_recommendation.py view-rated
Review your past ratings and the movies you've evaluated.

## Deleting Favorites
Remove a movie from your favorites using:

python movie_recommendation.py delete
Choose the movie you'd like to delete from your collection and confirm the action.

## Contributing
Contributions to this project are always welcome! If you have ideas for improvements or new features, feel free to contribute by following these steps:

Fork the Repository: Create your own fork of this repository.

Create a New Branch: Develop your feature or bug fix in a new branch.

Make Changes: Make your changes and commit them to your branch.

Push Your Changes: Push your changes to your forked repository.

Open a Pull Request: Create a pull request, explaining your changes and why they should be merged.

## License
This project is licensed under the MIT License. For details, see the LICENSE file.

## Acknowledgments
This project was created with a passion for movies and coding.
Special thanks to [gilbert bageni] for inspiration or assistance in creating this CLI tool.
Enjoy your movie journey with the Movie Recommendation CLI! If you have any questions or need further assistance, feel free to contact the author, Gilbert Bageni, at gilbertwilber0@gmail.com.




