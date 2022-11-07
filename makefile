RAIDIX : RAIDIX.o
	g++ RAIDIX.o -o RAIDIX

RAIDIX.o : RAIDIX.cpp
	g++ -c RAIDIX.cpp -o RAIDIX.o

clean:
	rm -f *.o RAIDIX
