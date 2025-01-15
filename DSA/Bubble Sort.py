#Initialize the sort algorithm
def BubbleSort (list_years): 

    for year in range(len(list_years)-1,0,-1):
        for year_value in range(year):            
          if list_years[year_value] > list_years[year_value + 1]:                
           temp = list_years[year_value]
           list_years[year_value] = list_years[year_value + 1]
           list_years[year_value + 1] = temp
                
    #lets have a list that we want to sort
list_years = [2001, 1990,1450,2023,1900,1890]

BubbleSort(list_years)
print(list_years)
        
        
    
    
    
