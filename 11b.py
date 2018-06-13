def subsetSum(ls, target):    
  pos = 0    
  while pos<len(ls) and ls[pos]<=target:        
    pos+=1    
    for i in range(pos+1):        
      for j in range(i):            
        for k in range(j):                
          if ls[i]+ls[j]+ls[k]==target:                    
            return True 
  return False 
print("Enter a list of numbers: ") 
ls = list(map(int, input().split())) 
print("Enter the target: ") 
target = int(input()) 
ls.sort() 
print(subsetSum(ls, target))
