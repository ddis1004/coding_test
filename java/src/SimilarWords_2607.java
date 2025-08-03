import java.io.BufferedReader;
import java.io.InputStreamReader;

public class SimilarWords_2607 {
    static int[] count;
    public static int compositionDiff(String word){
        int ans = 0;
        int[] newCount = new int[26];
        for(int i = 0; i < word.length(); i++){
            int idx = word.charAt(i) - 'A';
            newCount[idx] ++;
        }
        for(int i = 0; i < 26; i++) {
            ans += Math.abs(newCount[i] - count[i]);
        }
        return ans;
    }
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int answer = 0;

        String word = br.readLine();

        count = new int[26];
        for(int i = 0; i < word.length(); i++){
            int idx = word.charAt(i) - 'A';
            count[idx] ++;
        }
        for(int i = 0; i < N - 1; i ++){
            String newWord = br.readLine();
            int diff = compositionDiff(newWord);
            if(diff == 0 ||
                    (Math.abs(newWord.length() - word.length()) == 1 && diff == 1) ||
                    (Math.abs(newWord.length() - word.length()) == 0 && diff == 2)){
                answer ++;
            }
        }
        System.out.println(answer);

    }
}
