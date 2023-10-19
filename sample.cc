int z = 0;

struct __attribute__((annotate("A"))) A {
    int a;
    double b;
    char c[8];
    
    __attribute__((annotate("foo"))) int foo(int);
};

template <class T>
class B {
    T t;
    T wibble(T);
};

double bar(double);

int main () {

}
