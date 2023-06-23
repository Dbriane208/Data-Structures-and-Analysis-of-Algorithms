def Insertion_sort (list_temp):

    for temp in range (1, len(list_temp)):

        prevTemp = temp -1
        nxtTemp = list_temp[temp]

        while list_temp[prevTemp] > nxtTemp and (prevTemp >= 0):

            list_temp[prevTemp + 1] = list_temp[prevTemp]
            prevTemp = prevTemp -1
            list_temp[prevTemp + 1] = nxtTemp

list_temp = [23,45,87,1,14,90,56,-4,-10,63,46,56]

Insertion_sort(list_temp)
print(list_temp)            

