def PowersofTwo(num):
  if num == None:
    return None
    
  while num > 1:
    if num % 2 == 0:
      num = num / 2
    else:
      return False
  return True

num = input("Enter The Number: ") 
print(PowersofTwo(int(num)))