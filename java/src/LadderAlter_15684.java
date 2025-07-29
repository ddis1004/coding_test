import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.StringTokenizer;

public class LadderAlter_15684 {
    static boolean[][] ladder;
    static int N, M, H;
    static int minGen = Integer.MAX_VALUE;

    public static boolean canPlace(int row, int col) {
        if(ladder[row][col]) return false;
        if(col > 0 && ladder[row][col - 1]) return false;
        if(col < N - 2 && ladder[row][col + 1]) return false;
        return true;
    }

    public static void dfs(int genCount, int startRow, int startCol){
        if(check()){
            minGen = Math.min(minGen, genCount);
        }
        if(genCount >= 3) return;
        for (int i = startRow; i < H; i++) {
            for (int j = startRow == i? startCol: 0; j < N - 1; j++) {
                if(ladder[i][j]) continue;
                if(canPlace(i, j)) {
                    ladder[i][j] = true;
                    dfs(genCount + 1, i, j + 2);
                    ladder[i][j] = false;
                }

            }
        }
    }
    public static boolean check() {
        for (int i = 0; i < N; i++) {
            int pos = i;
            for (int row = 0; row < H; row++) {
                if (pos < N - 1 && ladder[row][pos]) {
                    pos++;
                } else if (pos > 0 && ladder[row][pos - 1]) {
                    pos--;
                }
            }
            if (pos != i) return false;
        }
        return true;
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        ArrayDeque<int[]> stack = new ArrayDeque<>();
        ladder = new boolean[H][N - 1];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            ladder[x - 1][y - 1] = true;
        }

        dfs(0, 0 , 0);

        if(minGen == Integer.MAX_VALUE){
            System.out.println(-1);
            return;
        }
        System.out.println(minGen);

    }
}
