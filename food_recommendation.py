def recommend_food(user):

    food_list = []

    for restaurant, info in restaurants.items():

        if user.vegetarian:

            if info["veg"]:
                food_list.append(restaurant)

        else:
            food_list.append(restaurant)

    return food_list
