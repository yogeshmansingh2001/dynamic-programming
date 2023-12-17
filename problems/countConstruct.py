#count = 0
def countConstruct(target, workbank):
    if target == '':
        return 1
    totalCount = 0
    for word in  workbank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            noOfWay = countConstruct(suffix,workbank)
            totalCount += noOfWay
            
    return totalCount

#result = countConstruct('abcdef',['ab', 'abc', 'cd', 'def', 'abcd'])
#result = countConstruct('skateboard',['bo', 'rd', 'ate', 't', 'ska','sk','boar'])
#result = countConstruct('purple',['purp', 'p', 'ur', 'le', 'purpl'])
#result = countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e', 'ee', 'eee', 'eeee', 'eeeee','eeeeee','eeeeeee'])
#print(result)

cache = {}
def countConstruct_memo(target, workbank):
    if target in cache: return cache[target]
    if target == '':
        return 1
    totalCount = 0
    for word in  workbank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            noOfWay = countConstruct_memo(suffix,workbank)
            totalCount += noOfWay
    cache[target] = totalCount        
    return totalCount

#result = countConstruct('abcdef',['ab', 'abc', 'cd', 'def', 'abcd'])
#result = countConstruct('skateboard',['bo', 'rd', 'ate', 't', 'ska','sk','boar'])
#result = countConstruct_memo('purple',['purp', 'p', 'ur', 'le', 'purpl'])
#result = countConstruct_memo('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e', 'ee', 'eee', 'eeee', 'eeeee','eeeeee','eeeeeee'])
#print(result)

def countConstruct_Iterative(target,wordbank):
    false_value = 0
    table = [false_value] * (len(target)+1)
    table[0] = 1
    for i in range(len(table)):
        for word in wordbank:
            length = i + len(word)
            if target[i : length] == word:
                table[length] += table[i]

    #print (table)
    return table[len(target)]

print (countConstruct_Iterative('purple',['purp', 'p', 'ur', 'le', 'purpl']))
print (countConstruct_Iterative('abcdef',['ab', 'abc', 'cd', 'def', 'abcd']))
print (countConstruct_Iterative('skateboard',['bo', 'rd', 'ate', 't', 'ska','sk','boar']))
print (countConstruct_Iterative('enterpotentpot',['a', 'p', 'ent', 'enter', 'ot','o','ot']))
print (countConstruct_Iterative('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e', 'ee', 'eee', 'eeee', 'eeeee','eeeeee','eeeeeee']))