import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Mieral_2933 {
    static int mineralCount = 0;
    static int R = -1, C = -1;
    public int[] simulateThrow(char[][] board, int row, int direction){
        //find mineral to destroy
        int destroyedX = -1, destroyedY = -1;
        for (int i = direction > 0 ? 0 : C - 1; i < C && i >= 0; i += direction) {
            if(board[row][i] == 'x') {
                board[row][i] = '.';
                destroyedX = row;
                destroyedY = i;
                mineralCount--;
                break;
            };
        }
        return new int[] {destroyedX, destroyedY};
    }

    public void simulateDrop(int[][] board, int destroyX, int destroyY){
        // from removed mineral, do bfs, find cluster.
        //store bottom flag
        //store cluster in clusterBoard(int[N][N])
        //if not cluster contains bottom,
        //from bottom, drop cluster.
        //if bottom meets other mineral, stop.
        //check adjacent area while changing cluster loc
        //do this again for combined cluster.
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        char[][] board = new char[R][C];

        for (int i = 0; i < R; i++) {
            String line = br.readLine();
            for (int j = 0; j < C; j++) {
                char c = line.charAt(j);
                if(c == 'x') mineralCount += 1;
                board[i][j] = c;
            }
        }
        int pitchCount = Integer.parseInt(br.readLine());
        int[] pitch = new int[R];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < pitchCount; i++) {
            pitch[i] = Integer.parseInt(st.nextToken());

            //simulateThrow()
                //convert pitch[i] to x index to call simulateThrow
            //if destroyX == -1,
                //continue
            //simulateDrop
        }




    }
}
