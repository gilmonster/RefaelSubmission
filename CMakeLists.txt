output: Encripter.o
	g++ Encripter.o
	
Encripter.o: Encripter.py
	g++ -c Encripter.py
	
clean:
	rm *.o output