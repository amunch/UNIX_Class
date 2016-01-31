all: hello-dynamic hello-debug hello-profile

hello-dynamic:
	gcc hello.c -o hello-dynamic

hello-debug:
	gcc -g hello.c -o hello-debug

hello-profile:
	gcc -pg hello.c -o hello-profile

clean:
	rm hello-*
