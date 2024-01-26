import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class ScoreCalculation_2506 {
    public static void main(String[]args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer tokenizer = new StringTokenizer(br.readLine());

        int success = 0;
        int score = 0;

        for (int i = 0; i < N; i++){
            int k = Integer.parseInt(tokenizer.nextToken());
            if (k == 1) {
                score += success += 1;
            }else{
                success = 0;
            }
        }
        System.out.println(score);
    }
}

