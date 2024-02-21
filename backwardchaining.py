def backward_chain(rules, goal, known_facts):
    if goal in known_facts:
        return True
    for result, conditions in rules:
        if result == goal:
            for  condition in conditions:
                if backward_chain(rules,condition,known_facts):
                    return False
            return True
                
    return False

rules = [
    ("flu", ["fever", "cough", "sorethroat"]),
    ("migraine", ["headache", "fatigue"]),
    ("common cold", ["runnynose"]),
    ("allergies", ["sneezing"])
]
known_facts =  ["fever","cough", "throat"]
goal = "flu"

if backward_chain(rules, goal ,known_facts):
    print(f"Goal '{goal}' is consistent with the given facts.")
else:
    print(f"Goal '{goal}' is not consistent with the given facts.")
