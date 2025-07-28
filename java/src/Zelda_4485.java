import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;



public class Zelda_4485 {
    static class Node implements Comparable<Node>{

        int x;
        int y;
        int distance;
        public Node(int x, int y, int distance) {
            this.x = x;
            this.y = y;
            this.distance = distance;
        }
        @Override
        public int compareTo(Node o) {
            return this.distance - o.distance;
        }
    }

    static final int[] dx = new int[]{0, 1, 0, -1};
    static final int[] dy = new int[]{1, 0, -1, 0};

    static int findDistance(BufferedReader br, int N) throws Exception{
        PriorityQueue<Node> pq = new PriorityQueue<>();
        int[][] board = new int[N][N];
        int[][] dp = new int[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                dp[i][j] = Integer.MAX_VALUE;
            }
        }

        //do bfs
        pq.add(new Node(0, 0, board[0][0]));
        while(!pq.isEmpty()){
            Node status = pq.poll();
            if(status.x == N - 1 && status.y == N - 1){
                return status.distance;
            }

            for (int d = 0; d < 4; d++) {
                int nx =  status.x + dx[d];
                int ny =  status.y + dy[d];

                if(nx >= 0 && ny >= 0 && nx < N && ny < N){
                    if(dp[nx][ny] > board[nx][ny] + status.distance){
                        dp[nx][ny] =  status.distance + board[nx][ny];
                        pq.add(new Node(nx, ny, dp[nx][ny]));
                    }
                }
            }
        }
        return -1;
    }
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int problemNo = 0;

        while(N != 0){
            problemNo ++;
            System.out.println(String.format("Problem %d: %d",  problemNo, findDistance(br, N)));
            N = Integer.parseInt(br.readLine());
        }
    }
}
