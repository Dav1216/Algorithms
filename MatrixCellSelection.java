public class MatrixCellSelection {
     static int backtrack(int[][] M, boolean[] S, int k) {
         if(M.length == 0) {
             return Integer.MAX_VALUE;
         }
        if (k == S.length - 1) {
            // matrix is size lMatrix X lMatrix
            int lMatrix = M.length;
            // s_index is the index to iterate through the S array
            int s_index = 0;

            // check that our solution S doesn't contain any zeros
            for(int i = 0; i < lMatrix; i++) {
                for(int j = 0; j < lMatrix; j++) {
                    if (S[s_index] && M[i][j] == 0) {
                        return Integer.MAX_VALUE;
                    }
                    s_index++;
                }
            }

            // reset s_index is the index to iterate through the S array
            s_index = 0;
            // create intermediate matrix where every non selected character is 0 (for ease of column and row checking)
            int[][] MIntermediate = new int[lMatrix][lMatrix];

            for(int i = 0; i < lMatrix; i++) {
                for (int j = 0; j < lMatrix; j++) {
                    if (!(S[s_index] && M[i][j] == 1)) {
                        MIntermediate[i][j] = 0;
                    } else {
                        MIntermediate[i][j] = 1;
                    }
                    s_index++;
                }
            }

            // row check that every row contains at least one 1
            for(int i = 0; i < lMatrix; i++) {
                boolean intermediateCorrectSolution = false;

                for(int j = 0; j < lMatrix; j++) {
                    intermediateCorrectSolution = intermediateCorrectSolution || (MIntermediate[i][j] == 1);
                }

                if(intermediateCorrectSolution == false) {
                    return Integer.MAX_VALUE;
                }
            }

            // row check that every column contains at least one 1
            for(int i = 0; i < lMatrix; i++) {
                boolean intermediateCorrectSolution = false;

                for(int j = 0; j < lMatrix; j++) {
                    intermediateCorrectSolution = intermediateCorrectSolution || (MIntermediate[j][i] == 1);
                }

                if(intermediateCorrectSolution == false) {
                    return Integer.MAX_VALUE;
                }
            }

            // if everything is fine, calculate solution size
            int solution = 0;

            for (int i = 0; i < S.length; i++) {
                if (S[i]) {
                    solution++;
                }
            }

            return solution;
        } else {
             // initialize min solution value
             int min = Integer.MAX_VALUE;
             // first branch, the k + 1 th element in our solution is true
             S[k + 1] = true;
             // obtain min value for the case we are on (true)
             min = Math.min(min, backtrack(M, S, k + 1));
             // first branch, the k + 1 th element in our solution is false
             S[k + 1] = false;
            // obtain min value for the case we are on (false)
             min = Math.min(min, backtrack(M, S, k + 1));

             return min;
        }
    }

     public static void main(String[] args) {
        // initialize a test matrix
        int[][] M = new int[][] { {1, 1, 0, 1}, {0, 1, 0, 1}, {0, 0, 1, 0}, {1, 1, 0, 0} };
        // initialize solution
        boolean[] S = new boolean[M.length * M.length];
        // print min-sized solution
        System.out.println(backtrack(M, S, -1));
    }
}
