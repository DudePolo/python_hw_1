# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

nested_arrays = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]
print(flatten_and_sort(nested_arrays))
'''
Make sure to answer the following questions about your coding process:

How does this solution ensure data immutability?
    -This solution ensures data immutability by not modifying the original input array or its elements

Is this solution a pure function? Why or why not?
    -Yes this will always return the same output and has no side effects. 

Is this solution a higher order function? Why or why not?
    -No, there's no function taken in the original argument

Would it have been easier to solve this problem using a different programming style?
    -It's all up to the coder

Why in particular is functional programming a helpful paradigm when solving this problem?
    -Functional programming emphasizes immutability, higher-order functions, and the absence of side effects, which can lead to cleaner, more maintainable, and easier-to-reason-about code. 

'''