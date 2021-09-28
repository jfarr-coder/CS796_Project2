CPPFLAGS = -g -DDEBUG

objects = obj/Rectangle.o

all: PaintingMimic

clean: 
	rm $(objects)
	rm ./bin/Sokoban

PaintingMimic: $(objects)
	g++ $(CPPFLAGS) $(objects)
	mv a.out ./bin/Sokoban

obj/%.o: src/%.cpp include/%.h
	g++ $(CPPFLAGS) -c ./src/$*.cpp
	mv $*.o ./obj 

obj/main.o: ./src/main.cpp ./include/*.h
	g++ $(CPPFLAGS) -c ./src/main.cpp
	mv main.o ./obj	
