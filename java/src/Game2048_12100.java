import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

class State{
    public State(int[][] board, int time){
        this.board = board;
        this.time = time;
    }
    public int[][] board;
    public int time;
}

class Game2048_12100 {

    private static int[][] move(int[][] board, int d){
        int N = board.length;
        int[][] newBoard = new int[N][N];
        int prev = 0;
        int blockCount = 0;
        int sameCount = 0;

        if(d >= 2){ //horizontal
            for (int i = 0; i < N; i++) {
                int j = d % 2 == 0 ? 0 : N - 1;
                while(j >= 0 && j < N){
                    if(board[i][j] == 0){
                        j += d % 2 == 0 ? 1 : -1;
                        continue;
                    } else if(board[i][j] == prev){
                        newBoard[i][d % 2 == 0 ? blockCount: N - 1 - blockCount] = prev * 2;
                        prev = 0;
                        blockCount++;
                    } else if(prev != 0){
                        newBoard[i][d % 2 == 0 ? blockCount: N - 1 - blockCount] = prev;
                        blockCount++;
                        prev = board[i][j];
                    } else {
                        prev = board[i][j];
                    }
                    j += d % 2 == 0 ? 1 : -1;
                }
                if(prev != 0){
                    newBoard[i][d % 2 == 0 ? blockCount: N - 1 - blockCount] = prev;
                    prev = 0;
                }
                blockCount = 0;
            }
        } else { //vertical
            for (int j = 0; j < N; j++) {
                int i = d % 2 == 0 ? 0 : N - 1;
                while(i >= 0 && i < N){
                    if(board[i][j] == 0){
                        i += d % 2 == 0 ? 1 : -1;
                        continue;
                    } else if (board[i][j] == prev){
                        newBoard[d % 2 == 0 ? blockCount: N - 1 - blockCount][j] = prev * 2;
                        prev = 0;
                        blockCount++;
                    } else if( prev != 0){
                        newBoard[d % 2 == 0 ? blockCount: N - 1 - blockCount][j] = prev;
                        blockCount++;
                        prev = board[i][j];
                    } else {
                        prev = board[i][j];
                    }
                    i += d % 2 == 0 ? 1 : -1;
                }
                if(prev != 0){
                    newBoard[d % 2 == 0 ? blockCount: N - 1 - blockCount][j] = prev;
                    prev = 0;
                }
                blockCount = 0;
            }
        }
        return newBoard;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        int N = Integer.parseInt(br.readLine());
        int[][] board = new int[N][N];

        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            StringTokenizer st = new StringTokenizer(str);
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        Deque<State> queue= new ArrayDeque<State>();
        queue.offer(new State(board, 0));
        int maxScore = 0;
        while(!queue.isEmpty()){
            State state = queue.poll();
            if(state.time == 5){
                int max = 0;
                for (int i = 0; i < N; i++) {
                    for (int j = 0; j < N; j++) {
                        max = Math.max(max, state.board[i][j]);
                    }
                }
                maxScore = Math.max(maxScore, max);
            } else {
                for (int d = 0; d < 4; d++) {
                    int[][] newBoard = move(state.board, d);
                    queue.offer(new State(newBoard, state.time + 1));
                }
            }
        }
        System.out.println(maxScore);

    }
}