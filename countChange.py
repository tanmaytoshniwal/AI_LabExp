target = 200 #4
coins = [1,2,5,10,20,50,100,200] #[1,2,3]
ways = [1]+[0]*target
for coin in coins:
    for i in range(coin,target+1):
        ways[i]+=ways[i-coin]
print(ways[target])