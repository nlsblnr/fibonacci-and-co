#include <iostream>

int fib(int n) {
	if (n == 0) {
		return 0;
	}
	else if (n == 1) {
		return 1;
	}

	return fib(n - 1) + fib(n - 2);
}

int main() {
	std::cout << "Calculate the following fibonacci number: ";
	int n;
	std::cin >> n;
	std::cout << fib(n);

	return 0;
}