#include <iostream>
#include <string>
using namespace std;

int sum_from_to(int first, int last) {
    int result = 0;
    for (int i = 0; i < last; i++) {
        result += first + i;
    };
    return result;
};

int enough(int num) {
    int counter = 0;
    int result = 0;
    for (int i = 0; counter < num; i++) {
        counter += 1 + i;
        result = 1 + i;
    };
    return result;
};

int main() {
    cout << sum_from_to(1, 10);
    cout << enough(21) << endl;
};

