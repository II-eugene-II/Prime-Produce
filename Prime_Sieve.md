# 에라토스테네스의 체와 그 최적화

---

소수 관련 문제를 풀던 중 기존 소수 판정 방식이 좀 느리다 생각하여 다른 방법을 찾던 중 [에라토스테네스의 체](https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4#cite_note-1) 방식을 찾았다.

①
```
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]
```

그러나 이 방식대로도 조금 늦어서, 더 빠른 방법을 생각해보게 된다.

기존의 방식은 i가 2부터 시작하여 어쩔 수 없이 모든 짝수를 한번씩 다 훑어야 한다는데에 있다.

②
```
def prime_Sieve(n):
    
    sieve = [True] * n                       # 태초에 모든 칸은 True(소수)로 판단
    
    m = int(n ** 0.5)                        # 소수가 아니라면 약수가 2와 sqrt(N) 사이에 있다.
    for i in range(4, n, 2):
        sieve[i] = False                     # 2가 아닌 2의 배수를 전부 False(합성수)로 판단
    
    for i in range(3, m + 1, 2):             # i는 3부터 홀수만 따짐
        
        if sieve[i] == True:                 # i가 소수 일때는
            for j in range(3 * i, n, 2 * i): # i가 아닌 i의 배수들을 전부 False(합성수)로 판단
                sieve[j] = False             # 2의 배수를 이미 제거했으므로 3i, 5i, 7i...만 제거

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]
```

이렇게 되면 짝수 부분은 굳이 확인 할 필요도 없고,
차례대로 진행했을때 3의 배수 제거시, 기존엔 3, 6, 9, 12, 15를 하나하나 False 처리 했던것과 대조적으로, 더 빨리 3, 9, 15, 21...을 False 처리한다.

그러나 이 방법도 만족스럽지 못하여, 한번 더 빠르게 만들기에 이른다.

③
```
def prime_Sieve(n):
    
    sieve = [True] * n                       # 태초에 모든 칸은 True(소수)로 판단
    
    m = int(n ** 0.5)                        # 소수가 아니라면 약수가 2와 sqrt(N) 사이에 있다.
    
    for i in range(4, n, 2):
        sieve[i] = False                     # 2가 아닌 2의 배수를 전부 False(합성수)로 판단
        
    for i in range(9, n, 6):
        sieve[i] = False                     # 3이 아닌 3의 배수를 전부 False(합성수)로 판단
    
    for i in range(3, m + 1, 2):             # i는 3부터 홀수만 따짐
        
        if sieve[i] == True:                 # i가 소수 일때는
            for j in range(5 * i, n, 6 * i): # i가 아닌 i의 배수들을 전부 False(합성수)로 판단
                sieve[j] = False
            for j in range(7 * i, n, 6 * i):
                sieve[j] = False             # 2, 3의 배수를 이미 제거했으므로 5i, 7i, 11i, 13i, ...만 제거

    # 소수 목록 산출
    return [2] + [i for i in range(3, n, 2) if sieve[i] == True]
```

-> 2의 배수도, 3의 배수도 미리 다 쳐내버린다.

2, 3을 제외하면 모든 소수는 6k-1, 6k+1꼴인 점을 감안하여, i가 소수면 5i, 7i, 11i, 13i...만 제거한다. (다른 수들은 이미 2와 3에 의해 제거당했으므로)



-> 출력할때도 2는 따로 넣고 홀수들만 판단한다.

맨 처음에 2를 넣어줘야 하기때문에 i for i in range(2, n) 이었으나, 그러면 4한테도 "너가 소수니?"를 물어봐야하고...6한테도 굳이 물어봐야하고...

따라서 2는 별개로 분류한다.

---

잘 생각해보니 그렇다면 짝수는 굳이 분류할 필요도 없어진다.

④
```
def prime_Sieve(n):
    
    sieve = [True] * n                       # 태초에 모든 칸은 True(소수)로 판단
    
    m = int(n ** 0.5)                        # 소수가 아니라면 약수가 2와 sqrt(N) 사이에 있다.
    
    #for i in range(4, n, 2):
    #    sieve[i] = False                    # 2가 아닌 2의 배수를 전부 False(합성수)로 판단...하지도 않고 아예 무시한다.
        
    for i in range(9, n, 6):
        sieve[i] = False                     # 3이 아닌 3의 배수를 전부 False(합성수)로 판단
    
    for i in range(3, m + 1, 2):             # i는 3부터 홀수만 따짐
        
        if sieve[i] == True:                 # i가 소수 일때는
            for j in range(5 * i, n, 6 * i): # i가 아닌 i의 배수들을 전부 False(합성수)로 판단
                sieve[j] = False
            for j in range(7 * i, n, 6 * i):
                sieve[j] = False             # 2, 3의 배수를 이미 제거했으므로 5i, 7i, 11i, 13i, ...만 제거

    # 소수 목록 산출
    return [2] + [i for i in range(3, n, 2) if sieve[i] == True]
```

2의 배수를 아예 무시함으로써 $\frac{1][2]N$회 정도의 연산을 아예 안해도 된다. 에라토스테네스의 체의 시간복잡도가 $O(N loglog N)$ 정도라고 하니 의미 있는 횟수라고 볼 수 있다. ($loglog 2^{64}$ 가 대략 3.79 정도이므로 굉장히 미미한 증가 속도를 지닌다.)

---

더 찾다보니 i x i 번쨰부터 제거해도 된다는 이야기가 보인다.

기존 알고리즘에선 i=29라면 5 x 29, 7 x 29, 11 * 29, ... 를 False 처리해야했지만 어차피 그 수들은 5, 7, 11 등이 제거 완료한 상태이기 때문이다.

⑤
```
def prime_Sieve(n):
    
    sieve = [True] * n                           # 태초에 모든 칸은 True(소수)로 판단
    
    m = int(n ** 0.5)                            # 소수가 아니라면 약수가 2와 sqrt(N) 사이에 있다.
    
    #for i in range(4, n, 2):
    #    sieve[i] = False                        # 2가 아닌 2의 배수를 전부 False(합성수)로 판단...하지도 않고 아예 무시한다.
        
    for i in range(9, n, 6):
        sieve[i] = False                         # 3이 아닌 3의 배수를 전부 False(합성수)로 판단
    
    for i in range(3, m + 1, 2):                 # i는 3부터 홀수만 따짐
        
        if sieve[i] == True:                     # i가 소수 일때는
            if (i%6) == 5:
                i2 = i+2
                for j in range(i * i, n, 6 * i): # i가 아닌 i의 배수들을 전부 False(합성수)로 판단
                    sieve[j] = False
                for j in range(i2 * i, n, 6 * i):
                    sieve[j] = False             # 2, 3의 배수를 이미 제거했으므로 5i, 7i, 11i, 13i, ...만 제거
            else:
                i4 = i+4
                for j in range(i * i, n, 6 * i): # i가 아닌 i의 배수들을 전부 False(합성수)로 판단
                    sieve[j] = False
                for j in range(i4 * i, n, 6 * i):
                    sieve[j] = False             # 2, 3의 배수를 이미 제거했으므로 5i, 7i, 11i, 13i, ...만 제거

    # 소수 목록 산출
    return [2] + [i for i in range(3, n, 2) if sieve[i] == True]
```

최초의 방식보다 굉장히 길어지고 복잡해진 모습이다.

각각의 시간을 측정해보자.

![image](https://user-images.githubusercontent.com/104616990/173785020-4f10c643-5d7e-4070-96bb-d3fdbfd46d01.png)

①의 위키백과판으로 1억까지의 소수 갯수를 세는데에 15초가 걸렸다.

5761445개도 맞는 모습이다.

![image](https://user-images.githubusercontent.com/104616990/173785847-818be120-318b-4c76-9d66-eb73d0563ae0.png)

②에서는 기존에 2i, 4i, 6i, 8i, ...를 다 False 처리하던 문제점을 제거하여, 3i, 5i, 7i만 처리하고, i 자체도 홀수만 검색하도록 바꾸었더니 굉장히 정직하게 ①의 2/3 정도로 줄어든 모습이다.

![image](https://user-images.githubusercontent.com/104616990/173786934-8843d8b9-288c-4216-b6a5-42d23b2c206d.png)

③에서는 ②에서의 (6k+3)i를 다 False 처리하던 문제점을 제거하고, 마지막 출력에서도 2를 별개 취급 후 홀수만 훑어서 출력한다.

생각보단 시간이 확 단축되진 않았으나, 그래도 15% 정도 더 빠르게 만들었다.

![image](https://user-images.githubusercontent.com/104616990/173787846-56d9d424-eadf-44c4-b450-c18977fc915b.png)

④에서는 아예 짝수를 판단하지도 않고 패싱해버렸다.

$\frac{1][2]N$회 정도의 연산을 안할 수 있을것이라곤 생각했으나, 꽤 큰 것이었는지 무려 ③에서 ②으로 올때 단축된 것 만큼 또 단축되었다.

이제 ①의 위키백과 판의 절반도 안되는 수치이다.

![image](https://user-images.githubusercontent.com/104616990/173788567-774001a3-4048-40af-ba3e-cdf2024fd635.png)

⑤에서는 0.1초 정도를 단축하는데에 그쳤다. 생각해보면 N = 1억이 입력된다고 해도, i가 10000보단 작으니 (루트1억 = 1만) 큰 차이가 나진 않는듯 하다.

또한 i를 6으로 나눠보는데에서 i가 커질수록 나눗셈 자체가 부담스러울 수 있으니, ④와 ⑤는 거의 비슷한 알고리즘이라고 볼 수 있을 듯 하다.

...더 줄일 수 있을까?
