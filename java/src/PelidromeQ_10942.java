import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class PelidromeQ_10942 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] nums = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        int M = Integer.parseInt(br.readLine());

        int[][] Q = new int[M][2];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            Q[i][0] = Integer.parseInt(st.nextToken()) - 1;
            Q[i][1] = Integer.parseInt(st.nextToken()) - 1;
        }
        br.close();

        boolean[][] dp = new boolean[N][N];

        for (int i = 0; i < N; i++) {
            dp[i][i] = true;
        }

        for (int i = 0; i < N - 1; i++) {
            dp[i][i + 1] = nums[i] == nums[i + 1];
        }

        for (int length = 2; length < N; length++) {
            for (int i = 0; i + length < N; i++) {
                if(nums[i] == nums[i + length] && dp[i + 1][i + length -1]){
                    dp[i][i + length] = true;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < M; i++) {
            if(dp[Q[i][0]][Q[i][1]])  sb.append(1 + "\n");
            else sb.append(0 + "\n");
        }
        System.out.println(sb.toString());
    }
}
