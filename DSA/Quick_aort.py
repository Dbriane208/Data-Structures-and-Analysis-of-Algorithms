#Define the swap function

def swap (list, index1, index2):
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp

def pivot(list, pivot_end, end_index):
    swap_index = pivot_end

    for i in range(pivot_end+1,end_index+1):
        if list[i] < list[pivot_end]:
            swap_index += 1
            swap(list, swap_index, i)
    swap(list,pivot_end,swap_index)
    return swap_index

def quick_sort_helper(list, left, right):

    if left < right:
        pivot_end = pivot(list,left, right)
        quick_sort_helper(list,left,pivot_end-1)
        quick_sort_helper(list,pivot_end+1,right)
    return list

def quick_sort(list):
    return quick_sort_helper(list,0,len(list)-1)

unsorted_list = [23,45,87,1,14,90,56,-4,-10,63,46,56]
quick_sort(unsorted_list)
print(unsorted_list)       

