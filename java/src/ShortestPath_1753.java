import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Node implements Comparable<Node>{
    int v, w;
    public Node(int v, int w){
        this.v = v;
        this.w = w;
    }

    @Override
    public int compareTo(Node n) {
        return this.w - n.w;
    }
}

public class ShortestPath_1753 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int V = Integer.parseInt(st.nextToken()), E = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(br.readLine());
        ArrayList<Node>[] list = new ArrayList[V + 1];

        boolean[] visited = new boolean[V + 1];

        int[] distances = new int[V+1];
        for (int i = 0; i < V+1; i++) {
            distances[i] = Integer.MAX_VALUE;
            list[i] = new ArrayList<Node>();
        }
        distances[K] = 0;

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            list[u].add(new Node(v, w));
        }

        PriorityQueue<Node> queue = new PriorityQueue<>();
        queue.offer(new Node(K, 0));
        while(!queue.isEmpty()){
            Node now = queue.poll();
            if (distances[now.v] < now.w) {
                continue;
            }
            for(Node node: list[now.v]){
                if(distances[now.v] + node.w < distances[node.v]){
                    distances[node.v] = distances[now.v] + node.w;
                    queue.offer(new Node(node.v, distances[node.v]));
                }
            }
        }
        for (int i = 1; i < V + 1; i++) {
            if(distances[i] == Integer.MAX_VALUE) System.out.println("INF");
            else System.out.println(distances[i]);
        }
    }
}
