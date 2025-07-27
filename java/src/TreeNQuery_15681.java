import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class TreeNQuery_15681 {
    static ArrayList<Integer>[] edges;
    static int[] counts;
    static boolean[] visiting;

    static int countSubTree(int prev, int start){
        int sum = 0;
        for (int i = 0; i < edges[start].size(); i++) {
            int next = edges[start].get(i);
            if(next != prev && !visiting[next]){
                visiting[next] = true;
                sum += countSubTree(start, next);
            }
        }
        return counts[start] = sum + 1;
    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()), R = Integer.parseInt(st.nextToken()), Q = Integer.parseInt(st.nextToken());
        edges = new ArrayList[N];
        visiting = new boolean[N];
        counts = new int[N];

        for (int i = 0; i < N; i++) {
            edges[i] = new ArrayList<Integer>();
        }
        for (int i = 0; i < N - 1; i++){
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken()), v = Integer.parseInt(st.nextToken());
            edges[u - 1].add(v - 1);
            edges[v - 1].add(u - 1);
        }

        visiting[R - 1] = true;
        countSubTree(-1, R - 1);
        for (int i = 0; i < Q; i++) {
            int query = Integer.parseInt(br.readLine());
            System.out.println(counts[query - 1]);
        }

    }
}
