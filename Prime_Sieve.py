def prime_Sieve(n):
    
    sieve = [True] * n                       # 태초에 모든 칸은 True(소수)로 판단
    
    m = int(n ** 0.5)                        # 소수가 아니라면 약수가 2와 sqrt(N) 사이에 있다.
    for i in range(4, n, 2):
        sieve[j] = False                     # 2가 아닌 2의 배수를 전부 False(합성수)로 판단
    
    for i in range(3, m + 1, 2):             # i는 3부터 홀수만 따짐
        
        if sieve[i] == True:                 # i가 소수 일때는
            for j in range(3 * i, n, 2 * i): # i가 아닌 i의 배수들을 전부 False(합성수)로 판단
                sieve[j] = False             # 2의 배수를 이미 제거했으므로 3i, 5i, 7i...만 제거

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]
  
# https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4#cite_note-1
