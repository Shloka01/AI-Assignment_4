def calculate_cost(
        places,
        hotel,
        restaurant):

    place_cost = 0

    for p in places:
        place_cost += tourist_places[p]["cost"]

    hotel_cost = hotels[hotel]["price"] * 3

    food_cost = restaurants[restaurant]["cost"] * 3

    total = (
        place_cost
        + hotel_cost
        + food_cost
    )

    return total
