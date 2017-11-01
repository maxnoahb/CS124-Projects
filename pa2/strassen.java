import java.io.*;
import java.util.*;
import java.lang.*;

/*

CS124 Programming Assignment 2
March 24, 2017
Harvard IDs: 10939860, 60950350

USAGE: 
$ make
$ java strassen <flag> <dimension> <inputfile>

*/

public class strassen {
    // to test for the optimal cross-over point, we changed this value
    private static int crossover = 130;

    public static void main(String[]args) throws Exception{
        final int dimension = Integer.parseInt(args[1]);
        final String given_matrices = args[2];
        
        // read matrix ASCII file (using our matrix file) and put values in 2D arrays
        Matrix[] matrices = Matrix.readMatrices(given_matrices, dimension);
        int[][] matrix1 = matrices[0].matrixValues;
        int[][] matrix2 = matrices[1].matrixValues;
        
        // for testing:
        //int[][] matrix1 = {{1, 1, 1, 1, 1}, {1, 1, 1, 1, 1}, {1, 1, 1, 1, 1}, {1, 1, 1, 1, 1}, {1, 1, 1, 1, 1}};
        //int[][] matrix2 = {{2, 2, 2, 2, 2}, {2, 2, 2, 2, 2}, {1, 2, 3, 4, 5}, {1, 2, 3, 4, 5}, {5, 4, 3, 2, 1}};
        
        if (dimension <= 0) {
            throw new Exception("dimension must be greater than 0");
        }
        
        if (args.length != 3) {
            throw new Exception("usage: java strassen <flag> <dimension> <inputfile>");
        }
        
        // time for testing
        // long startTime = System.currentTimeMillis();

        // run strassens, putting the product answer in a new matrix
        int[][] product = strassens(matrix1, matrix2, dimension);

        // long endTime = System.currentTimeMillis();

        // print diagonal of product matrix
        for (int i = 0; i < dimension; i++){
            System.out.println(product[i][i]);
        } 
        // for testing
        // System.out.println("That took " + (endTime - startTime) + " milliseconds!");
    }

    private static int[][] strassens(int[][] A, int[][] B, int dimension){
        int[][] product = new int[dimension][dimension];
        if (dimension <= crossover) {
            return traditionalMult(A, B);
        }
    //  these cases were to test only Strassen's : 
    // if (dimension == 1){
    //      product[0][0] = A[0][0] * B[0][0];
    //      return product;
    //  }
    //  if (dimension == 2) {
       //     int a = A[0][0];
       //     int b = A[0][1];
       //     int c = A[1][0];
       //     int d = A[1][1];
       //     int e = B[0][0];
       //     int f = B[0][1];
       //     int g = B[1][0];
       //     int h = B[1][1];
       //     int p1 = a*(f - h);
       //     int p2 = (a + b)*h;
       //     int p3 = (c + d)*e;
       //     int p4 = d*(g - e);
       //     int p5 = (a + d)*(e + h);
       //     int p6 = (b - d)*(g + h);
       //     int p7 = (a - c)*(e + f);
             
       //     product[0][0] = p5 + p4 - p2 + p6;
       //     product[0][1] = p1 + p2;
       //     product[1][0] = p3 + p4;
       //     product[1][1] = p5 + p1 - p3 - p7;

       //       return product;
       // }
        
        // if dimension is even, recurse on strassens
        else if (dimension % 2 == 0) {
            // create 8 new arrays, breaking up A and B into 4 subarrays
            int[][] A1 = new int[dimension / 2][dimension / 2];
            int[][] A2 = new int[dimension / 2][dimension / 2];
            int[][] A3 = new int[dimension / 2][dimension / 2];
            int[][] A4 = new int[dimension / 2][dimension / 2];
            int[][] B1 = new int[dimension / 2][dimension / 2];
            int[][] B2 = new int[dimension / 2][dimension / 2];
            int[][] B3 = new int[dimension / 2][dimension / 2];
            int[][] B4 = new int[dimension / 2][dimension / 2];
            
            // fill subarrays with original matrices A and B
            for (int i = 0; i < (dimension / 2); i++) {
                for (int j = 0; j < (dimension / 2); j++) {
                    A1[i][j] = A[i][j];
                    B1[i][j] = B[i][j];
                    A2[i][j] = A[i + (dimension / 2)][j];
                    B2[i][j] = B[i + (dimension / 2)][j];
                    A3[i][j] = A[i][j + (dimension / 2)];
                    B3[i][j] = B[i][j + (dimension / 2)];
                    A4[i][j] = A[i + (dimension / 2)][j + (dimension / 2)];
                    B4[i][j] = B[i + (dimension / 2)][j + (dimension / 2)];
                }
            }

            // recurse over strassens
            int[][] p1 = strassens(A1, subtractMatrix(B3, B4), (dimension / 2));
            int[][] p2 = strassens(addMatrix(A1, A3), B4, (dimension / 2));
            int[][] p3 = strassens(addMatrix(A2, A4), B1, (dimension / 2));
            int[][] p4 = strassens(A4, subtractMatrix(B2, B1), (dimension / 2));
            int[][] p5 = strassens(addMatrix(A1, A4), addMatrix(B1, B4), (dimension / 2));
            int[][] p6 = strassens(subtractMatrix(A3, A4), addMatrix(B2, B4), (dimension / 2));
            int[][] p7 = strassens(subtractMatrix(A1, A2), addMatrix(B1, B3), (dimension / 2));
            
            int[][] C1 = addMatrix(p5, addMatrix(subtractMatrix(p4, p2), p6));
            int[][] C2 = addMatrix(p3, p4);
            int[][] C3 = addMatrix(p1, p2);
            int[][] C4 = addMatrix(p5, subtractMatrix(p1, addMatrix(p3, p7)));
            
            // combine back into final larger matrix
            for (int i = 0; i < (dimension / 2); i++) {
                for (int j = 0; j < (dimension / 2); j++) {
                    product[i][j] = C1[i][j];
                    product[i][j + (dimension / 2)] = C2[i][j];
                    product[i + (dimension / 2)][j] = C3[i][j];
                    product[i + (dimension / 2)][j + (dimension / 2)] = C4[i][j];
                }
            }
            
            return product;
        }
        // if dimension is odd, pad with one row and column of 0s and recurse
        else {
            int pad = dimension + 1;

            int[][] A1 = new int[pad][pad];
            int[][] B1 = new int[pad][pad];
            
            // new arrays automatically fill with 0s, so just add original values
            for (int i = 0; i < dimension; i++) {
                for (int j = 0; j < dimension; j++) {
                    A1[i][j] = A[i][j];
                    B1[i][j] = B[i][j];
                }
            }
            
            int[][] C1 = strassens(A1, B1, pad);
            
            // fill product matrix with information from padded multiplication
            // when we fill product, it will only fill the non-padding values
            for (int i = 0; i < dimension; i++) {
                for (int j = 0; j < dimension; j++) {
                    product[i][j] = C1[i][j];
                }
            }
            
            return product;
        }
    }
    
    // perform conventional matrix multiplication, assuming square matrices
    private static int[][] traditionalMult(int[][] A, int[][] B) {
        int[][] C = new int[A.length][A.length];
        
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < A.length; j++) {
                for (int k = 0; k < A.length; k++) {
                    C[i][j] += A[i][k] * B[k][j];
                }
            }
        }
        return C;
    }
    
    // helper to perform matrix addition
    private static int[][] addMatrix(int[][] A, int[][] B) {
        int[][] C = new int[A.length][A.length];
        
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < A.length; j++) {
                C[i][j] = A[i][j] + B[i][j];
            }
        }
        return C;
    }
    
    // helper to perform matrix subtraction
    private static int[][] subtractMatrix(int[][] A, int[][] B) {
        int[][] C = new int[A.length][A.length];
        
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < A.length; j++) {
                C[i][j] = A[i][j] - B[i][j];
            }
        }
        return C;
    }
}