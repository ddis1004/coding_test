import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;

public class TicTacToe_7682 {
    static HashSet<String> set = new HashSet<>();
    public static boolean finished(char[][] board){
        //horizontal
        for (int i = 0; i < 3; i++) {
            char x = board[i][0];
            int sameCount = 0;
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == x) sameCount++;
            }
            if(sameCount == 3 && x != '.') return true;
        }
        //vertical
        for (int i = 0; i < 3; i++) {
            char x = board[0][i];
            int sameCount = 0;
            for (int j = 0; j < 3; j++) {
                if (board[j][i] == x) sameCount++;
            }
            if(sameCount == 3 && x != '.') return true;
        }
        char x = board[0][0];
        int sameCount = 0;
        for (int i = 0; i < 3; i++) {
            if(board[i][i] == x) sameCount++;
        }
        if(sameCount == 3 && x != '.') return true;

        x = board[0][2];
        sameCount = 0;
        for (int i = 0; i < 3; i++) {
            if(board[i][2 - i] == x) sameCount++;
        }
        if(sameCount == 3 && x != '.') return true;

        return false;
    }
    public static void addBoard(char[][] board){
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                sb.append(board[i][j]);
            }
        }
        set.add(sb.toString());
    }
    public static void dfs(char[][] board, int depth){
        if(finished(board) || depth == 9){
            addBoard(board);
            return;
        }
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if(board[i][j] != '.') continue;
                board[i][j] = depth % 2 == 0 ? 'X' : 'O';
                dfs(board, depth + 1);
                board[i][j] = '.';
            }
        }
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        char[][] emptyBoard = {{'.', '.', '.'}, {'.', '.', '.'}, {'.', '.', '.'}};
        dfs(emptyBoard, 0);

        while(!line.equals("end")){
            char[][] board = new char[3][3];
            int xCount = 0;
            int oCount = 0;
            for(int i = 0; i < 3; i++){
                for (int j = 0; j < 3; j++) {
                    char c = line.charAt(3 * i + j);
                    if(c =='X') xCount++;
                    if(c =='O') oCount++;
                    board[i][j] = c;
                }
            }
            if(xCount < oCount || xCount - oCount > 1){
                System.out.println("invalid");
                line = br.readLine();
                continue;
            }
            if(set.contains(line)){
                System.out.println("valid");
                line = br.readLine();
                continue;
            }
            System.out.println("invalid");
            line = br.readLine();
        }
    }
}
