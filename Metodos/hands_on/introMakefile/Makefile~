lineas.dat:cuenta.py salida.txt
	python cuenta.py
salida.txt:a.out
	./a.out>salida.txt
a.out:hola.c #Target:Requirement
	gcc hola.c #Commands to issue if requierement is newer than target
clean:
	rm -f a.out salida.txt lineas.dat
