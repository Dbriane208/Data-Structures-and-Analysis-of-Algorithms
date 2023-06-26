# Question: Given an array of integers, sort the elements in ascending order using the merge sort algorithm.

# Example:
# Input: [1, 2, 7, 8, 3, 4, 5, 6]
# Output: [1, 2, 3, 4, 5, 6, 7, 8]

#Solution:
def Merge_sort(input):
    if len(input) <= 1:
      return input
    
    middle = len(input) // 2
    left_sub = input[:middle]
    right_sub = input[middle:]

    left_sub = Merge_sort(left_sub)
    right_sub = Merge_sort(right_sub)
    return list(merge(left_sub, right_sub))

def merge(left_list, right_list):

    sorted_list = []

    while len(left_list) != 0 and len(right_list) != 0:

      if left_list[0] < right_list[0]:
        sorted_list.append(left_list[0])
        left_list.remove(left_list[0])
      else:
        sorted_list.append(right_list[0])
        right_list.remove(right_list[0])

    if len(left_list) == 0:
       sorted_list += right_list
    else:
       sorted_list += left_list
    return sorted_list
input = [1, 2, 7, 8, 3, 4, 5, 6]
print(Merge_sort(input))



