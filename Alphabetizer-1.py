# Function that takes in a series of string and returns them in sorted order
def alphabetizer(string):
    # Edge case to check if the given string is empty or invalid and return empty string
    if not string:
        return ""
    # To store the result
    result = []
    # Iterate over the given string and store only valid alphabets
    for i in string:
        if i.isalpha():
            result.append(i)
    # First loop to go over all elements
    for i in range(len(result)):
        # Second loop to go over all elements
        for j in range(len(result)):
            # Check if the indexes are not same and check which alphabet is smaller
            if i != j and result[i].lower() < result[j].lower():
                # Swap the elements
                result[i], result[j] = result[j], result[i]
    # Converting to string format
    result = "".join(result)
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
We iterate over the given string two times and compare each alphabet to find the minimum and swap their postions, the time complexity is => O(N*N), where N is the number of alphabets.

Space Complexity:
We have an result array to store the alphabets into a list format because strings are immutable, the space complexity is => O(N), where N is the number of alphabets.
"""
