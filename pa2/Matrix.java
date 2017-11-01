import java.io.*;
import java.util.*;
import java.lang.*;

// class to represent matrices
public class Matrix {
    public int dimension;
    public int[][] matrixValues;
    
    public Matrix(int[][] matrixValues) {
        this.matrixValues = matrixValues;
        this.dimension = matrixValues.length;
    }
    
    // function to read matrices from a text file of integers, one per line
    public static Matrix[] readMatrices(String inputfile, int dimension) {
        
        // make an array of size 2d^2
        String[] lines = new String[2*dimension*dimension];
        
        // read the file line by line, placing the integers into an array
        try {
            // begin reading the file
            FileReader file = new FileReader(inputfile);
            BufferedReader file1 = new BufferedReader(file);

            // put all numbers into an array
            for (int i = 0; i < lines.length; i++)
            {
                String line = file1.readLine();
                lines[i] = line;
            }
            file1.close();
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }
        
        // initalize two 2D arrays to pass to strassens
        int[][] m1 = new int[dimension][dimension];
        int[][] m2 = new int[dimension][dimension];
        
        // separate the array into the two matrices
        int place = 0;
        for (int i = 0; i < dimension; i ++) {
            for (int j = 0; j < dimension; j ++) {
                m1[i][j] = Integer.parseInt(lines[place]);
                place ++;
            }
        }
        for (int i = 0; i < dimension; i ++) {
            for (int j = 0; j < dimension; j ++) {
                m2[i][j] = Integer.parseInt(lines[place]);
                place ++;
            }
        }
        
        Matrix[] matrices = new Matrix[2];
        matrices[0] = new Matrix(m1);
        matrices[1] = new Matrix(m2);
        return matrices;
        
    }
}