def delete_duplicate_valid_entry(arr):
  
  if not arr:
    return
  
  count = 1
  for i in range(len(arr) - 1):
    
    if arr[i] == arr[i+1]:
      continue
      
    count+=1
    
  return count

def delete_duplicate(arr):
  
  indx = 1
  for i in range(1,len(arr)):
    
    if arr[indx-1] != arr[i]:
      arr[indx] = arr[i]
      indx+=1
      
      

 
