num = 1234
sum = 0
while (num/10 >10):
    print(num)
    print(sum)
    sum += num%10
    num = num//10

#print(sum)
sum = sum +num
print(sum)    