import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class RGBStreet_17404 {
    public static void main(String[] args)  throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] costs = new int[3][N + 1];
        int[][] dp = new int[3][N + 1];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 3; j++) {
                costs[j][i] = Integer.parseInt(st.nextToken());
            }
        }

        int answer = Integer.MAX_VALUE;

        for (int c = 0; c < 3; c++) {
            for (int i = 0; i < 3; i++) {
                if(i == c) dp[i][0] = costs[i][0];
                else dp[i][0] = 1001;
            }

            for (int i = 1; i < N; i++) {
                for (int j = 0; j < 3; j++) {
                    int min = Integer.MAX_VALUE;
                    for (int k = 0; k < 3; k++) {
                        if(k == j) continue;
                        min = Math.min(min, dp[k][i - 1] + costs[j][i]);
                    }
                    dp[j][i] = min;
                }
            }

            for (int i = 0; i < 3; i++) {
                if(c == i) continue;
                answer = Math.min(answer, dp[i][N - 1]);
            }
        }

        System.out.println(answer);

    }
}
