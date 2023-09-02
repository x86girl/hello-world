# Author: Priscila Gutierres
# License: MIT

.DEFAULT_GOAL := hello-world

CC = gcc

CC_FLAGS = -Wall 

hello-world.o:
	$(CC) $(CC_FLAGS) -c hello-world.c

hello-world: hello-world.o
	$(CC) -o $@ $^

install: hello-world
	cp ./$^ /usr/bin/$^
clean: hello-world
	rm -f hello-world.o 
	rm -f hello-world