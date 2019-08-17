movie_file = open("top100moviesRT.txt", "r")
movie_list = movie_file.readlines()
movie_file.close()

for i in range(len(movie_list)):
    movie_list[i] = movie_list[i].strip()

print("The file 'top100moviesRT.txt' has been loaded.")
print("It contains the Top 100 movies of all time, according to Rotten Tomatoes.")

while True:
    user_movie = input("Please enter a movie title (or STOP): ")

    if user_movie.upper() == "STOP":
        break

    found = False

    for i in range(len(movie_list)):
        if user_movie.title() == movie_list[i]:
            print("That's the #", i + 1, "movie of all time.")
            found = True

    if not found:
        print("I couldn't find that movie in the list.")

        
