test_string = "madamismalayalam"
for j in range (0,len(test_string)) :
  for i in range (j+1,len(test_string)):
    if(test_string[j:i] == test_string[j:i][::-1] and len(test_string[j:i]) != 1):
      print(test_string[j:i])
      #print(''.join(reversed(test_string[j:i])))
    else:
      bool=True
    

    
  
   
   
  


