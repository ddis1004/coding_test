import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;

public class MovingMaze_16594 {
    private static int[] dx = new int[]{0, 0, 1, 1, -1, -1, 1, -1, 0};
    private static int[] dy = new int[]{1, -1, 1, -1, 1, -1, 0, 0, 0};

    static ArrayList<int[]> walls = new ArrayList<int[]>();
    static boolean isWall(int x, int y, int time){
        for (int[] wall : walls) {
            if (y == wall[1] && x == wall[0] + time)
                return true;
        }
        return false;
    }
    
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        boolean[][][] visited = new boolean[9][8][8];
        Deque<int[]> queue = new ArrayDeque<int[]>();

        for (int i = 0; i < 8; i++) {
            String line =br.readLine();
            for (int j = 0; j < 8; j++) {
                if(line.charAt(j) == '#') walls.add(new int[]{i, j});
            }
        }

        queue.push(new int[]{7, 0, 0}); //x, y, time;

        while(!queue.isEmpty()){
            int[] status = queue.poll();

            for (int d = 0; d < 9; d++) {
                int nx = status[0] + dx[d];
                int ny = status[1] + dy[d];

                if(nx >= 0 && nx < 8 && ny >= 0 && ny < 8 && ! visited[Math.min(status[2] + 1, 8)][nx][ny] &&
                        !isWall(nx, ny, status[2]) && !isWall(nx, ny, status[2] + 1)){
                    visited[Math.min(status[2] + 1, 8)][nx][ny] = true;
                    if(nx == 0 && ny == 7){
                        System.out.println(1);
                        return;
                    }
                    queue.push(new int[]{nx, ny, status[2] + 1});
                }
            }
        }
        System.out.println(0);
    }
}
