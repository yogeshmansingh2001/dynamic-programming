## Can sum / sum of subset without memoization
def canSum(targetsum, numbers):
    if targetsum == 0:
        return True
    if targetsum < 0:
        return False
    
    for num in numbers:
        remainder = targetsum - num
        if (canSum(remainder,numbers) == True):
            return True

    return False

#print (canSum(5,[2,3]))
#print (canSum(5,[3,3,3]))
#print (canSum(300,[7,14]))

## Can sum / sum of subset with memoization
cache = {}

def canSum_memo(targetsum, numbers):
    if targetsum in cache:
        return cache[targetsum]
    if targetsum == 0:
        return True
    if targetsum < 0:
        return False
    
    for num in numbers:
        remainder = targetsum - num
        if (canSum_memo(remainder,numbers) == True):
            cache[targetsum] = True
            return True

    cache[targetsum] = False
    return False

#print (canSum_memo(5,[2,3]))
#print (canSum_memo(5,[3,3,3]))
#print (canSum_memo(300,[7,14]))

## CanSum using iteration (Tabulation) - Non recusrion
def canSum_Iterative(targetsum,numbers):
    false_value = False
    table = [false_value] * (targetsum+1) # for canSum_Iterative(7,[5,3,4]) -> [0,1,2,3,4,5,6,7,8] starts from zero
    table[0] = True # Base scenarion canSum_Iterative(0,[.....]) -> True
    #print(range(len(table)))
    for i in range(len(table)):
        if table[i] == True:
            for num in numbers:
                if i+num < len(table):table[i+num] = True
    
    #print(table)
    return table[targetsum]

print(canSum_Iterative(7,[2,3]))
print(canSum_Iterative(7,[5,3,4,7]))
print(canSum_Iterative(7,[2,4]))
print(canSum_Iterative(8,[2,2,2,2]))
print(canSum_Iterative(300,[7,14]))