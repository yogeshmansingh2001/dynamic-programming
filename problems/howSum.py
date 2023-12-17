#import gc
## How sum / sum of subset without memoization
def howSum(targetsum, numbers):
    if targetsum == 0: return []
    if targetsum < 0: return None
    
    for num in numbers:
        remainder = targetsum - num
        remianderResult = howSum(remainder,numbers)
        if (remianderResult is not None):
            return [*remianderResult,num]

    return None

#print (howSum(7,[2,3]))
#print (howSum(7,[5,3,4,7]))
#print (howSum(7,[2,4]))
#print (canSum(300,[7,14])

## Can sum / sum of subset with memoization
cache = {}

def howSum_memo(targetsum, numbers):
    if targetsum in cache: return cache[targetsum]
    if targetsum == 0: return []
    if targetsum < 0: return None
    
    for num in numbers:
        remainder = targetsum - num
        remianderResult = howSum_memo(remainder,numbers)
        if (remianderResult is not None):
            cache[targetsum] = [*remianderResult,num]
            return cache[targetsum]

    cache[targetsum] = None
    return None

#print (howSum_memo(7,[2,3]))
#gc.collect()
#print (howSum_memo(7,[5,3,4,7]))
#print (howSum_memo(7,[2,5]))
#print (howSum_memo(300,[7,14]))

## howSum using iteration (Tabulation) - Non recusrion
def howSum_Iterative(targetsum,numbers):
    false_value = None
    table = [false_value] * (targetsum+1) # for howSum_Iterative(7,[5,3,4]) -> [0,1,2,3,4,5,6,7,8] starts from zero
    table[0] = [] # Base scenarion howSum_Iterative(0,[.....]) -> []
    for i in range(len(table)):
        #print(i)
        if table[i] is not None:
            #print(table[i])
            for num in numbers:
                #print(i+num,len(table))
                #break
                if (i+num) < len(table):
                    #print("true")
                    #break
                    table[i+num] = [*table[i],num]
                    #print(table[i+num])
                    #break
            #break
            #print(table)

    #print(table)
    return table[targetsum]            

print(howSum_Iterative(7,[2,3]))
print(howSum_Iterative(7,[5,3,4]))
print(howSum_Iterative(7,[2,4]))
print(howSum_Iterative(8,[2,3,5]))
print(howSum_Iterative(300,[7,14]))