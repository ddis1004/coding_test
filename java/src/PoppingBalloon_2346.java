import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class PoppingBalloon_2346 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer tokenizer = new StringTokenizer(br.readLine());

        ArrayList<Integer> index = new ArrayList<Integer>();
        ArrayList<Integer> next = new ArrayList<Integer>();

        for(int i = 0; i < N; i++){
            index.add(i + 1);
            next.add(Integer.parseInt(tokenizer.nextToken()));
        }

        int current = 0;

        while(!index.isEmpty()){
            //print
            System.out.print(index.get(current) + " ");
            //remove
            int nexti = next.get(current);
            index.remove(current);
            next.remove(current);
            //go ( - 1 )
            if(nexti > 0)
                current += nexti - 1;
            else
                current += nexti;
            if(index.size() == 0)
                break;
            current = current % index.size();
            if(current < 0)
                current += index.size();
        }

    }
}
