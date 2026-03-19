nums = [1, 2, 3, 4, 5]

for num in nums:
    # 1
    # 2
    # Found the number 3, breaking the loop.
    if num == 3:
        print("Found the number 3, breaking the loop.")
        break
    print(num)

    # 1
    # 2
    # Found the number 3, Continuing the loop.
    # 4
    # 5
    if num == 3:
        print("Found the number 3, Continuing the loop.")
        continue
    print(num)

for i in range(5):
    # 0
    # 1
    # 2
    # 3
    # 4
    print(i)

for i in range(1, 6):
    # 1
    # 2
    # 3
    # 4
    # 5
    print(i)

for num in nums:
    for letter in "abc":
        # 1 a
        # 1 b
        # 1 c
        # 2 a
        # 2 b
        # 2 c
        # 3 a
        # 3 b
        # 3 c
        # 4 a
        # 4 b
        # 4 c
        # 5 a
        # 5 b
        # 5 c
        print(num, letter)

for num in nums:
    if num % 2 == 0:
        # 2 is even.
        # 4 is even.
        print(f"{num} is even.")
    else:
        # 1 is odd.
        # 3 is odd.
        # 5 is odd.
        print(f"{num} is odd.")

    