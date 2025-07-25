import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Party_1238 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()), M = Integer.parseInt(st.nextToken()), X = Integer.parseInt(st.nextToken());

        int[][] minDistances = new int[N][N];
        int[][] edges = new int[M][3];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                minDistances[i][j] = Integer.MAX_VALUE;
            }
        }
        minDistances[0][0] = 0;

        for (int i = 0; i < M; i++) {
            int start = Integer.parseInt(st.nextToken()), end = Integer.parseInt(st.nextToken()), cost= Integer.parseInt(st.nextToken());
            edges[M][0] = start;
            edges[M][1] = end;
            edges[M][2] = cost;
        }



    }

}
