def tsp_nearest_neighbor(distances):
    tour = [0]
    while len(tour) < len(distances):
        current_city = tour[-1]
        nearest_city = min((city for city in range(len(distances)) if city not in tour), key=lambda city: distances[current_city][city])
        tour.append(nearest_city)
    tour.append(0)
    return tour

def total_distance(tour, distances):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += distances[tour[i]][tour[i+1]]
    return total_dist

if __name__ == "__main__":
    distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    tour = tsp_nearest_neighbor(distances)
    print("Tour:", tour)
    print("Total Distance:", total_distance(tour, distances))