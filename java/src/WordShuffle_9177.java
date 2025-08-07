import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;

public class WordShuffle_9177 {
    static HashSet<String> set = new HashSet<>();
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringBuffer sb = new StringBuffer();
        for(int i = 0; i < N; i ++){
            set.clear();
            StringTokenizer st = new StringTokenizer(br.readLine());
            String word1 = st.nextToken();
            String word2 = st.nextToken();
            String word3 = st.nextToken();

            ArrayDeque<int[]> queue = new ArrayDeque<>();
            queue.add(new int[] {0, 0, 0});
            set.add(Arrays.toString(new int[] {0, 0, 0}));
            boolean answer = false;
            while(!queue.isEmpty()){
                int[] idxs = queue.poll();
                int i1 = idxs[0], i2 = idxs[1], i3 = idxs[2];
                if(i1 < word1.length() && word1.charAt(i1) == word3.charAt(i3)){
                    int[] state = new int[] {i1 + 1, i2, i3 + 1};
                    if(!set.contains(Arrays.toString(state))){
                        queue.add(state);
                        set.add(Arrays.toString(state));
                    }
                }
                if(i2 < word2.length() && word2.charAt(i2) == word3.charAt(i3)){
                    int[] state = new int[]{i1, i2 + 1, i3 + 1};
                    if(!set.contains(Arrays.toString(state))) {
                        queue.add(state);
                        set.add(Arrays.toString(state));
                    }
                }
                if(i3 == word3.length()){
                    answer = true;
                    break;
                }
            }
            sb.append(String.format("Data set %d: %s\n", i + 1, answer?"yes":"no"));
        }
        System.out.println(sb);
    }
}
