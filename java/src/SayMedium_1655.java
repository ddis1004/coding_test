import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class SayMedium_1655 {
    //private static int binarySearch(ArrayList<Integer> list, int target){
    //    int left = 0;
    //    int right = list.size();
    //    int medium = (left + right)/2;
    //
    //    while(left < right){
    //        if(list.get(medium) < target){
    //            left = medium + 1;
    //        } else{
    //            right = medium;
    //        }
    //        medium = (left + right)/2;
    //    }
    //    return left;
    //}
    //
    //public static void main(String[] args) throws  Exception{
    //    StringBuilder sb = new StringBuilder();
    //    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    //    int N = Integer.parseInt(br.readLine());
    //    ArrayList<Integer> list = new ArrayList<Integer>();
    //    int first = Integer.parseInt(br.readLine());
    //    list.add(first);
    //    sb.append(String.format("%d\n", first));
    //
    //    for (int i = 0; i < N - 1; i++) {
    //        int n = Integer.parseInt(br.readLine());
    //        int index = binarySearch(list, n);
    //        list.add(index, n);
    //        if(list.size() % 2 == 1){
    //            sb.append(String.format("%d\n", list.get(list.size() / 2)));
    //        } else{
    //            sb.append(String.format("%d\n", list.get(list.size() / 2 - 1)));
    //        }
    //
    //    }
    //    System.out.println(sb.toString());
    //}

    public static void main(String[] args) throws Exception{
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());

        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());
            if (maxHeap.isEmpty() || num <= maxHeap.peek()) {
                maxHeap.offer(num);
            } else {
                minHeap.offer(num);
            }

            // balance heaps
            if (maxHeap.size() > minHeap.size() + 1) {
                minHeap.offer(maxHeap.poll());
            } else if (minHeap.size() > maxHeap.size()) {
                maxHeap.offer(minHeap.poll());
            }
            System.out.println(maxHeap.peek());
        }

    }
}
