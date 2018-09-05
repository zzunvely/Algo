#pragma warning (disable : 4996) 
#include <stdio.h>
#include <string.h>


int n = 0;
int StackArr[10001] = { 0, };
void push();
void pop();
void empty();
void size();
void top();

int main(void) {
	int N;
	scanf("%d", &N);
	char command[12];
	int i;

	for (i = 0; i < N; i++) {
		scanf("%s", command);
		if (strcmp(command, "push") == 0) {
			push();
		}
		else if (strcmp(command, "pop") == 0) {
			pop();
		}
		else if (strcmp(command, "size") == 0) {
			size();
		}
		else if (strcmp(command, "empty") == 0) {
			empty();
		}
		else if (strcmp(command, "top") == 0) {
			top();
		}

	}

}

void push() {
	scanf("%d", &StackArr[n++]);
}
void pop() {
	if (n) {
		printf("%d\n", StackArr[--n]);
	}
	else {
		printf("%d\n", -1);
	}
}

void size() {
	printf("%d\n", n);
}

void empty() {
	if (n) {
		printf("0\n");
	}
	else {
		printf("1\n");
	}

}

void top() {
	if (n) {
		printf("%d\n", StackArr[n - 1]);

	}
	else {
		printf("-1\n");
	}
}

