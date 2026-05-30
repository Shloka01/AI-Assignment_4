def expert_rules(user):

    advice = []

    if user.interest == "Beach":
        advice.append(
            "Recommend coastal destinations"
        )

    if user.budget < 20000:
        advice.append(
            "Use budget hotels"
        )

    if user.vegetarian:
        advice.append(
            "Recommend vegetarian restaurants"
        )

    return advice
