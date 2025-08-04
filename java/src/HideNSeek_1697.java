import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class HideNSeek_1697 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        boolean[] visited = new boolean[Math.max(N, K) * 2];

        ArrayDeque<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{0, N});
        while(!queue.isEmpty()){
            int[] status = queue.poll();
            //System.out.println(Arrays.toString(status));
            if(status[1] == K){
                System.out.println(status[0]);
                return;
            }

            if(status[1] - 1 >= 0 && !visited[status[1] - 1]){
                visited[status[1] - 1] = true;
                queue.offer(new int[]{status[0] + 1, status[1] - 1});
            }
            if(status[1] + 1 < visited.length && !visited[status[1] + 1]){
                visited[status[1] + 1] = true;
                queue.offer(new int[]{status[0] + 1, status[1] + 1});
            }
            if(status[1] * 2 < visited.length && !visited[status[1] * 2]){
                visited[status[1] * 2] = true;
                queue.offer(new int[]{status[0] + 1, status[1] * 2});
            }
        }
    }
}
