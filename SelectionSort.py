# Question: Given an array of integers, sort the elements in ascending order using the selection sort algorithm.

# Example:
# Input: [5, 2, 9, 1, 7]
# Output: [1, 2, 5, 7, 9]

#Solution:

def Selection_sort(numValues):

    for num in range(len(numValues)):
        current_num = num

        for value in range(num+1, len(numValues)):
            if numValues[current_num] > numValues[value]:
                current_num = value

                numValues[num],numValues[current_num] = numValues[current_num],numValues[num]

list = [5, 2, 9, 1, 7]
Selection_sort(list)

print(list)
