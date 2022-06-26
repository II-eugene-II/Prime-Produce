## 밀러-라빈 소수 판별법

---

[참고 자료1 (블로그)](https://man-25-1.tistory.com/99) (한국 자료중에는 제일 잘 정리된 듯 보인다.)

[참고 자료2 (위키백과 한글판)](https://ko.wikipedia.org/wiki/%EB%B0%80%EB%9F%AC-%EB%9D%BC%EB%B9%88_%EC%86%8C%EC%88%98%ED%8C%90%EB%B3%84%EB%B2%95)

[참고 자료3 (위키백과 영문판)](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)

최초 시작은 $p$가 소수이면 서로소인 정수 $a$에 대하여 $a^{p-1} \equiv 1\(\bmod{p})$ 이라는 페르마의 소정리에서 출발한다.

$p$가 소수일때는 이 식이 확실히 맞으며, $p$가 소수가 아닐때도 간간히 맞는 경우가 있어서 주의를 요한다.

확실한 것은 $a^{p-1} \equiv 1\(\bmod{p})$ 가 아닐때에는 **무조건** 합성수라는 데에 있다.

---

이 이상은 이해가 되는대로 내용을 추가하는 것으로 하고, 참고 자료 1에서 가져온 블로그에서 참고를 한다.

```
import random

def miller_rabin_test(n,a,r,d):
    # n은 odd integer
    # b는 base
    # n-1 = 2^r * d
    x = pow(a, d, n)  # a0= a^d mod n
    if x == 1 or x == n-1:
        return 1
    else: # a0가 +-1이 아니라면
        for i in range(s):
            if x==n-1:
                return 1
            x= pow(x,2,n)
        return 0

def is_prime(n):
    r=0
    if n<2 or not n&1:
        return 0 # 짝수이거나 1은 소수가 아니다.
    if n==2:
        return 1 # 2는 소수이다.
    d = (n-1)
    while d%2==0:
        r+=1
        d>>=1
    mini_primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    for a in mini_primeList:
        test = miller_rabin_test(n, a, r, d)
        if test==0:
            return 0
    return 1

N = input()
N = int(N)

if is_prime(N):
  print("높은 확률로 소수") # N이 3317044064679887385961981 보다 작으면 확실한 소수
else:
  print("확실한 합성수") # 소수라고 출력했으나 사실은 합성수인 경우는 있어도, 합성수라고 출력했으나 사실 소수인 경우는 없음
```

N이 3,317,044,064,679,887,385,961,981 (2^64보다 한참 큰 2^81과 2^82 사이의 수이다.) 보다 작으면 a = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41에 대해서만 검사해봐도 [충분히 검증 가능하다고 한다](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)

원래대로의 밀러 소수판정법에서는 **리만 가설이 맞다는 가정 하에** 2(ln(N))^2 보다 작은 소수들을 가지고 판정해야 확인이 가능한데 2(ln(3,317,044,064,679,887,385,961,981))^2 의 값이 대략 6375인 점을 감안하면 굉장히 빠른 소수 판정법인 셈이다.
