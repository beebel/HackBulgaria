from status_data_test import generate_test

def status_count(students):
    result = {}
    result["finalized"] = []
    result["not_finalized"] = []

    for i in range(len(students)):
        if students[i]["status"] == "finalized":
            result["finalized"] = result["finalized"] + [students[i]["name"]]
        else:
            result["not_finalized"] = result["not_finalized"] + [students[i]["name"]]

    return result    

def main():
    testStudents = generate_test(10)
    print(testStudents)
    print()
    print(status_count(testStudents))

if __name__ == "__main__":
    main()
