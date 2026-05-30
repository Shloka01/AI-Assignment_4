def generate_itinerary(user):

    places = recommend_places(user)

    hotel = recommend_hotel(user)

    food = recommend_food(user)

    print("------ TRAVEL PLAN ------")

    print("Traveller:", user.name)

    print("Hotel:", hotel)

    print("\nPlaces:")

    for p in places:
        print("-", p)

    print("\nFood:")

    for f in food:
        print("-", f)

    total = calculate_cost(
        places,
        hotel,
        food[0]
    )

    print("\nEstimated Cost:", total)
