def canConstruct(target, workbank):
    if target == '':
        return True
    
    for word in  workbank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if canConstruct(suffix,workbank) == True:
                return True
            
    return False

#print (canConstruct('abcdef',['ab', 'abc', 'cd', 'def', 'abcd']))
#print (canConstruct('skateboard',['bo', 'rd', 'ate', 't', 'ska','sk','boar']))
#print (canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e', 'ee', 'eee', 'eeee', 'eeeee','eeeeee','eeeeeee']))

cache = {}

def canConstruct_memo(target, workbank):

    if target in cache: return cache[target]
    if target == '':
        return True
    
    for word in  workbank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if canConstruct_memo(suffix,workbank) == True:
                cache[target] = True
                return True

    cache[target] = False        
    return False

#print (canConstruct_memo('abcdef',['ab', 'abc', 'cd', 'def', 'abcd']))
#print (canConstruct_memo('skateboard',['bo', 'rd', 'ate', 't', 'ska','sk','boar']))
#print (canConstruct_memo('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e', 'ee', 'eee', 'eeee', 'eeeee','eeeeee','eeeeeee']))

def canConstruct_Iterative(target, wordbank):
    false_value = False
    table = [false_value] * (len(target)+1)
    table[0] = True
    for i in range(len(table)):
        if table[i] == True:
            for word in wordbank:
                length = i + len(word)
                #print(length)
                #print(target[i : length])
                #exit()
                if target[i : length] == word:
                    #print(target[i : length])
                    table[length] = True

    #print(table)
    return table[len(target)]

print (canConstruct_Iterative('abcdef',['ab', 'abc', 'cd', 'def', 'abcd']))
print (canConstruct_Iterative('skateboard',['bo', 'rd', 'ate', 't', 'ska','sk','boar']))
print (canConstruct_Iterative('enterpotentpot',['a', 'p', 'ent', 'enter', 'ot','o','ot']))
print (canConstruct_Iterative('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e', 'ee', 'eee', 'eeee', 'eeeee','eeeeee','eeeeeee']))
