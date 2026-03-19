def check_language():
    language = "Java"

    if language == "Python":
        print("Language is Python!")
    elif language == "Java":
        # Language is Java!
        print("Language is Java!")
    else:
        print("Language is not Python or Java!")

def check_boolean():
    is_raining = True
    condition = {}
    string = "Hello"

    if condition:
        print("Condition is true.")
    else:
        # Condition is false.
        print("Condition is false.")

    if string:
        # String is not empty.
        print("String is not empty.")
    else:
        print("String is empty.")

    if is_raining:
        # It's raining! Don't forget your umbrella.
        print("It's raining! Don't forget your umbrella.")
    else:
        print("It's not raining! Enjoy your day.")

def check_membership():
    fruits = ["apple", "banana", "cherry"]

    if "banana" in fruits:
        # Banana is in the list of fruits.
        print("Banana is in the list of fruits.")
    else:
        print("Banana is not in the list of fruits.")

    if "grape" not in fruits:
        # Grape is not in the list of fruits.
        print("Grape is not in the list of fruits.")
    else:
        print("Grape is in the list of fruits.")

def check_identity_and_membership():
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a

    print(id(a))  # Memory address of a
    print(id(b))  # Memory address of b
    print(id(c))  # Memory address of c

    if a == b:
        # a and b have the same content.
        print("a and b have the same content.")
    else:
        print("a and b have different content.")

    if a is b:
        print("a and b refer to the same object.")
    else:
        # a and b refer to different objects.
        print("a and b refer to different objects.")

def check_logical_operators():
    x = 5
    y = 10

    if x > 0 and y > 0:
        # Both x and y are positive.
        print("Both x and y are positive.")
    else:
        print("Either x or y is not positive.")

    if x > 0 or y > 0:
        # At least one of x or y is positive.
        print("At least one of x or y is positive.")
    else:
        print("Neither x nor y is positive.")

    if not (x < 0):
        # x is not negative.
        print("x is not negative.")
    else:
        print("x is negative.")

def check_comparison_operators():
    a = 10
    b = 20

    if a == b:
        print("a is equal to b.")
    else:
        # a is not equal to b.
        print("a is not equal to b.")

    if a != b:
        # a is not equal to b.
        print("a is not equal to b.")
    else:
        print("a is equal to b.")

    if a < b:
        # a is less than b.
        print("a is less than b.")
    else:
        print("a is not less than b.")

    if a > b:
        print("a is greater than b.")
    else:
        # a is not greater than b.
        print("a is not greater than b.")

    if a <= b:
        # a is less than or equal to b.
        print("a is less than or equal to b.")
    else:
        print("a is greater than b.")

    if a >= b:
        print("a is greater than or equal to b.")
    else:
        # a is less than b.
        print("a is less than b.")

# If you run this file directly (python conditionals.py),
# the code below will run. If you import this file from
# another module, the code below will NOT run.
if __name__ == "__main__":
    check_language()
    check_boolean()
    check_membership()
    check_identity_and_membership()
    check_logical_operators()
    check_comparison_operators()