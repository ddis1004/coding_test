import java.util.*;
import java.lang.*;
import java.io.*;

class Exchange_1039 {
    
    static int N, K;
    static HashSet<String> set = new HashSet<>();

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        int answer = -1;
        
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{0, N});
        int swapCount = 0;

        while(!queue.isEmpty()){
            int[] status = queue.poll();
            int time = status[0];
            Integer num = status[1];
            // System.out.println(num);
            if(time == K){answer = Math.max(answer, num); continue;}
            if(time > K) break;
            for(int i = 0; i < num.toString().length() - 1; i ++ ){
                for(int j = i + 1; j < num.toString().length(); j ++){
                    char[] numString = num.toString().toCharArray();
                    if(i == 0 && numString[j] == '0') continue;
                    swapCount ++;
                    char temp = numString[i];
                    numString[i] = numString[j];
                    numString[j] = temp;
                    // System.out.println(i + ","  + j);
                    // System.out.println(new String(numString));
                    String setv = (time + 1) + new String(numString);
                    if(!set.contains(setv)){
                        set.add(setv);
                        queue.offer(new int[]{time + 1, Integer.parseInt(new String(numString))});
                    }
                }
            }
            
        }
        if(swapCount <= 0){
            System.out.println(-1);
        } else {
            System.out.println(answer);
        }
        
    }
}
