import java.util.*;
import java.lang.*;
import java.io.*;

class PuangInWorkingHell_Large_25584 {
    static int N ;
    static HashMap<String, Integer> map = new HashMap<>();

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        int[] times = {4, 6, 4, 10};
        for(int i = 0; i < N; i ++ ){
            for(int j = 0; j < 4; j++){
                StringTokenizer st = new StringTokenizer(br.readLine());
                for(int k = 0; k < 7; k ++){
                    String name = st.nextToken();
                    if(name.equals("-")) continue;
                    if(map.containsKey(name)){
                        map.put(name, map.get(name) + times[j]);
                    } else {
                        map.put(name, times[j]);
                    }
                }
            }
        }
        Collection<Integer> values = map.values();
        int min = Integer.MAX_VALUE;
        int max = 0;
        for (int v : values) {
            min = Math.min(min, v);
            max = Math.max(max, v);
        }

        if(max - min > 12) System.out.println("No");
         else System.out.println("Yes");
        
    }
}
