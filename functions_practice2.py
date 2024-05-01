def max_num(*nums):
    max = nums[0]
    for num in nums[1:]:
        if num > max:
            max = num
    
    print(max)

max_num(1, 2, 5, 4, 3, 10, 14, 12, 11)

def mult_list(*nums):
    result = 1
    for num in nums:
        result *= num
    print(result)

mult_list(2, 5, 3, 4)


def rev_string(string):
    gnirts = string[::-1]
    print(gnirts)

rev_string('hello world i am alive')

def num_within(num, beg, end):
    start_range = beg
    end_range = end
    if start_range < num < end_range:
        print(True)
    else:
        print(False)

num_within(4, 1, 5)
num_within(1, 4, 5)

def pascal(n):
    
    triangle = []

    for i in range(n):
        row = [1]  # first element in each row is always 1
        if triangle:
            last_row = triangle[-1]
            # Generate elements of current row (except first and last)
            row.extend([last_row[j] + last_row[j + 1] for j in range(len(last_row) - 1)])
            row.append(1)  # last element in each row is always 1
        triangle.append(row)

    # Print Pascal's triangle
    for row in triangle:
        # Print leading spaces for formatting
        print(" " * (n - len(row)), end="")
        for num in row:
            print(num, end=" ")
        print()

pascal(1)

pascal(5)