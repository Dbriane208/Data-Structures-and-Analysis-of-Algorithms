def Sorted_Squared ():

    array = [1,2,3,4,5]

    sortedArray = []

    for value in range(len(array)):

        array1 = array[value]* array[value]
        sortedArray.append(array1)    

    return sortedArray

myArray = Sorted_Squared()

print(myArray)
