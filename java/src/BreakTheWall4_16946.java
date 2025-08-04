import java.util.*;
import java.lang.*;
import java.io.*;

class BreakTheWall4_16946 {
    
    static int N, M;
    static final int[] dx = {-1, 1, 0, 0};
    static final int[] dy = {0, 0, -1, 1};
    static ArrayList<Integer> sectionArea = new ArrayList<>();
    static int[][] section;
    static int[][] board;

    public static void divideSection(){
        int sectionName = 1;
        sectionArea.add(0);
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        for(int i = 0; i < N; i ++){
            for(int j = 0; j < M ; j++){
                if(section[i][j] != 0 || board[i][j] == 1) continue;
                section[i][j] = sectionName;
                queue.offer(new int[]{i, j});
                int area = 0;
                while(!queue.isEmpty()){
                    int[] coord = queue.poll();
                    area ++;
                    for(int d = 0; d < 4; d++){
                        int nx = dx[d] + coord[0];
                        int ny = dy[d] + coord[1];
                        if(nx >= 0 && nx < N && ny >= 0 && ny < M && board[nx][ny] == 0 && section[nx][ny] == 0){
                            section[nx][ny] = sectionName;
                            queue.offer(new int[]{nx, ny});
                        }
                    }
                }
                sectionArea.add(area);
                sectionName ++;
            }
        }
    }


    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        board = new int[N][M];
        int[][] answer = new int[N][M];
        section = new int[N][M];
        for(int i = 0; i < N; i ++){
            String line = br.readLine();
            for(int j = 0; j < M; j ++){
                board[i][j] = line.charAt(j) - '0';
            }
        }
        divideSection();
        // for (int i = 0; i < N; i ++) {
        //     System.out.println(Arrays.toString(section[i]));
        // }
        // System.out.println(sectionArea.toString());
        HashSet<Integer> set = new HashSet<>();
        StringBuffer sb = new StringBuffer();
        for(int i = 0; i < N; i ++){
            for(int j = 0; j < M; j ++){
                if(board[i][j] == 0) sb.append(0);
                else {
                    int area = 0;
                     for(int d = 0; d < 4; d++){
                        int nx = dx[d] + i;
                        int ny = dy[d] + j;
                        if(nx >= 0 && nx < N && ny >= 0 && ny < M && board[nx][ny] == 0 && section[nx][ny] != 0){
                            if(set.contains(section[nx][ny])) continue;
                            area += sectionArea.get(section[nx][ny]);
                            set.add(section[nx][ny]);
                        }
                    }
                    set.clear();
                    sb.append((area + 1) % 10); // add the wall area itself
                }
            }
            sb.append("\n");
        }
        System.out.println(sb);
        
        

        
    }
}
