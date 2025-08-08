import java.io.BufferedReader;
import java.io.InputStreamReader;

public class ColorCircle_2482 {
    final static int MOD = 1000000003;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine()); // N colors
        int K = Integer.parseInt(br.readLine());  // K select

        if (K > N / 2) {
            System.out.println(0);
            return;
        }

        int[][] dp = new int[N + 1][K + 1];

        for (int i = 0; i <= N; i++) {
            dp[i][1] = i; // i개 중 1개를 고르는 경우
            dp[i][0] = 1; // i개 중 0개를 고르는 경우
        }

        for (int i = 2; i <= N; i++) {
            for (int j = 2; j <= K; j++) {
                dp[i][j] = (dp[i - 1][j] + dp[i - 2][j - 1]) % MOD;
            }
        }

        int result = (dp[N - 1][K] + dp[N - 3][K - 1]) % MOD;

        System.out.println(result);
    }
}