# Alphabetizer

## Method 1: Use a Hammer (Brute Force):

Maintain two ```for``` loops to iterate over the input string and compare each element and swap them according to ascending order.

Time Complexity:
We iterate over the given string two times and compare each alphabet to find the minimum and swap their postions, the time complexity is => ```O(N*N)```, where N is the number of alphabets.

Space Complexity:
We have an result array to store the alphabets into a list format because strings are immutable, the space complexity is => ```O(N)```, where N is the number of alphabets.

## Method 2: Merge Sort:

Perform Regular Merge Sort. Split the input string into two halves until there is one element is left in both halves, compare both the elements and merge them in ascending order and continue doing it for the rest of the string.

![image](https://user-images.githubusercontent.com/20106435/116936647-fe461680-ac1c-11eb-85ed-8a2a1a239f1f.png)

Time Complexity:
Since we perform a regular merge sort and compare elements and place them in the right position, the time complexity is => ```O(N*logN)```, where N is the number of alphabets.

Space Complexity:
We have an result array to store the alphabets after comparing, the space complexity is => ```O(N)```, where N is the number of alphabets.

## Method 3: Use buckets (Bucket Sort):

Maintain 26 buckets since there are 26 alphabets and in each bucket maintain the frequency of the corresponding alphabet number and their captilization, at the end iterate over the buckets to form the result string.

![image](https://user-images.githubusercontent.com/20106435/116937997-eff8fa00-ac1e-11eb-8385-bf9aa864b254.png)

Time Complexity:
There are only 26 Alphabets, so we maintain 26 buckets to keep track of the frequency of each alphabet and form the result string, the time complexity is => ```O(N)```, where N is the number of alphabets.

Space Complexity:
We have an result array to store the alphabets after comparing, the space complexity is => ```O(N)```, where N is the number of alphabets. If the result array is not taken into space complexity consideration, the the space complexity is -> ```O(1)```
