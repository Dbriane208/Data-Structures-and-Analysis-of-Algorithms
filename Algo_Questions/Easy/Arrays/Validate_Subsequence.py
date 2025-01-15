# time O(n) | space O(1)
def validateSequence(array,sequence):
    smallIdx = 0
    for value in array:
        if smallIdx == len(sequence):
            break
        if sequence[smallIdx] == value:
            smallIdx += 1

    return smallIdx == len(sequence)        

def validateSequence(array,sequence):
    arrIdx = 0
    seqIdx = 0

    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
        return seqIdx == len(sequence)    