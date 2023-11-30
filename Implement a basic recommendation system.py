# Implement a basic recommendation system
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Sample data (user-item matrix)
user_item_matrix = np.array([
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 1, 1, 0]
])
# Calculate cosine similarity
similarity_matrix = cosine_similarity(user_item_matrix, user_item_matrix)

# Recommend items for a user
user_id = 0
user_vector = user_item_matrix[user_id]
recommendations = np.dot(similarity_matrix, user_vector)
sorted_indices = np.argsort(recommendations)[::-1]

print("Recommendations for user", user_id, ":")
for idx in sorted_indices:
    if user_vector[idx] == 0:  # Not already rated
        print("Item", idx, ":", recommendations[idx])