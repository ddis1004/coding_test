import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Zelda_4485 {
    static final int[] dx = new int[]{0, 1, 0, -1};
    static final int[] dy = new int[]{1, 0, -1, 0};
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        while(N != 0){
            int[][] board = new int[N][N];
            boolean[][] visited = new boolean[N][N];

            for (int i = 0; i < N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    board[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int[][] dp = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    dp[i][j] = Integer.MAX_VALUE;
                }
            }

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {

                }
            }
        }
    }
}
