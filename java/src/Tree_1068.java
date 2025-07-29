import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Tree_1068 {
    private static int countLeaf(ArrayList<Integer>[] tree, int start, int del){
        if(start == del){
            return 0;
        }
        if(!tree[start].isEmpty()){
            int sum = 0;
            int leafCount = 0;
            for (int i = 0; i < tree[start].size(); i++) {
                if(tree[start].get(i) == del) continue;
                sum += countLeaf(tree, tree[start].get(i), del);
                leafCount++;
            }
            if(leafCount == 0)
                return 1;
            else
                return sum;
        } else {
            return 1;
        }
    }
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] parents = new int[N];
        ArrayList<Integer>[] tree = new ArrayList[N];

        for (int i = 0; i < N; i++) {
            tree[i] = new ArrayList<Integer>();
        }

        int start = -1;
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int parent = Integer.parseInt(st.nextToken());
            if(parent == -1) {
                start = i;
                continue;
            }
            tree[parent].add(i);
        }

        int del = Integer.parseInt(br.readLine());
        System.out.println(countLeaf(tree, start, del));


    }
}
