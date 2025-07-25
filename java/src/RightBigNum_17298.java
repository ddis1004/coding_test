import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class RightBigNum_17298 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Deque<int []> stack = new ArrayDeque<int[]>();

        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] nge = new int[N];

        stack.push(new int[]{0,Integer.parseInt(st.nextToken())}); //index, num
        nge[0] = -1;

        for (int i = 1; i < N; i++) {
            int seq = Integer.parseInt(st.nextToken());
            while(!stack.isEmpty() && stack.peek()[1] < seq){
                int[] num = stack.pop();
                nge[num[0]] = seq;
            }
            stack.push(new int[]{i, seq});
            nge[i] = -1;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            sb.append(nge[i]).append(' ');
        }
        System.out.println(sb);
    }
}
