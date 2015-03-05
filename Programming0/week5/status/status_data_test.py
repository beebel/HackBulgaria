import random

def generate_test(maxCountNames):
    names = ["Ivo", "Maria", "Genadi", "Rosti", "Marieta", "Boyan", "Katya",
         "Ivan", "Slavena", "Alex", "Georgi", "Radost", "Eli", "Bistra", "Pesho"]
    status = ["not_finalized", "finalized"]
    students = []
    studNames = []
    
    while len(studNames) < random.randint(1, maxCountNames):
        randName = random.choice(names)
        if randName not in studNames:
            studNames.append(randName)

    for name in studNames:
         oneStud = {}
         oneStud["name"] = name
         oneStud["status"] = random.choice(status)
         students.append(oneStud)

    return students    

def main():
    print(generate_test(10))

if __name__ == "__main__":
    main()
