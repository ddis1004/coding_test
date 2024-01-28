import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class FactorialBreakdown_2057 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long N = Long.parseLong(st.nextToken());

        ArrayList<Long> factorials  = new ArrayList<Long>();

        factorials.add((long)1);
        long last = 1;
        long i = 1;
        while(last * i <= N){
            factorials.add(last * i);
            last *= i;
            //System.out.println(last);
            i++;
        }

        long K = N;
        int j = factorials.size() - 1;

        if(N == 0)
            System.out.println("NO");
        else{
            while(K >= 0){
                if(K == 0) {
                    System.out.println("YES");
                    break;
                }
                if(j < 0){
                    if(K == 0){
                        System.out.println("YES");
                        break;
                    }
                    else{
                        System.out.println("NO");
                        break;
                    }
                }
                if(K >= factorials.get(j)){
                    K -= factorials.get(j);
                }
                j -= 1;
                //System.out.println("K = " + K + " j = " + j);
            }
        }


    }
}
