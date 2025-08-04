import java.util.*;
import java.lang.*;
import java.io.*;

class CardShuffle_1091 {
    static HashSet<String> set = new HashSet<>();
    static int[] result;
    static int[] shuffleOrder;
    static int N;

    public static int[] shuffle(int[] deck){
        int[] newDeck = new int[N];
        for(int i = 0; i < N; i ++){
            newDeck[shuffleOrder[i]] = deck[i];
        }
        return newDeck;
    }

    public static boolean isAnswer(int[] deck){
        for(int i = 0; i < deck.length; i ++){
            if(i % 3 != result[deck[i]]) return false;
        }
        return true;
    }
    
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        int answer = 0;
        result = new int[N];
        shuffleOrder = new int[N];
        int[] deck = new int[N];
        int time = 0;

        StringTokenizer st = new StringTokenizer(br.readLine());
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i ++) {
            result[i] = Integer.parseInt(st.nextToken());
            shuffleOrder[i] = Integer.parseInt(st2.nextToken());
            deck[i] = i;
        }

        if(isAnswer(deck)){
            System.out.println(0);
            return;
        }

        while(true){
            int[] newDeck = shuffle(deck);
            time ++;
            String stringDeck = Arrays.toString(newDeck);
            System.out.println(stringDeck);
            if(isAnswer(newDeck)){
                System.out.println(time);
                return;
            }
            if(set.contains(stringDeck)){
                System.out.println(-1);
                return;
            }
            set.add(stringDeck);
            deck = newDeck;
        }
        
    }
}
