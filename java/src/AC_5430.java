import java.io.*;
import java.util.*;

public class AC_5430 {

    private static String calculate(String operations, int[] sequence){
        int x = 0, y = sequence.length;
        boolean reversed = false;

        for(int i = 0; i < operations.length(); i ++){
            if(operations.charAt(i) == 'R'){
                reversed = !reversed;
            } else if (operations.charAt(i) == 'D'){
                if(reversed) y --;
                else x++;
                if(y < x) {
                    return "error";
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        sb.append('[');
        if(reversed){
            for(int i = y - 1; i >= x; i --){
                sb.append(sequence[i]);
                if(i != x) sb.append(',');
            }
        } else {
            for(int i = x; i < y; i ++){
                sb.append(sequence[i]);
                if(i != y - 1) sb.append(',');
            }
        }
        sb.append(']');
        return sb.toString();
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder answer = new StringBuilder();

        for(int t = 0; t < T; t++){
            String operations = br.readLine();
            int length = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine(), ",[] ");

            int[] sequence = new int[length];

            for(int i =0; i < length; i ++){
                sequence[i] = Integer.parseInt(st.nextToken());
            }
            answer.append(calculate(operations, sequence));
            answer.append('\n');
        }
        System.out.println(answer);
    }
}
