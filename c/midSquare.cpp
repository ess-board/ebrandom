#include <cmath>

extern "C" {
    int seed;

    // 초기화 함수
    void initialize(int initialSeed) {
        seed = initialSeed % 1000000;
        if (seed == 0) seed = 1;
    }

    int getNumber() {
        int digits = 6;  // 시드 자릿수
        
        long long squared = static_cast<long long>(seed) * seed;
        
        int totalDigits = log10(squared) + 1;
        int start = (totalDigits - digits) / 2;
        long long divisor = static_cast<long long>(pow(10, start));
        long long mid = (squared / divisor) % static_cast<long long>(pow(10, digits));

        // 시드 갱신 및 고정 패턴 방지
        seed = static_cast<int>(mid);
        if (seed == 0) seed = 1;  // 0 방지
        seed = (seed * 65537 + 12345) % 1000000;

        if (seed < 0) seed = -seed;  // 음수면 양수로 변환
        return seed;
    }

    int getNumberInRange(int min, int max) {
        return min + (getNumber() % (max - min + 1));
    }

    double getUD01() {
        return getNumber() / 1000000.0;
    }
}
