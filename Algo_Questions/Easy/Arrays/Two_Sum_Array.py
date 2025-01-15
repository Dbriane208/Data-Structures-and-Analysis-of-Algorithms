# Method 1 using has table
# space O(n) | time O(n) where n is the length of the array
def twoSumArray(array, targetSum):
    hashTab = {}

    for val in array:
        result = targetSum - val
        if result in hashTab:
            return [result, val]
        else:
            hashTab[val] = True

    return []   


# Method 2 using sorting techniques
# requires array to be sort first
# time O(nlogn) | space O(1)
def twoSumArray(array, targetSum):
    # sort the array
    array.sort()

    left = 0
    right = len(array) - 1

    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum > targetSum:
            right -= 1  
        elif currentSum < targetSum:
            left += 1

    return []  

# Method 3 using the bruteforce method
# time O(n^2) | space O(1)
def twoSumArray(array, targetSum):
    for i in range(len(array)-1):
        firstNum = array[i]

        for j in range(i + 1, len(array)):
            secondNum = array[j]

            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
            
    return []        


