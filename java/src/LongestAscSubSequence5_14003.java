import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class LongestAscSubSequence5_14003 {
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
        ArrayList<Integer> minPerDepth = new ArrayList<Integer>();
        int[] minPrev = new int[N];

        for (int i = 0; i < N; i++) {
            int pos = Collections.binarySearch(minPerDepth, sequence[i]);
            if(pos < 0)
                pos = -(pos + 1);
            if(pos == minPerDepth.size()){
                minPerDepth.add(sequence[i]);
                minPrev[pos] = i;
            } else {
                if(sequence[i] < minPerDepth.get(pos)) {
                    minPrev[pos] = i;
                }
                minPerDepth.set(pos, Math.min(sequence[i], minPerDepth.get(pos)));
            }
            dpDepth[i] = pos;

            if (pos < 0) {
                pos = -(pos + 1);  // 실제 삽입 위치 계산
            }
            else {
                if(pos == 0){
                    dpPrev[i] = -1;
                } else {
                    dpPrev[i] = minPrev[pos - 1];
                    //for (int j = i - 1; j >= 0; j--) {
                    //    if (dpDepth[j] == pos - 1 && sequence[j] < sequence[i]) {
                    //        dpPrev[i] = j;
                    //        break;
                    //    }
                    //}
                }

            }
        }
        int answerLength = minPerDepth.size();
        System.out.println(answerLength);

        ArrayList<Integer> result = new ArrayList<>();
        int answerLast = -1;

        for (int i = N - 1; i >= 0; i--) {
            if (dpDepth[i] == answerLength - 1) {
                answerLast = i;
                break;
            }
        }

        while (answerLast != -1) {
            result.add(sequence[answerLast]);
            answerLast = dpPrev[answerLast];
        }
        Collections.reverse(result);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.size(); i++) {
            if (i > 0) sb.append(" ");
            sb.append(result.get(i));
        }
        System.out.println(sb.toString());

    }
}
