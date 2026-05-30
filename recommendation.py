def recommend_places(user):

    recommendations = []

    for place, info in tourist_places.items():

        if info["type"] == user.interest:
            recommendations.append(place)

    return recommendations
