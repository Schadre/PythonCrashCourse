Movie_Database = {
    "The Addams Family" : {"genre": "comdey", "rating" : "10", "director": "Barry Sonnenfeld"}
    }

while True:
    try:
        print("Welcome to the Movie Database!")
        service_option = input("Please select your option: \n 1. Add a new movie \n 2. Delete an existing movie \n 3. Display all the movies \n 4. Exit \n")

        if service_option == "1":
            favorite = input("What is your favorite movie? ")
            genre = input("What is the genre of your favorite movie? ")
            rating = input("What is the rating of your favorite movie? ")
            director = input("Who is the director of your favorite movie? ")
            Movie_Database[favorite] = {
                            "genre" : genre,
                            "rating" : rating,
                            "director" : director
                        }
            print(f"Added {favorite} to our movie database!")
        
        elif service_option == "2":
            print("Alert: You will be removing a movie from our database!")
            movie = input("What movie would you like to remove? ")
            del Movie_Database[movie]
            print(f"{movie} has been removed!")
        
        elif service_option == "3":
            views = list(Movie_Database.keys())
            for view in views:
                print(view)

        elif service_option == "4":
            print("Goodbye")
            break

    except NameError:
        print("\nPlease try again.")
    except KeyError:
        print("\nThe movie does not exist in our database.")