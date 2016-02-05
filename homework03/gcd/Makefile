CC=		gcc
CFLAGS=		-Wall -std=c99 -g
LD=		gcc
LDFLAGS=	# TODO
AR=		ar
ARFLAGS=	# TODO
TARGETS=	main

all:	$(TARGETS)

gcd-static: main.o libgcd.a

gcd-dynamic: main.o libgcd.so

libgcd.a: gcd.o

libgcd.so: gcd.o

%.o: %.c
	$(CC) -c $(CFLAGS) -o $@ $^

clean:
	rm -f $(TARGETS) *.o
