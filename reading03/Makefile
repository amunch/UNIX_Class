all: hello-dynamic hello-static hello-debug hello-profile

hello-dynamic:
	gcc hello.c -o hello-dynamic

hello-static:
	gcc -static hello.c -o hello-static

hello-debug:
	gcc -g hello.c -o hello-debug

hello-profile:
	gcc -pg hello.c -o hello-profile

clean:
	rm hello-*
