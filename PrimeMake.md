소수를 생성하는 작업을 할때에는, 1은 소수가 아닌 점과 2는 유일한 짝수인 소수인 점을 감안하여, 3부터 작업을 하는게 편한 작업에 도움을 줄 것이다.

77이 소수인가를 판단할때, 2로 나눠보았을때 나머지가 0이 아니고, 3으로 나눠보았을때 나머지가 0이 아니다.
이때 4로도 나누어 볼 필요는 없다. 4는 2 x 2로 나타낼 수 있고, 2로 나눴을때 나머지가 0이 아니었다면 마찬가지로 4로 나눴을때도 나머지가 0이 아닐 것임을 알 수 있다.

이를 일반화하면 산술의 기본정리인 "(1이 아닌)모든 자연수는 한 개 이상의 소수들의 곱으로 유일하게 나타낼 수 있다."를 도출해낸다.

따라서 <img src="https://latex.codecogs.com/svg.image?N" title="https://latex.codecogs.com/svg.image?N" />이 소수인가를 판단할 때에는, <img src="https://latex.codecogs.com/svg.image?N" title="https://latex.codecogs.com/svg.image?N" /> 이하의 모든 소수로만 나누어보아 나머지가 0인지를 판단해보면 된다.

그러나 <img src="https://latex.codecogs.com/svg.image?N" title="https://latex.codecogs.com/svg.image?N" /> 이하의 소수의 갯수도 생각보다 많다. [소수 정리](https://ko.wikipedia.org/wiki/%EC%86%8C%EC%88%98_%EC%A0%95%EB%A6%AC)에 의해 <img src="https://latex.codecogs.com/svg.image?N" title="https://latex.codecogs.com/svg.image?N" /> 이하의 소수의 개수는

<img src="https://latex.codecogs.com/svg.image?\frac&space;N&space;{\ln&space;N}" title="https://latex.codecogs.com/svg.image?\frac N {\ln N}" />
이나
<img src="https://latex.codecogs.com/svg.image?{\rm&space;Li}&space;(N)&space;=&space;&space;&space;\int_2^N&space;\frac{dt}{\ln&space;t}&space;\;" title="https://latex.codecogs.com/svg.image?{\rm Li} (x) = \int_2^x \frac{dt}{\ln t} \;" />

개임이 알려져있다.

따라서 <img src="https://latex.codecogs.com/svg.image?N" title="https://latex.codecogs.com/svg.image?N" />이 소수인가를 판단할 땐, <img src="https://latex.codecogs.com/svg.image?\sqrt{N}" title="https://latex.codecogs.com/svg.image?\sqrt{N}" /> 이하의 모든 소수로만 나누어보면 된다.

<img src="https://latex.codecogs.com/svg.image?N" title="https://latex.codecogs.com/svg.image?N" />이 <img src="https://latex.codecogs.com/svg.image?\sqrt{N}" title="https://latex.codecogs.com/svg.image?\sqrt{N}" /> 이상의 두 소인수만을 가진다고 가정하면, 당연히 두 소인수를 곱하였을 때 <img src="https://latex.codecogs.com/svg.image?N" title="https://latex.codecogs.com/svg.image?N" />보다 커지는 것은 자명하기 때문이다. (귀류법)

---

장기적으로 소수를 계속 만들어내는 시스템을 만들고자 한다면, 어떤 큰 수 N까지 소수를 전부 다 센 후,

N+1이 소수인지...N+2가 소수인지...를 계속 판단해가야 할 것이다.

그런데 이때, 짝수인 소수는 2밖에 없음을 생각해본다면 짝수는 아예 판단기준에서 뺄 필요가 있음을 알게 된다.

N이 2의 배수였다면, N+1, N+3, N+5...만 판단해보면 될 일이다. N+2나 N+4는 짝수이기때문에 애초에 소수가 아니다.

![image](https://user-images.githubusercontent.com/104616990/166138391-687d7b00-006c-41f9-a6cf-6789c2cc67f2.png)

모든 2k+2 꼴은 걸러낼 수 있다. (전체의 1/2)

이때 N을 더욱 확장하면 거를 것들은 점점 더 늘어난다.

N이 3의 배수라면, N+3, N+6...도 걸러낼 수 있고, 6의 배수일때를 그림으로 나타내면 다음과 같다.

![image](https://user-images.githubusercontent.com/104616990/166138527-682c3864-789c-4fb3-b6b8-c86c8d6442c4.png)

무려 6개중에 6k+2(2의 배수), 6k+3(3의 배수), 6k+4(2의 배수), 6k+6(2, 3의 배수)의 4개를 걸러낼 수 있다. (전체의 (1/2) x (2/3)으로 줄어듦.)

따라서 6k+1, 6k+1+4, 6k+1+4+2, 6k+1+4+2+4... 의 방식으로 4를 더했다가 2를 더했다가를 반복하면 더 빠르게 소수를 찾아낼 수 있다.

N이 30(2 x 3 x 5)의 배수라면 어떻게 될까?

![image](https://user-images.githubusercontent.com/104616990/166138735-2c0cfcf8-2910-4b5f-806d-79cd5b3d5923.png)

전체의 (1/2) x (2/3) x (4/5) 로 줄어, 30개 중에 8개만 선택하면 된다.

이 과정을 계속 늘려나간다면, 전체 비중은 0%로 수렴하게 될까? 아니면 어떤 수로 수렴하게 될까?

<img src="https://latex.codecogs.com/svg.image?\prod_{}^{\infty&space;}\left&space;(&space;&space;\frac{p-1}{p}&space;\right&space;)&space;=&space;\prod_{}^{\infty&space;}\left&space;(&space;&space;1&space;-&space;\frac{1}{p}&space;\right&space;)" title="https://latex.codecogs.com/svg.image?\prod_{}^{\infty }\left ( \frac{p-1}{p} \right ) = \prod_{}^{\infty }\left ( 1 - \frac{1}{p} \right )" />

소수 p에 대하여 다음과 같은 무한곱을 취하면, 0으로 수렴할까? 0이 아닌 수로 수렴할까?

검색해보니, 과거에 이를 증명한 사람이 있었다. [메르텐스의 제3정리](https://ko.wikipedia.org/wiki/%EB%A9%94%EB%A5%B4%ED%85%90%EC%8A%A4_%EC%A0%95%EB%A6%AC_(%EC%88%98%EB%A1%A0))에 의하면

<img src="https://latex.codecogs.com/svg.image?\prod_{p\leq&space;n}\left(1-{{1}\over{p}}\right)&space;\approx&space;&space;{{e^{-\gamma}}\over{\ln&space;n}}" title="https://latex.codecogs.com/svg.image?\prod_{p\leq n}\left(1-{{1}\over{p}}\right) \approx {{e^{-\gamma}}\over{\ln n}}" />
임을 알 수 있다. "N이 (2 x 3 x 5 x ... x M)의 배수"에서 M이 커질수록 계산 속도가 매우 빨라진다.

M을 2라 하면, 2k+1, 2k+1+2, 2k+1+2+2...에서 홀수에서 2만 계속 더해주는 식으로 연산해주고,

M을 3이라 하면, 6k+1, 6k+1+4, 6k+1+4+2...에서 4를 더했다가 2를 더했다가를 반복해준다.

M이 5일때는 30k+1에서 30k+1+6(30k+7), 30k+1+6+4(30k+11), 30k+1+6+4+2(30k+13), 30k+1+6+4+2+4(30k+17), 30k+1+6+4+2+4+2(30k+19), 30k+1+6+4+2+4+2+4(30k+23), 30k+1+6+4+2+4+2+4+6(30k+29)에서 30k+1+6+4+2+4+2+4+6+2(30k+31=30k+1) 으로, [6, 4, 2, 4, 2, 4, 6, 2]를 차례대로 더해준다.




