import java.util.*;
import java.lang.*;
import java.io.*;

class RangeSum5_11660 {
    static int N, M;
    static int[][] board;
    static int[][] dp;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][N];
        dp = new int[N + 1][N + 1];

        for(int i = 0; i < N ; i ++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j ++){
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int i = 1; i < N + 1; i ++){
            for(int j = 1; j < N + 1; j ++){
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + board[i - 1][j - 1];
            }
        }

        for(int i =0; i < M; i ++){
            st = new StringTokenizer(br.readLine());
            int x1 =  Integer.parseInt(st.nextToken());
            int y1 =  Integer.parseInt(st.nextToken());
            int x2 =  Integer.parseInt(st.nextToken());
            int y2 =  Integer.parseInt(st.nextToken());

            int answer = dp[x2][y2] + dp[x1 - 1][y1 - 1] - dp[x1 - 1][y2] - dp[x2][y1 - 1];
            System.out.println(answer);
            
        }

    }
}
