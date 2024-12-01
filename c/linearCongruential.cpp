#include <cstdint>

extern "C" {
    void initialize(int seed, int a, int c, int64_t m);
    unsigned int getNumber();
    unsigned int getRandomInRange(int min, int max);

    static int64_t current;
    static int a;
    static int c;
    static int64_t m;

    const int DEFAULT_A = 1664525;
    const int DEFAULT_C = 1013904223;
    const int64_t DEFAULT_M = 4294967296;

    void initialize(int seed, int a_init = DEFAULT_A, int c_init = DEFAULT_C, int64_t m_init = DEFAULT_M) {
        current = seed;
        a = a_init;
        c = c_init;
        m = m_init;
    }

    unsigned int getNumber() {
        current = (a * current + c) % m;
        return static_cast<unsigned int>(current);
    }

    unsigned int getNumberInRange(int min, int max) {
        unsigned int randomValue = getNumber();
        return min + (randomValue % (max - min + 1));
    }

    double getUD01(){
        return getNumber() / 4294967296.0;
    }
}
