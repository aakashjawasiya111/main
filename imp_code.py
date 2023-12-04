MENU = "\nEnter 'a' to add a movie, 'l' to see your movies , 'f to find a movie by tital, or 'q' to quit:"
movies = []


def add_movie():
    title = input("Enter the movie tital: ")
    actor = input("Enter actor name: ")
    year = input("Enter the movie realese year: ")

    movies.append({
        'title' : title,
        'actor' : actor,
        'year' : year
    })



def show_movies():
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    print(f"Tital: {movie['title']}")
    print(f"Actor Name: {movie['actor']}")
    print(f"Realese Year: {movie['year']}")


def find_movie():
    search_title = input("Enter movie title you're loocking for: ")

    for movie in movies:
        if movie["title"] == search_title:
            print_movie(movie)


user_option ={
    "a" : add_movie,
    "l" :  show_movies,
    "f" : find_movie
}



# def menu():
#     selection = input(MENU)
#     while selection != 'q':
#         if selection == 'a':
#             add_movie()
#         elif selection == 'l':
#             show_movies()
#         elif selection == 'f':
#             find_movie()
#         else:
#             print('Unkown commond, Please try again: ')

#         selection = input(MENU)

# menu()


def menu():
    selection = input(MENU)
    while selection != 'q':
        if selection in user_option:
            selection_function = user_option[selection]
            selection_function()
        else:
            print('Unkown commond, Please try again: ')

        selection = input(MENU)

menu()
