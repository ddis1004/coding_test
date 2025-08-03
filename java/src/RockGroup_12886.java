import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class RockGroup_12886 {
    static HashSet<String> set = new HashSet<String>();

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] rocks = new int[3];

        for(int i = 0; i < 3; i ++){
            rocks[i] = Integer.parseInt(st.nextToken());
        }

        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(rocks);
        while(! queue.isEmpty()){
            int[] status = queue.poll();
//            System.out.println(Arrays.toString(status));
            if(status[0] == status[1] && status[1] == status[2]){
                System.out.println(1);
                return;
            }

            for(int i = 0; i < 3; i++){
                for (int j = 0; j < 3; j++) {
                    if(i == j) continue;
                    if(status[i] >= status[j]) continue;
                    int[] newStatus = new int[3];
                    newStatus[0] = status[0];
                    newStatus[1] = status[1];
                    newStatus[2] = status[2];
                    newStatus[j] -= newStatus[i];
                    newStatus[i] *= 2;
                    String stringStatus = Arrays.toString(newStatus);
                    if(!set.contains(stringStatus)){
                        set.add(stringStatus);
                        queue.add(newStatus);
                    }
                }
            }
        }
        System.out.println(0);
    }
}
