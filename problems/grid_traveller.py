## Grid Travller without memoization
def gridTraveller(m,n):
    if (m ==1 and n ==1):
        return 1
    if (m==0 or n==0):
        return 0
    return gridTraveller(m-1,n) + gridTraveller(m,n-1)

#print (gridTraveller(2,3))
#print (gridTraveller(3,3))
#print (gridTraveller(4,3))
#print (gridTraveller(0,3))
#print (gridTraveller(2,0))
#print (gridTraveller(14,14))

## Grid Travller with memoization
cache = {}

def gridTraveller_memo(m,n):
    key = str(m) + ',' + str(n)
    if key in cache:
        return cache[key]
    if (m ==1 and n ==1):
        return 1
    if (m==0 or n==0):
        return 0
    cache[key] = gridTraveller_memo(m-1,n) + gridTraveller_memo(m,n-1)
    return cache[key]

#print (gridTraveller_memo(2,3))
#print (gridTraveller_memo(3,3))
#print (gridTraveller_memo(4,3))
#print (gridTraveller_memo(0,3))
#print (gridTraveller_memo(2,0))
#print (gridTraveller_memo(18,18))

## Grid Traveller using iteration (Tabulation) - Non recusrion
def grid_Traveller(m,n):
    table = [[0 for i in range(n+1)] for j in range(m+1)] # Index starts from zero so m+1, n+1
    #arr[0][0] = 1
    table[1][1] = 1
    #print(len(table))
    for i in range(m+1):
        for j in range(n+1):
            #print(table[i][j])
            current = table[i][j]
            if (j+1 <= n): table[i][j+1] += current
            if (i+1 <= m): table[i+1][j] += current
            
    return table[m][n]

print (grid_Traveller(1,1))
print (grid_Traveller(2,3))
print (grid_Traveller(3,2))
print (grid_Traveller(3,3))
print (grid_Traveller(18,18))