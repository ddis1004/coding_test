import java.util.Arrays;

public class LambdaTest {
    public static void main(String[] args) {
        Integer[] array = {2, 4, 5, 6};
        String[] strArray = {"Hello", "Hi", "My", "Name"};
        //Arrays.sort( array, (o1, o2) -> Integer.compare(o1.length(), o2.length()));
        //컴파일 시 타입이 자동으로 인식되어서 오류남
        Arrays.sort( strArray, (o1, o2) -> Integer.compare(o1.length(), o2.length()));
        System.out.println(Arrays.toString(array));
    }
}
