"""
 Challenge:  Personal Movie Tracker with JSON

Create a Python CLI tool that lets users maintain their own personal movie database, like a mini IMDb.

Your program should:
1. Store all movie data in a `movies.json` file.
2. Each movie should have:
   - Title
   - Genre
   - Rating (out of 10)
3. Allow the user to:
   - Add a movie
   - View all movies
   - Search movies by title or genre
   - Exit the app

Bonus:
- Prevent duplicate titles from being added
- Format output in a clean table
- Use JSON for reading/writing structured data
- use [
    {
        'title' : 'movie_name',
        'genre' : 'movie_genre',
        'rating' : 'movie_rating'
    },{},{}
]
"""
import os
import json

# Constants
FILE_NAME = "movies.json"

def load_movies(file_name):
    """Load movies from JSON file"""
    if not os.path.exists(file_name):
        return []
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_movies(file_name, movies):
    """Save movies to JSON file"""
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(movies, file, indent=4)

def show_menu():
    """Show menu options"""
    print("Menu:")
    print("1. Add a movie")
    print("2. View all movies")
    print("3. Search for a movie")
    print("4. Exit")
    print()

def add_movie(file_name, movies):
    """Add a new movie"""
    title = input("Enter movie title: ")

    if any(movie['title'] == title for movie in movies):
        print("Movie already exists.")
        return 

    genre = input("Enter movie genre: ")
    while True:
        try:
            rating = float(input("Enter the movie rating (out of 10): "))
            if 0 <= rating <= 10:
                break
            else:
                print("Invalid rating. Please enter a number between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    movies.append({
        'title': title,
        'genre': genre,
        'rating': rating
    })

    save_movies(file_name, movies)
    print("Movie added successfully")

def search_movie(movies, search_term):
    """Search for a movie by title or genre"""
    results = [movie for movie in movies if movie['title'].lower() == search_term.lower() or movie['genre'].lower() == search_term.lower()]
    if results:
        for movie in results:
            print(f"Title: {movie['title']}\nGenre: {movie['genre']}\nRating: {movie['rating']}\n")
    else:
        print("Movie not found.")

def show_movies(movies):
    """Show all movies"""
    if not movies:
        print("No movies found.")
        return
    print(f"Movies found: {len(movies)}")
    print("-" * 50)
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie['title']}")
        print(f"  Genre: {movie['genre']}")
        print(f"  Rating: {movie['rating']}/10")
        print("-" * 50)

if __name__ == "__main__":
    # Get the current working directory
    cwd = os.getcwd()

    # Create the file path for the movies.json file
    file_path = os.path.join(cwd, FILE_NAME)

    movies = load_movies(file_path)

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_movie(file_path, movies)
        elif choice == "2":
            show_movies(movies)
        elif choice == "3":
            search_term = input("Enter search term: ")
            search_movie(movies, search_term)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")