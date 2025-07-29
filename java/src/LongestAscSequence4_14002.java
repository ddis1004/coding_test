import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class LongestAscSequence4_14002 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] sequence = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            sequence[i] = Integer.parseInt(st.nextToken());
        }

        int[] dpPrev = new int[N];
        int[] dpDepth = new int[N];
        int answerLength = 1;
        int answerLast = 0;
        StringBuilder sb = new StringBuilder();

        dpPrev[0] = -1;
        dpDepth[0] = 1;

        for (int i = 1; i < N; i++) {
            int maxDepth = 0;
            int maxPrev = -1;
            for (int j = 0; j < i; j++) {
                if(sequence[i] > sequence[j] && maxDepth <= dpDepth[j]){
                    maxDepth = dpDepth[j] + 1;
                    maxPrev = j;
                }
            }
            if(maxPrev == -1){
                dpDepth[i] = 1;
                dpPrev[i] = -1;
            } else {
                dpDepth[i] = maxDepth;
                dpPrev[i] = maxPrev;
            }
            if(answerLength < dpDepth[i]){
                answerLength = dpDepth[i];
                answerLast = i;
            }
        }

        while(answerLast >= 0){
            sb.insert(0, " ");
            sb.insert(0, sequence[answerLast]);
            answerLast = dpPrev[answerLast];
        }

        System.out.println(answerLength);
        System.out.println(sb.toString());
    }
}
