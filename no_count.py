arrdup=[1,2,3,4,6,4,8,4,4,5,6,6,7,7,7,8,9,9,10];

arrlist = ["0"]

for i  in range(len(arrdup)):
    j=i+1
    count =0
    for j in range(len(arrdup)):
        if(arrdup[i]== arrdup[j] and arrdup[i] ):
            count=count+1
            arrlist.append(arrdup[i])
            
        
    print(arrdup[i] +"Coming"+ count)        