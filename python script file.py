def main():
    return
if __name__=='__main__':
    main()
    ## Complex Data Structure
    data_structure = {
        "full_name": "John Doe",
        "student_id": 12345,
        "pizza_toppings": ["PEPPERONI", "MUSHROOMS", "OLIVES"],
        "movies": [
            {
                "title": "the shawshank redemption",
                "genre": "drama"
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

    # Print the updated data structure
    print(data_structure)

if __name__ == "__main__":
    main()