import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class MatrixPowered_10830 {
    private static int[][] multiply(int[][] board, int[][] board2){
        int N = board.length;
        int[][] newBoard = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int sum = 0;
                for (int k = 0; k < N; k++) {
                    sum += board[i][k] * board2[k][j];
                }
                newBoard[i][j] = sum%1000;
            }
        }
        return newBoard;
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        long B = Long.parseLong(st.nextToken());

        int[][] matrix = new int[N][N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st_ = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                matrix[i][j] = Integer.parseInt(st_.nextToken());
            }
        }

        long twoPowered = 1;
        int[][] twoPoweredMatrix = matrix;

        int[][] answer = new int[N][N];
        for (int i = 0; i < N; i++) { //identical matrix
            for (int j = 0; j < N; j++) {
                if(i == j) answer[i][j] = 1;
                else answer[i][j] = 0;
            }
        }

        while(B != 0){
            if(B % 2 == 1){
                answer = multiply(answer, twoPoweredMatrix);
            }
            twoPoweredMatrix = multiply(twoPoweredMatrix, twoPoweredMatrix);
            B = B >> 1;
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(answer[i][j] + " ");
            }
            System.out.println();
        }
    }
}

