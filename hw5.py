for i in range(100,1000):
    for j in range(100,1000):
        sum=i*j
        if sum/100000 !=0:
            a=sum//100000
            b=sum%100000//10000
            c=sum%100000%10000//1000
            d=sum%100000%10000%1000//100
            e=sum%100000%10000%1000%100//10
            f=sum%100000%10000%1000%100%10
            if a==f and b==e and c==d :
                maxnum=sum
              

print(maxnum)


            
