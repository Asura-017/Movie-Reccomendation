import random

# Movie data stored in a dictionary
movies = {
    "Action": ["Mad Max: Fury Road", "John Wick", "Terminator", "Gladiator"],
    "Comedy": ["Superbad", "Step Brothers", "The Hangover", "Dumb and Dumber"],
    "Drama": ["Forrest Gump", "The Shawshank Redemption", "Fight Club", "The Godfather"],
    "Sci-Fi": ["Inception", "The Matrix", "Interstellar", "Blade Runner 2049"]
}

def recommend_movies():
    """Ask user for a genre and recommend 3 random movies"""
    while True:
        genre = input("\nEnter a movie genre (Action, Comedy, Drama, Sci-Fi) or 'quit' to exit: ").strip()
        if genre.lower() == "quit":
            print("Goodbye! Enjoy your movies!")
            break  # Exit the loop

        elif genre in movies:
            recommendations = random.sample(movies[genre], 3)
            print(f"\nRecommended {genre} movies: {', '.join(recommendations)}")
        
        else:
            print("Sorry, we don’t have recommendations for that genre. Try again!")

# Run the recommendation system
if __name__ == "__main__":
    recommend_movies()
