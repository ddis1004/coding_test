import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Prerequisite_14567 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()), M = Integer.parseInt(st.nextToken());
        ArrayList[] required = new ArrayList[N + 1];
        int[] inCount = new int[N + 1];
        int[] distance = new int[N + 1];

        Queue<Integer> q = new ArrayDeque<>();
        for(int i = 0; i < N + 1; i++){
            required[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int pre = Integer.parseInt(st.nextToken()), post = Integer.parseInt(st.nextToken());
            required[pre].add(post);
            inCount[post]++;
        }

        for (int i = 1; i < N; i++) {
            if (inCount[i] == 0) {
                q.add(i);
                distance[i] = 0;
            }
        }

        while(!q.isEmpty())  {
            int pre = q.poll();
            for (int i = 0; i < required[pre].size(); i++) {
                int post = (Integer) required[pre].get(i);
                distance[post] = Math.max(distance[post], distance[pre] + 1);
                if(--inCount[post] == 0){
                    q.offer(post);
                }
            }
        }

        for (int i = 1; i < N + 1; i++) {
            System.out.printf(distance[i] + 1 + " ");
        }

    }
}
