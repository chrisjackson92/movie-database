#!/usr/bin/env/python3

import db
from objects import Movie

def display_title():
    print("The Movie List program")
    print()    
    display_menu()

def display_menu():
    print("COMMAND MENU")
    print("cat  - View movies by category")
    print("year - View movies by year")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("id   - Get movie by ID")
    print("min  - View movie by minutes equal or less than value")
    print("exit - Exit program")
    print()    

def display_categories():
    print("CATEGORIES")
    categories = db.get_categories()    
    for category in categories:
        print(str(category.id) + ". " + category.name)
    print()

def display_movies(movies, title_term):
    print("MOVIES - " + title_term)
    line_format = "{:3s} {:37s} {:6s} {:5s} {:10s}"
    print(line_format.format("ID", "Name", "Year", "Mins", "Category"))
    print("-" * 64)
    for movie in movies:
        print(line_format.format(str(movie.id), movie.name,
                                 str(movie.year), str(movie.minutes),
                                 movie.category.name))
    print()    

def display_movies_by_category():
    category_id = int(input("Category ID: "))
    category = db.get_category(category_id)
    if category == None:
        print("There is no category with that ID.\n")
    else:
        print()
        movies = db.get_movies_by_category(category_id)
        display_movies(movies, category.name.upper())
    
def display_movies_by_year():
    year = int(input("Year: "))
    print()
    movies = db.get_movies_by_year(year)
    display_movies(movies, str(year))

def add_movie():
    name        = input("Name: ")
    year        = int(input("Year: "))
    minutes     = int(input("Minutes: "))
    category_id = int(input("Category ID: "))
    
    category = db.get_category(category_id)
    if category == None:
        print("There is no category with that ID. Movie NOT added.\n")
    else:        
        movie = Movie(name=name, year=year, minutes=minutes,
                      category=category)
        db.add_movie(movie)    
        print(name + " was added to database.\n")

def delete_movie():
    movie_id = int(input("Movie ID: "))
    movies = db.get_movie_by_id(movie_id)
    if movies == None:
        print("There is no movie with that ID.\n")
    else:
        print()
        display_movies(movies, str(id))
    confirmation = input("Are you sure you want to delete this mmovie? (Enter y for yes n for no: ").lower()
    if confirmation == "y":
        db.delete_movie(movie_id)
        print("Movie ID " + str(movie_id) + " was deleted from database.\n")
    elif confirmation == "n":
        print("Delete cancelled.")
    else:
        print("Please make a valid choice")

def get_movie_by_id():
    id = int(input("Movie ID: "))
    movies = db.get_movie_by_id(id)
    if movies == None:
        print("There is no movie with that ID.\n")
    else:
        print()
        display_movies(movies, str(id))

def display_movie_by_minutes():
    minutes = int(input("Minutes: "))
    movies = db.get_movies_by_minutes(minutes)
    if movies == None:
        print("There are no movies with minutes equal or less than the value entered.\n")
    else:
        print()
        display_movies(movies, str(minutes))

        
def main():
    db.connect()
    display_title()
    display_categories()
    while True:        
        command = input("Command: ")
        if command == "cat":
            display_movies_by_category()
        elif command == "year":
            display_movies_by_year()
        elif command == "add":
            add_movie()
        elif command == "del":
            delete_movie()
        elif command == "id":
            get_movie_by_id()
        elif command == "min":
            display_movie_by_minutes()
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
            display_menu()
    db.close()
    print("Bye!")

if __name__ == "__main__":
    main()
