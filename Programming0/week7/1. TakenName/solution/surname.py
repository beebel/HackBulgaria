def taken_name(surname_husband, surname_wife):
    if surname_husband == surname_wife:
        return True
    elif surname_husband == surname_wife[:-1]:
        return True
    elif surname_husband[:-1] == surname_wife[:-1]:
        return True
    if "-" in surname_wife:
        wifeNames = surname_wife.split("-")
        for name in wifeNames:
            if surname_husband == name:
                return True
            elif surname_husband == name[:-1]:
                return True
            elif surname_husband[:-1] == name[:-1]:
                return True
    else:
        return False

def main():
    manName = input("Enter husband's surname: ")
    wifeName = input("Enter wife's surname: ")
    print(taken_name(manName, wifeName))

if __name__ == "__main__":
    main()
