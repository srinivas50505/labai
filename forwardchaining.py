def forwardchain(rules,intial_Facts):
    facts=intial_Facts.copy()
    while True:
        new_added_fact=False
        for rule in rules:
            result=evaluate(rule,facts)
            if result and result not in facts:
                facts.append(result)
                new_added_fact=True
        if not new_added_fact:
                break
    return facts
def evaluate(rule,facts):
    conditions,result =rule
    if all(condition in facts for condition in conditions):
        return result
    return None
        
rules = [
    (["fever", "cough"], "flu"),
    (["fever", "sorethroat"], "flu"),
    (["headache", "fatigue"], "migraine"),
    (["runnynose"], "common cold"),
    (["sneezing"], "allergies")
]

initial_facts =  ["fever","cough", "throat"]
conclusions = forwardchain(rules, initial_facts)
print(" The Result is : ",conclusions[-1])
