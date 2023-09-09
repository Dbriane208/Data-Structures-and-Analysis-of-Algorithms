#0 . CONSTANT TIME O(1)
#The function takes aproximately same time to perform the same operation of given num input

def example0(num):
    return num % 2 == 0
output = example0(5)
print(output)

#1. LINEAR TIME O(n)
# The total time take by this function is 2n + 1 hence the time complexity of 0(n) 
# because as the n grows large the constants doesn't matter.

def example1(nums):
    total = 0
    for number in nums:
        total += number
    return total    
 
 
#2. QUADRATIC NOTATION O(n^2)
#The total time take by the function is n + 3n^2 + 1
#The greatest power of the function, n^2, is always the time complexity of the function

def example2(nums):
    results = [1 for _ in range(len(nums))]

    for i, num1 in enumerate(nums):
        for num2 in nums:
            if num1 == num2:
              continue
            results[i] *= num2
        return results  

#3. BIG-O OF O(n+m)
# The function takes two differents inputs which we will represent as n and m
# The total time of the function will be n + 3n + m removing the constants we have the time complexity as 0(n+m)

def example3(nums1,nums2):
    results = []

    for num in nums1:
        results.append(num)

    for i, num in enumerate(nums2):
        if i >= len(results):
            results.append(i)
        results[i] *= num

    return results                

#4. BIG-O OF O(nm)
# Assuming all the constants the total time will be n(m+m+m) = O(nm)

def example4(nested_list):
    total = 1

    for inner_list in nested_list:
        for num in inner_list:
            total += num

        for num in inner_list:
            total += num

        for num in inner_list:
            total += num

    return total      

#5. BIG-O OF O(2^n)
# Since this is a recursive function for every input n into the algorithm the function will call itself twice 
# in a constant time. eg n = 5 it will have last = example5(5-1) = 4 and second_last = example5(5-2) = 3 hence
# the time complexity of 0(2^n)

def example5(n):
    if n == 1:
        return 1
    if n == 2:
        return 1

    last = example5(n-1)
    second_last = example5(n-2)
    return last + second_last

fib = example5(10)
print(fib)          

#6. BIG-O OF O(n+m)
# Most python inbuilt tools eg min,max takes constant time as they need to loop
# through all the items to find the least  or max values thus the total time = n + m
# hence O(n + m)

def example6(lst,search_list):
    max_value = max(lst)

    for value in search_list:
        if max_value == value:
            return True
    return False    

#7. BIG-O OF O(log base 2 n) : LOGARITHIMIC
# In theis recursive function we're not dividing the input in a constant time.ie as the 
# the number of input grows inproportional to the number of operations hence have a logarithimic time complexity O(log base 2 n)

def example7(n):
    if n == 0:
        return 1
    
    print(n)
    example7(round(n/2))

#8. BIG-O OF O(n(k log base 2 k))  
# The time complexity of the function is n because of the first function and k(log base 2 k) because of the 
# string loop and the sort function. 

def example8(strings):
    for i, string in enumerate(strings):

        digits = 0

        for char in string:
            if char in [str(i) for i in range(0,10)]:
                digit += 1
        if digits >= len(string) / 2 :
            strings[i] = sorted(strings[i])
    return strings

#9. BIG-O OF O(n log base 2 (n) + m log base 2 (m) + (n+m)k)
# n represents the first dictionary,m represents the second dictionary and lastly k represents the length of the longest key
# The total time complexity will be n log base 2 (n) + m log base 2 (m) + (n+m)k

def example9(dict1,dict2):
    keys1 = sorted(dict1.keys())
    keys2 = sorted(dict2.keys())

    process = keys1 + keys2
    results = set()

    while len(process) > 0:
        element = process.pop(0)
        results.append(element)

        if len(element) == 1:
            continue
        process.append(element[:-1])
    return results

#10. BIG-O OF O(n^3)
# The total time  = n * n * n hence a time complexity of O(n^3) 

def example10(nums):
    sum_to_end = []
    count = 0

    for i in range(len(nums)):
        num1 = nums[i]
        sum_to_end.append(0)

        for j in range(i + 1,len(nums)):
            num2 = nums[j]
            sum_to_end[i] += num2

            for _ in sum_to_end:
                count += 1
                print(count)
    return sum_to_end

ans = example10([1,2,3,4,5,6,7])
print(ans)  

#11. BIG-O OF O(n!)
# In this function the number of call made will depend on the size of n. The base case of each n wil be
# given by the permutation of n i.e n! hence the time complexity of O(n!)

def example11(n):
    if n == 1:
        return 1
    total = 0
    for _ in range(n):
        total += example11(n-1)
        return total
print(example11(2))    