pWant = 4000000 # pWant까지의 소수 구하기

primeList = [2, 3, 5, 7]

def isPrime(N): # 소수면 1 아니면 0
    lenPL = len(primeList)
    w = 0
    while(w < lenPL and primeList[w] ** 2 <= N):
        if(N % primeList[w] == 0):
            return 0
        w += 1      
    return 1

pTest = 11

while(pTest < pWant):

    if(isPrime(pTest)):
        primeList.append(pTest)

    pTest += 2

    if(isPrime(pTest)):
        primeList.append(pTest)

    pTest += 4

print(primeList)
