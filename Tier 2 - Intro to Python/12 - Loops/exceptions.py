while True:
    try:
        age = int(input("AGE: "))
        income = int(input("INCOME: "))
        risk = income/age
        print("Age: ", age)
        print("Income: ", income)
        print("Risk: ", risk)
    except ValueError:
        print("INVALID!")
    except ZeroDivisionError:
        print("AGE CANNOT BE ZERO")