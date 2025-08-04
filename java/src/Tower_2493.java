import java.util.*;
import java.lang.*;
import java.io.*;

class Tower_2493 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] towers = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++){
            towers[i] = Integer.parseInt(st.nextToken());
        }
        ArrayDeque<int[]> stack = new ArrayDeque<>();
        stack.addLast(new int[]{N - 1, towers[N - 1]});
        int[] answer = new int[N];

        for(int i = N - 2; i >= 0; i--){
            while( !stack.isEmpty() && towers[i] >= stack.peekLast()[1]){
                int[] sender = stack.pollLast();
                answer[sender[0]] = i + 1;
            }
            stack.addLast(new int[]{i, towers[i]});
        }

        while(!stack.isEmpty()){
            int[] sender = stack.pollLast();
            answer[sender[0]] = 0;
        }
        StringBuffer sb = new StringBuffer();
        for (int ans : answer) {
            sb.append(ans);
            sb.append(" ");
        }
        System.out.println(sb);
    }
}
