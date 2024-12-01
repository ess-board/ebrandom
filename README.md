# ebrandom

여러 가지 난수 생성 알고리즘을 제공하는 모듈형 난수 생성 패키지입니다.<br>
선린인터넷고등학교 2024년도 자료구조 Term Project에 사용하기 위해 제작되었습니다.

## 기능
- 난수 생성:
  - **Mersenne Twister**
  - **Linear Congruential Generator**
  - **Mid Square Method**

## 설치 방법
패키지를 설치하려면 repository를 clone 후 다음 명령어를 실행하세요

```bash
# on your project
git clone https://github.com/ess-board/ebrandom.git
cd ebrandom
python setup.py install
```

## 사용 예시

```python
from ebrandom import lc_random, mt_random, ms_random

print(lc_random(1, 100))

print(mt_random(1, 100))

print(ms_random(1, 100))
```
