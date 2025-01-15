def TwoSum ():

    nums = [7,6,8,2,3]
    target = 10

    for index in range(len(nums)):
        for value in range(index+1,len(nums)): 
                    
            if  nums[index] + nums[value]  == target:
                return [index,value]              

                return []
        
myArray = TwoSum ()
print(myArray)



       