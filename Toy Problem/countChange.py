target = 100 #4
coins = [10,20,50] #[1,2,3]
ways = [1]+[0]*target
for coin in coins:
    for i in range(coin,target+1):
        ways[i]+=ways[i-coin]
print(ways[target])