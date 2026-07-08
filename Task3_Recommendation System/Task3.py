movies = {
    "action": ["Avengers", "John Wick", "Mad Max"],
    "comedy": ["Hangover", "Superbad", "Step Brothers"],
    "romance": ["Titanic", "Notebook", "La La Land"]
}

print("Choose genre: action / comedy / romance")
choice = input("Enter genre: ").lower()

if choice in movies:
    print("Recommended movies:")
    for movie in movies[choice]:
        print("-", movie)
else:
    print("Genre not found")
