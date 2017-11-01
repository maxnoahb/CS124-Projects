all: strassen.class Matrix.class
strassen.class: strassen.java
	javac -d . -classpath . strassen.java
Matrix.class: Matrix.java
	javac -d . -classpath . Matrix.java
clean:
	rm -f *.class 