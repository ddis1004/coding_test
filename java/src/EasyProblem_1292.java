import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class EasyProblem_1292{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        int finder = 1;
        int number = 0;
        int sum = 0;

        int Bto1 = 0;
        int Ato1 = 0;

        //1 22 333 444 55555
        while(finder <= A){
            Ato1 += number * number;
            Bto1 += number * number;
            finder += number += 1;
        }

        Ato1 += (number) * (number - (finder - A));

        while(finder <= B){
            Bto1 += number * number;
            finder += number += 1;
        }
        Bto1 += (number) * (number - (finder - B)) + number;

        System.out.println(Bto1 - Ato1);
    }
}