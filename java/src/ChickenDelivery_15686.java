import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class ChickenDelivery_15686 {

    static int minDistance(int cnt, int R, int start, int[][] distances, int[] b){
        if(cnt == R){
            int sum = 0;
            for (int i = 0; i < distances[0].length; i++) {
                int min = Integer.MAX_VALUE;
                for (int j = 0; j < R; j++) {
                    min = Math.min(distances[b[j]][i], min);
                }
                sum += min;
            }
            return sum;
        }
        int min = Integer.MAX_VALUE;
        for (int i = start; i < distances.length; i++) {
            b[cnt] = i;
            min = Math.min(min, minDistance(cnt + 1, R, i + 1, distances, b));
        }
        return min;
    }
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()), M = Integer.parseInt(st.nextToken());
        ArrayList<int[]> cList = new ArrayList<int[]>();
        ArrayList<int[]> hList = new ArrayList<int[]>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int field = Integer.parseInt(st.nextToken());
                if(field == 1) hList.add(new int[]{i , j});
                else if (field == 2) cList.add(new int[]{i , j});
            }
        }
        int[][] distances = new int[cList.size()][hList.size()];
        for (int i = 0; i < cList.size(); i++) {
            for (int j = 0; j < hList.size(); j++) {
                distances[i][j] = Math.abs(cList.get(i)[0] - hList.get(j)[0]) + Math.abs(cList.get(i)[1] - hList.get(j)[1]);
            }
        }
        System.out.println(minDistance(0, M, 0, distances, new int[M]));
    }
}
