# Question: Given an array of integers, sort the elements in ascending order using the selection sort algorithm.

# Example:
# Input: [5, 2, 9, 1, 7]
# Output: [1, 2, 5, 7, 9]

#Solution:

def Selection_sort(numValues):

    for num in range(len(numValues)-1):
        current_num = num

        for value in range(num+1, len(numValues)):
            if numValues[current_num] > numValues[value]:
                current_num = value
            
        if num != current_num:
                
            numValues[num],numValues[current_num] = numValues[current_num],numValues[num]

    return numValues

list = [5, 1, 7, 2, 1, 9, 9, 7]
print(Selection_sort(list))






        
    



