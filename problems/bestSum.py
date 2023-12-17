## How sum / sum of subset without memoization
def bestSum(targetsum, numbers):
    if targetsum == 0: return []
    if targetsum < 0: return None

    shortestCombination = None
    
    for num in numbers:
        remainder = targetsum - num
        remianderResult = bestSum(remainder,numbers)
        if (remianderResult is not None):
            combination = [*remianderResult,num]
            if ((shortestCombination == None) or (len(combination) < len(shortestCombination))):
                shortestCombination = combination
                #return combination
            
            #return [*remianderResult,num]

    return shortestCombination

#print (bestSum(7,[5,3,4,7]))
#print (bestSum(7,[2,3]))
#print (bestSum(8,[1,4,5]))
#print (bestSum(100,[1,2,5,25]))

## Best sum / sum of subset with memoization
cache = {}

def bestSum_memo(targetsum, numbers):
    if targetsum in cache: return cache[targetsum]
    if targetsum == 0: return []
    if targetsum < 0: return None

    shortestCombination = None
    
    for num in numbers:
        remainder = targetsum - num
        remianderResult = bestSum_memo(remainder,numbers)
        if (remianderResult is not None):
            combination = [*remianderResult,num]
            if ((shortestCombination == None) or (len(combination) < len(shortestCombination))):
                shortestCombination = combination
                #return combination
            
            #return [*remianderResult,num]
    cache[targetsum] = shortestCombination
    return shortestCombination

#print (bestSum_memo(7,[5,3,4,7]))
#print (bestSum_memo(7,[2,3]))
#print (bestSum_memo(8,[1,4,5]))
#print (bestSum_memo(100,[1,2,5,25]))

def bestSum_Iterative(targetsum, numbers):
    false_value = None
    table = [false_value] * (targetsum+1) # for bestSum_Iterative(7,[5,3,4]) -> [0,1,2,3,4,5,6,7,8] starts from zero
    table[0] = [] # Base scenarion bestSum_Iterative(0,[.....]) -> []
    for i in range(len(table)):
        if table[i] is not None:
            for num in numbers:
                if (i+num) < len(table):
                    combination = [*table[i],num]
                    if ((not table[i+num]) or len(table[i+num]) > len(combination)):
                        table[i+num] = combination
    #print (table)
    return table[targetsum]

print(bestSum_Iterative(7,[5,3,4,7]))
print(bestSum_Iterative(8,[2,3,5]))
print(bestSum_Iterative(8,[1,4,5]))
print(bestSum_Iterative(100,[1,2,5,25]))
print(bestSum_Iterative(300,[7,14]))