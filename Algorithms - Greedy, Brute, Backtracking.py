#-------------------------------------------Greedy Algorithm--------------------------------------
list_coins=[5,15,20]
#---change this to 5,15,20 and change to 30 - nonoptimized, optimized 1,2,5 and change=6
change=30

print(len(list_coins))
list_coins.sort()

index=len(list_coins)-1

counter=0
while change>0:

    while True:
        if list_coins[index]<=change:

            counter+=1
            change=change-list_coins[index]
        else:
            break

    print("Denomination:",list_coins[index],"-",counter)
    counter=0
    index-=1


#-----------------------------Using brute force-------------------------------------
list_coins=[1,5,8,10,12,20]
length=len(list_coins)
comb=len(list_coins)
counter=0
tmp=0
list_val=[]
list_deno=[]
iter=0
i=len(list_coins)
while comb>0:
    index = len(list_coins) - 1
    print(index)
    change=30
    list_val=[0]*length
    i=length-comb
    comb1=0
    while change>0:

        while True:
            if list_coins[index]<=change:
                counter+=1
                iter+=1
                change=change-list_coins[index]
            else:
                break
        list_val[i]=counter

        i+=1

        counter=0
        index-=1
    if comb==length:
        tmp=iter
    elif iter<tmp:
        tmp=iter
        comb1=comb
    iter=0
    list_deno.append(list_val)
    print(list_deno)

    list_coins.pop()
    comb-=1

print(list_deno[comb1])

