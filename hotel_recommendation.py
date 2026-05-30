def recommend_hotel(user):

    if user.budget < 20000:
        return "Budget Inn"

    elif user.budget < 50000:
        return "Comfort Stay"

    else:
        return "Luxury Palace"
