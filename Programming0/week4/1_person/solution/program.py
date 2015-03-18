from datetime import date

firstName = input("Enter first name: ")
secondName = input("Enter second name: ")
thirdName = input("Enter third name: ")
birthYear = input("Enter birth year: ")
birthYear = int(birthYear)

user = {'fist_name':firstName, 'second_name':secondName, 'third_name':thirdName,
'birth_year':birthYear, 'current_age':(int((date.today().year)) - birthYear)}

print(user)

