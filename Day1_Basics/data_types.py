def string_operations():
    message = "Hello Srishti"

    # Hello Srishti
    print(message)
    # 13
    print(len(message))
    # H
    print(message[0])
    # i
    print(message[-1])
    # Hello
    print(message[0:5])
    # Srishti
    print(message[6:])
    # HELLO SRISHTI
    print(message.upper())
    # hello srishti
    print(message.lower())

    message = "{}, welcome to Python programming!".format(message)
    # Hello Srishti, welcome to Python programming!
    print(message)

def number_operations():
    a = 10
    b = 3

    # 13
    print(a + b)
    # 7
    print(a - b)
    # 30
    print(a * b)
    # 3.3333333333333335
    print(a / b)
    # 3
    print(a // b)
    # 1
    print(a % b)
    # 1000
    print(a ** b)

    num = 3.14159
    # 3.14
    print(round(num, 2))
    # <class 'float'>
    print(type(num))
    # True
    print(isinstance(num, float))
    # 3
    print(int(num))

def array_operations():
    numbers = [1, 2, 3, 4, 5]
    Nums = [4, 5, 1, 3, 2]

    # [1, 2, 3, 4, 5]
    print(numbers)
    # 5
    print(len(numbers))
    # 1
    print(numbers[0])
    # 5
    print(numbers[-1])
    # [1, 2, 3]
    print(numbers[0:3])
    # [1, 3]
    print(numbers[0:4:2])
    # [4, 5]
    print(numbers[3:])
    numbers.append(6)
    # [1, 2, 3, 4, 5, 6]
    print(numbers)
    numbers.remove(2)
    # [1, 3, 4, 5, 6]
    print(numbers)
    s_li = sorted(Nums)
    # [1, 2, 3, 4, 5]
    print(s_li)
    Nums.sort()
    # [1, 2, 3, 4, 5]
    print(Nums)
    Nums.sort(reverse=True)
    # [5, 4, 3, 2, 1]
    print(Nums)
    sorted_nums = Nums.sort(reverse=True)
    # None
    print(sorted_nums)



def tuple_operations():
    coordinates = (10, 20)

    # (10, 20)
    print(coordinates)
    # 2
    print(len(coordinates))
    # 10
    print(coordinates[0])
    # 20
    print(coordinates[-1])
    # (10, 20)
    print(coordinates[0:2])
    # Tuples are immutable, so we cannot modify them
    # coordinates[0] = 15  # This will raise an error

def set_operations():
    unique_numbers = {1, 2, 3, 4, 5}

    # {1, 2, 3, 4, 5}
    print(unique_numbers)
    # 5
    print(len(unique_numbers))
    unique_numbers.add(6)
    # {1, 2, 3, 4, 5, 6}
    print(unique_numbers)
    unique_numbers.remove(3)
    # {1, 2, 4, 5, 6}
    print(unique_numbers)

def dictionary_operations():
    person = {
        "name": "Srishti",
        "age": 29,
        "city": "Udaipur"
    }

    # {'name': 'Srishti', 'age': 29, 'city': 'Udaipur'}
    print(person)
    # 3
    print(len(person))
    # Srishti
    print(person["name"])
    # 29
    print(person.get("age"))
    person["age"] = 26
    # {'name': 'Srishti', 'age': 26, 'city': 'Udaipur'}
    print(person)
    del person["city"]
    # {'name': 'Srishti', 'age': 26}
    print(person)

if __name__ == "__main__":
    string_operations()
    number_operations()
    array_operations()
    tuple_operations()
    set_operations()
    dictionary_operations()