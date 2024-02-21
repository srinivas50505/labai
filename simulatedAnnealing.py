import random,math

def acceptance_probability(old, new, t): return math.exp((old - new) / t)
def generate_neighbor(sol): a,b=random.sample(range(len(sol)),2);sol[a],sol[b]=sol[b],sol[a];return sol

def simulated_annealing(sol, cost_func, max_iter, t, cooling_rate):
    current = best = sol
    for _ in range(max_iter):
        new = generate_neighbor(current)
        old, new_cost = cost_func(current), cost_func(new)
        if acceptance_probability(old, new_cost, t) > random.random(): current = new
        if new_cost < cost_func(best): best = new
        t *= cooling_rate
    return best

initial, max_iter, t, cooling_rate = [1, 2, 3, 4, 5], 1000, 1.0, 0.95
best_solution = simulated_annealing(initial, sum, max_iter, t, cooling_rate)
print("Best solution:", best_solution)
print("Cost:", sum(best_solution))