import math


def euclidean_distance(point):
  # Calculate the Euclidean distance from the origin (0,0)
  return math.sqrt(point[0]**2 + point[1]**2)


def furthest_points(points):
  # Sort points based on Euclidean distance in descending order
  sorted_points = sorted(points, key=euclidean_distance, reverse=True)

  # Return the furthest and second furthest points
  furthest_point = sorted_points[0]
  second_furthest_point = sorted_points[1]

  return furthest_point, second_furthest_point


# Example usage:
points = [(1, 2), (3, 4), (-1, 0), (5, 6)]
furthest, second_furthest = furthest_points(points)

print("Furthest Point:", furthest)
print("Second Furthest Point:", second_furthest)
