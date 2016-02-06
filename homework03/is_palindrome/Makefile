all: is_palindrome

is_palindrome:
	gcc -g -std=gnu99 is_palindrome.c -o is_palindrome

clean:
	rm is_palindrome

test:
	./is_palindrome < is_palindrome.input | diff is_palindrome.output -
