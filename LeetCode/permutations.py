# Python program to print all permutations with
# duplicates allowed


# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
    if l==r:
        print ("".join(a))
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack

# # Driver program to test the above function
# string = "ABC"
# n = len(string)
# a = list(string)
# permute(a, 0, n-1)

# This code is contributed by Bhavya Jain


# Python function to print permutations of a given list
def permutation(lst):

    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = [] # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

    # Extract lst[i] or m from the list. remLst is
    # remaining list
        remLst = lst[:i] + lst[i+1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l


# # Driver program to test above function
# data = list('123')
# for p in permutation(data):
#     print(p)

from itertools import permutations
l = list(permutations(range(1, 4)))
print(l)

