# Function that takes in a series of string and returns them in sorted order
def alphabetizer(string):
    # Edge case to check if the given string is empty or invalid and return empty string
    if not string:
        return ""
    # Maintaing 26 buckets to count capital and small alphabet frequency
    buckets = [[0, 0] for _ in range(26)]
    # Iterating over the given string
    for ch in string:
        # Checking if the current element is alphabet or not
        if ch.isalpha():
            # If current element is not capital letter, increment it's count in it's appropriate bucket
            if ch.islower():
                buckets[ord(ch)-ord('a')][0] += 1
            # If current element is capital letter, increment it's count in it's appropriate bucket
            else:
                buckets[ord(ch)-ord('A')][1] += 1
    # String to store result
    result = ""
    # Iterating through our buckets
    for i in range(len(buckets)):
        # Checking if there is a non capital letter at the current position and adding them to the result string
        if buckets[i][0]:
            result += chr(ord('a')+i)*buckets[i][0]
        # Checking if there is a capital letter at the current position and adding them to the result string
        if buckets[i][1]:
            result += chr(ord('A')+i)*buckets[i][1]
    # Returning the result string
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
There are only 26 Alphabets, so we maintain 26 buckets to keep track of the frequency of each alphabet and form the result string, the time complexity is => O(N), where N is the number of alphabets.

Space Complexity:
We have an result array to store the alphabets after comparing, the space complexity is => O(N), where N is the number of alphabets.
"""
