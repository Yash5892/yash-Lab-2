def main():
    ## Complex Data Structure
    data_structure = {
        "full_name": "Yash Patel",
        "student_id": 10328272,
        "pizza_toppings": ["CORN", "JALAPENO", "OLIVES"],
        "movies": [
            {
                "title": "Salaar",
                "genre": "action"
            },
            {
                "title": "the godfather",
                "genre": "crime"
            }
        ]
    }

    ## Add Another Movie
    data_structure["movies"].append({
        "title": "inception",
        "genre": "sci-fi"
    })

    ## Print Student Name and ID
    print_student_info(data_structure)

    ## Add Pizza Toppings
    data_structure = add_pizza_toppings(data_structure, ("BACON", "PINEAPPLE"))

    ## Print Pizza Toppings (Before)
    print_pizza_toppings(data_structure)

    ## Print Pizza Toppings (After)
    print_pizza_toppings(data_structure)

    ## Print Movie Genres
    print_movie_genres(data_structure)

    ## Print Movie Titles
    print_movie_titles(data_structure["movies"])

def print_student_info(data):
    full_name = data["full_name"]
    student_id = data["student_id"]
    first_name = full_name.split()[0]
    print(f"My name is {full_name}, but you can call me Sir {first_name}.")
    print(f"My student ID is {student_id}.")

def add_pizza_toppings(data, toppings):
    data["pizza_toppings"].extend(toppings)
    data["pizza_toppings"].sort()
    data["pizza_toppings"] = [topping.lower() for topping in data["pizza_toppings"]]
    return data

def print_pizza_toppings(data):
    toppings = data["pizza_toppings"]
    print("My favourite pizza toppings are:")
    for topping in toppings:
        print(f"- {topping}")

def print_movie_genres(data):
    genres = [movie["genre"] for movie in data["movies"]]
    genre_list = ", ".join(genres)
    print(f"I like to watch {genre_list} movies.")

def print_movie_titles(movies):
    titles = [movie["title"].title() for movie in movies]
    title_list = ", ".join(titles)
    print(f"Some of my favourite movies are {title_list}!")

if __name__ == "__main__":
    main()
