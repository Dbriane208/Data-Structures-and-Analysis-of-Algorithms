# Question: Given an array of integers, sort the elements in ascending order using the shell sort algorithm.

# Example:

#input = [19, 2, 31, 45, 30, 11, 121, 27]
#output = [2, 11, 19, 27, 30, 31, 45, 121]  

def Shell_sort(list):

    gap = len(list) // 2

    while gap > 0:

        for value in range(gap, len(list)):

            temp = list[value] #stores the current element to be stored in the correct position
            value_list = value # stores the value

            while value_list >= gap and list[value_list - gap] > temp:

        # We swap the elements

              list[value_list] = list[value_list - gap]
              value_list = value_list - gap
              list[value_list] = temp

        gap = gap // 2

list = [19, 2, 31, 45, 30, 11, 121, 27]

Shell_sort(list)
print(list)

                 