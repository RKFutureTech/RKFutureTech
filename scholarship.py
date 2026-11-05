# Scholarship Eligibility Checker
# BCA Python Project

def check_eligibility():
    print("=" * 50)
    print("       SCHOLARSHIP ELIGIBILITY CHECKER")
    print("=" * 50)

    # Taking student information
    name = input("Enter student name: ")

    age = int(input("Enter age: "))

    percentage = float(input("Enter academic percentage: "))

    income = float(input("Enter annual family income: "))

    category = input("Enter category (General/OBC/SC/ST): ").strip().upper()

    print("\nChecking eligibility...")

    # Scholarship eligibility conditions
    if (
        age >= 18
        and percentage >= 60
        and income <= 300000
    ):
        print("\n" + "=" * 50)
        print("             SCHOLARSHIP RESULT")
        print("=" * 50)

        print("Student Name :", name)
        print("Category     :", category)
        print("Percentage   :", percentage)
        print("Income       :", income)

        print("\nStatus       : ELIGIBLE")
        print("Congratulations! You are eligible for the scholarship.")

        print("=" * 50)

    else:
        print("\n" + "=" * 50)
        print("             SCHOLARSHIP RESULT")
        print("=" * 50)

        print("Student Name :", name)
        print("Category     :", category)
        print("Percentage   :", percentage)
        print("Income       :", income)

        print("\nStatus       : NOT ELIGIBLE")
        print("Sorry! You do not meet all the scholarship conditions.")

        print("=" * 50)


# Run the program
check_eligibility()
input("\nPress Enter to exit...")