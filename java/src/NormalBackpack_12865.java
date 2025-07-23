import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


class NormalBackpack_12865{

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader( new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] weights = new int[N];
        int[] values = new int[N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            weights[i] = Integer.parseInt(st2.nextToken());
            values[i] = Integer.parseInt(st2.nextToken());
        }

        int[][] dp = new int[N + 1][K + 1];

        for (int i = 1; i < N + 1; i++) {
            for (int j = 0; j < K + 1; j++) {
                if(weights[i - 1] >j){
                    dp[i][j] = dp[i - 1][j];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1]);
                }
            }
        }
        System.out.println(dp[N][K]);
    }
}