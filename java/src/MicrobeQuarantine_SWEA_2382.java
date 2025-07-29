import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class MicrobeQuarantine_SWEA_2382 {

    static final int[] dx = {-1, 1, 0, 0};
    static final int[] dy = {0, 0, -1, 1};

    static class Microbe{
        public int n;
        public int d;
        Microbe(int n, int d){
            this.n = n;
            this.d = d;
        }
        public void reverseDirection(){
            if(d == 0) d = 1;
            else if(d == 1) d = 0;
            else if(d == 2) d = 3;
            else if(d == 3) d = 2;
        }
    }

    static ArrayList<Microbe>[][] simulate(ArrayList<Microbe>[][] board){
        //create new_board
        ArrayList<Microbe>[][] newBoard =  new ArrayList[board.length][board[0].length];
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board.length; j++) {
                newBoard[i][j] = new ArrayList<Microbe>();
            }
        }
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board.length; j++) {
                //check board, move to new board
                if(board[i][j] == null || board[i][j].isEmpty()) continue;
                for(Microbe microbe : board[i][j]){
                    int nx = i + dx[microbe.d], ny = j + dy[microbe.d];
                    newBoard[nx][ny].add(microbe);
                }
            }
        }

        //check new_board,
        //edge check!
        for (int i = 0; i < newBoard.length; i++) {
            for(Microbe microbe : newBoard[i][0]){
                microbe.n = microbe.n / 2;
                microbe.reverseDirection();
            }
        }
        for (int i = 0; i < newBoard.length; i++) {
            for(Microbe microbe : newBoard[i][newBoard.length - 1 ]){
                microbe.n = microbe.n / 2;
                microbe.reverseDirection();
            }
        }

        for (int i = 1; i < newBoard.length - 1; i++) {
            for(Microbe microbe : newBoard[0][i]){
                microbe.n = microbe.n / 2;
                microbe.reverseDirection();
            }
            for(Microbe microbe : newBoard[newBoard.length - 1][i]){
                microbe.n = microbe.n / 2;
                microbe.reverseDirection();
            }
        }


        for (int i = 0; i < newBoard.length; i++) {
            for (int j = 0; j < newBoard.length; j++) {
                //if multiple Microbe, collision.
                if(newBoard[i][j].size() <= 1) continue;
                int nSum = 0;
                int maxN = 0;
                int maxD = -1;

                for(Microbe microbe : newBoard[i][j]){
                    //sum up n
                    nSum+= microbe.n;
                    if(microbe.n > maxN){   //find max direction
                        maxN = microbe.n;
                        maxD = microbe.d;
                    }
                }
                //replace arraylist with combined Microbe
                newBoard[i][j] = new ArrayList<Microbe>();
                newBoard[i][j].add(new Microbe(nSum, maxD));
            }
        }

        return newBoard;
    }

    public static void main(String[] args) throws Exception{
        System.setIn(new FileInputStream("sample_input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T =  Integer.parseInt(br.readLine());
        StringBuilder answers = new StringBuilder();

        for (int t = 0; t < T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N =  Integer.parseInt(st.nextToken());
            int M =  Integer.parseInt(st.nextToken());
            int K =  Integer.parseInt(st.nextToken());

            ArrayList<Microbe> board[][] = new ArrayList[N][N];

            for (int k = 0; k < K; k++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                int n = Integer.parseInt(st.nextToken());
                int d = Integer.parseInt(st.nextToken()) - 1;

                board[x][y] = new ArrayList<>();
                board[x][y].add(new Microbe(n, d));
            }


            for (int time = 0; time < M; time++) {
                board = simulate(board);
            }
            int answer = 0;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if(board[i][j] == null || board[i][j].isEmpty()) continue;
                    answer += board[i][j].get(0).n;
                }
            }
            answers.append(String.format("#%d %d\n", t + 1, answer));
        }
        System.out.println(answers.toString());
    }
}
