CC=		gcc
CFLAGS=		-Wall -std=c99 -g
LD=		gcc
LDFLAGS=	
AR=		ar
ARFLAGS=	rcs
TARGETS=	libgcd.a libgcd.so gcd-dynamic gcd-static

all:	$(TARGETS)

gcd-static: main.o libgcd.a
	$(LD) $(LDFLAGS) -static -o gcd-static main.o libgcd.a

gcd-dynamic: main.o libgcd.so
	$(LD) $(LDFLAGS) -o gcd-dynamic -L. main.o -lgcd

libgcd.a: gcd.o
	$(AR) $(ARFLAGS) libgcd.a gcd.o

libgcd.so: gcd.o
	$(CC) $(CFLAGS) -shared -o libgcd.so gcd.o

%.o: %.c
	$(CC) -c $(CFLAGS) -o $@ $^

clean:
	rm -f $(TARGETS) *.o 
