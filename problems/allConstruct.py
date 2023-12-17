def allConstruct(target, wordBank):
    if target == '': return [[]]

    result = []

    for word in  wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix,wordBank)
            
            targetWays = [word, *suffixWays]
            #targetWays = list(map(suffixWays.append,word))
            result.extend(targetWays)

    return result

print (allConstruct('purple',['purp','p','ur','le','purpl']))