def hello_func(greeting, name="World") -> str:
    return '{}, {}!'.format(greeting, name)

hello_func("Hello", "Srishti")
# Output: Hello, Srishti!

hello_func("Hi")
# Output: Hi, World!



def student_info(*args, **kwargs):
    # `*args` collects extra positional arguments into a tuple named `args`.
    # `**kwargs` collects extra keyword arguments into a dict named `kwargs`.
    # Example usage below:
    # student_info("Srishti", 25, course="Python", grade="A")
    # -> args == ("Srishti", 25)
    # -> kwargs == {"course": "Python", "grade": "A"}
    print(args)
    print(kwargs)

student_info("Srishti", 25, course="Python", grade="A")
# Output:
# ('Srishti', 25)
# {'course': 'Python', 'grade': 'A'}

courses = ["Python", "Java", "C++"]
student = {"name": "Srishti", "age": 25}

student_info(courses, student)
# Output:
# (['Python', 'Java', 'C++'], {'name': 'Srishti', 'age': 25})
# Here, `courses` is passed as a single positional argument (a list), and `student` is passed as a single positional argument (a dict).

# To unpack the list and dict into separate arguments, we can use `*` and `**` respectively:
student_info(*courses, **student)
# Output:
# ('Python', 'Java', 'C++')
# {'name': 'Srishti', 'age': 25}