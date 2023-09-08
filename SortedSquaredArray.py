#o(n) space and o(n) time complexity

def Sorted_Squared ():

    array = [-5,-2,-1,0,1,2,3]

    sortedArray = []

    for value in range(len(array)):

        array1 = array[value]* array[value]
        sortedArray.append(array1)    

    return sortedArray

myArray = Sorted_Squared()

print(myArray)

#The code above is an improvement of the one below in time and space complexity
#The one below has a time complexity of O(n2) and space complexity of O(n)

# def squaredArray(list):
    
#     # //Perform a bubble sort then square the output
#     for element in range(len(list)):
#         for value in range(element + 1,len(list)):
#             if abs(list[element]) > abs(list[value]):
#                 temp = list[element]
#                 list[element] = list[value]
#                 list[value] = temp
                
#     for index in range(len(list)):
#         list[index] *= list[index]
        
#     return list
    
# list = [-5,-2,-1,0,1,2,3]
# sort = squaredArray(list)
# print(sort)
