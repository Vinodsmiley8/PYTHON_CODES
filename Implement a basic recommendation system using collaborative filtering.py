# Simple user-based collaborative filtering
user_ratings = {
    'User1': {'Item1': 5, 'Item2': 3, 'Item3': 4},
    'User2': {'Item1': 4, 'Item3': 5, 'Item4': 2},
    'User3': {'Item2': 2, 'Item5': 4},
}

def recommend(user_ratings, target_user):
    recommendations = {}
    for user, ratings in user_ratings.items():
        if user != target_user:
            for item, rating in ratings.items():
                if item not in user_ratings[target_user]:
                    if item not in recommendations:
                        recommendations[item] = 0
                    recommendations[item] += rating

    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return sorted_recommendations

# Usage
target_user = 'User1'
result_recommendations = recommend(user_ratings, target_user)
print(f"Recommendations for {target_user}:", result_recommendations)