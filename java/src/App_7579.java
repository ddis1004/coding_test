import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class App_7579 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] memories = new int[N];
        int[] costs = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            memories[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            costs[i] = Integer.parseInt(st.nextToken());
        }

        int MAX_COST_SUM = 100 * N + 1;
        int[][] dp = new int[N + 1][MAX_COST_SUM]; // i번째 앱까지 고려시, j cost내에서 달성가능한 최대 메모리
        int answer = MAX_COST_SUM;
        for (int i = 1; i < N + 1; i++) {
            for (int j = 0; j < MAX_COST_SUM; j++) {
                if(costs[i - 1] > j){
                    dp[i][j] = dp[i - 1][j];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - costs[i - 1]] + memories[i - 1]);
                }
                if(dp[i][j] >= M)
                    answer = Math.min(j, answer);
            }
        }
        System.out.println(answer);
    }
}
