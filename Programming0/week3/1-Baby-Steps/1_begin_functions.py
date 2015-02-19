students = ["Rado", "Ivo", "Maria", "Nina"]
grades = [3, 4.5, 5.5, 6]

def square(num):
    sqrNum = num ** 2
    return sqrNum

def factorial(num):
    facNum = 1
    i = 1
    if num == 0:
        return facNum
    else:
        while i <= num:
            facNum = facNum * i
            i = i + 1
        return facNum    

def count_elements(items):
    sumElem = 0
    for e in items:
        sumElem = sumElem + 1
    return sumElem

def member(x, xs):
    i = 0
    result = False
    while i < len(xs):
        if xs[i] == x:
            result = True
            break
        i = i + 1
    return result

def grades_that_pass(names, marks, filter):
    i = 0
    passed = []
    while i < len(marks):
        if marks[i] >= filter:
            passed.append(names[i])
        i = i + 1

    return passed

print("square(2) = %s" % square(2))
print("square(5) = %s" % square(5))
print("factorial(5) = %s" % factorial(5))
print("factorial(0) = %s" % factorial(0))
print("factorial(6) = %s" % factorial(6))
print("count_elements([]) = %s" % count_elements([]))
print("count_elements([1, 2, 3]) = %s" % count_elements([1, 2, 3]))
print("member(1, [1,2,3])")
print(member(1, [1,2,3]))
print("member(\"Python\", [\"Django\", \"Rails\"])")
print(member("Python", ["Django", "Rails"]))
print("students = %s" % students)
print("grades = %s" % grades)
print("grades_that_pass(students, grades, 4.0)")
print(grades_that_pass(students, grades, 4.0))
