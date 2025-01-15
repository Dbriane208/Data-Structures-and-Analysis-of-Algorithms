# time O(n) | space O(n)
def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]
    leftIdx = 0
    rightIdx = len(array) - 1

    for idx in reversed(range(len(array))):
        smallerValue = array[leftIdx]
        largerValue = array[rightIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedSquares[idx] = smallerValue * smallerValue
            smallerValue += 1
        else:
            sortedSquares[idx] = largerValue * largerValue
            largerValue -= 1

    return sortedSquares  

# time O(nlogn) | space O(n)
def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]
    for idx in range(len(array)):
        value = array[idx]
        sortedSquares[idx] = value * value

    sortedSquares.sort()
    return sortedSquares    
