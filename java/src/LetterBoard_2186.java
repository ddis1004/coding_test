import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class LetterBoard_2186 {
    static final int[] dx = new int[]{1, 0, -1, 0};
    static final int[] dy = new int[]{0, 1, 0, -1};

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()), M = Integer.parseInt(st.nextToken()), K = Integer.parseInt(st.nextToken());
        char[][] letterBoard = new char[N][M];

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                letterBoard[i][j] = line.charAt(j);
            }
        }
        String word = br.readLine();
        int wordLen = word.length();
        int[][][] dp = new int[N][M][word.length()];
        Queue<int[]> q = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if(word.charAt(0) == letterBoard[i][j])
                    dp[i][j][0] = 1;
            }
        }

        for (int w = 0; w < wordLen - 1; w++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if(dp[i][j][w] == 0) continue;
                    for (int d = 0; d < 4; d++) {
                        for (int k = 1; k < K + 1; k++) {
                            int nx =  i + dx[d] * k, ny = j + dy[d] * k;
                            if(nx >= 0 && nx < N && ny >= 0 && ny < M &&
                                    letterBoard[nx][ny] == word.charAt(w + 1)) {
                                dp[nx][ny][w + 1] += dp[i][j][w];
                            }
                        }
                    }
                }
            }
        }
        int answer = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                answer += dp[i][j][wordLen - 1];
            }
        }

        System.out.println(answer);
        br.close();
    }
}
