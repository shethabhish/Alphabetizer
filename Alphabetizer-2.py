# Function that takes in a series of string and returns them in sorted order
def alphabetizer(string):
    # Edge case to check if the given string is empty or invalid and return empty string
    if not string:
        return ""
    # Filtering out all invalid characters
    result = list(filter(str.isalpha, string))
    # Calling merge sort function to return the result
    return "".join(merge_sort(result))


def merge_sort(result):
    # If there is 1 of no elements the result array
    if len(result) < 2:
        return result
    # Find the middle index
    mid = len(result)//2
    # Partition the left of the array
    left = merge_sort(result[:mid])
    # Partition the right of the array
    right = merge_sort(result[mid:])
    # Merge the left the right partition
    return merge(left, right)


def merge(left, right):
    # Array to store the result
    result = []
    # While left and right are not empty
    while left and right:
        # Comparing which alphabet is smaller and adding it to the result array
        if left[0].lower() <= right[0].lower():
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    # Flushing out the rest of the non empty array
    result += left or right
    # Returning the result array
    return result


# Simple function that checks few test cases.
def alphabetizer_tests():
    print(alphabetizer("VirginiaTech"))
    print(alphabetizer("3 Blind Mice"))
    print(alphabetizer(""))
    print(alphabetizer("                  "))
    print(alphabetizer("12345678"))
    print(alphabetizer("He  ll o   , World;"))


# Calling the test function
alphabetizer_tests()

"""
Time Complexity:
Since we perform a regular merge sort and compare elements and place them in the right position, the time complexity is => O(N*logN), where N is the number of alphabets.

Space Complexity:
We have an result array to store the alphabets after comparing, the space complexity is => O(N), where N is the number of alphabets.
"""
