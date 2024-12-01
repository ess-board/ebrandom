extern "C" { 
    const int N = 624;            // 상태 배열 크기
    const int M = 397;            // 주기적 성분
    const unsigned int MATRIX_A = 0x9908b0df; // 매트릭스 A
    const unsigned int UPPER_MASK = 0x80000000; // 상위 비트 마스크
    const unsigned int LOWER_MASK = 0x7fffffff; // 하위 비트 마스크

    unsigned int mt[N]; // 상태 배열
    int mti = N + 1; // mt 배열의 인덱스

    // 초기화 함수
    void initialize(unsigned int seed) {
        mt[0] = seed; // 시드 설정
        for (int i = 1; i < N; i++) {
            mt[i] = (1812433253UL * (mt[i - 1] ^ (mt[i - 1] >> 30)) + i);
            mt[i] &= 0xffffffff; // 32비트로 마스크
        }
    }

    // 난수 생성 함수
    unsigned int getNumber() {
        unsigned int y;
        static unsigned int mag01[2] = {0x0, MATRIX_A};

        if (mti >= N) { // mt 배열이 고갈되면 다시 생성
            for (int k = 0; k < N - M; k++) {
                y = (mt[k] & UPPER_MASK) | (mt[k + 1] & LOWER_MASK);
                mt[k] = mt[k + M] ^ (y >> 1) ^ mag01[y & 0x1];
            }
            for (int k = N - M; k < N - 1; k++) {
                y = (mt[k] & UPPER_MASK) | (mt[k + 1] & LOWER_MASK);
                mt[k] = mt[k + (M - N)] ^ (y >> 1) ^ mag01[y & 0x1];
            }
            y = (mt[N - 1] & UPPER_MASK) | (mt[0] & LOWER_MASK);
            mt[N - 1] = mt[M - 1] ^ (y >> 1) ^ mag01[y & 0x1];
            mti = 0; // 인덱스 초기화
        }

        y = mt[mti++];

        // 비트 변환
        y ^= (y >> 11);
        y ^= (y << 7) & 0x9d2c5680;
        y ^= (y << 15) & 0xefc60000;
        y ^= (y >> 18);

        return y; // 난수 반환
    }

    unsigned int getNumberInRange(unsigned int min, unsigned int max) {
        return min + (getNumber() % (max - min + 1));
    }

    double getUD01(){
        return getNumber() / 4294967296.0;
    }
}


