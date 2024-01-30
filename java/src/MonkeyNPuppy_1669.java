import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class MonkeyNPuppy_1669 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer = new StringTokenizer(br.readLine());

        int X = Integer.parseInt(tokenizer.nextToken());
        int Y = Integer.parseInt(tokenizer.nextToken());

        int N  = Y - X;

        int a = (int) Math.sqrt(N);

        int asqr = a * a;
        int bsqr = (a + 1) * (a + 1);

        if(N == 0){
            System.out.println(0);
            return;
        }

        if(N == asqr){
            System.out.println(a * 2 - 1);
        }
        else if(asqr + 1 <= N && N <= (bsqr - asqr)/2 + asqr){
            System.out.println(a * 2);
        }
        else{
            System.out.println(a * 2 + 1);
        }

    }

}
