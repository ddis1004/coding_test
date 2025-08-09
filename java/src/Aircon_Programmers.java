import java.io.*;
import java.util.*;
public class Aircon_Programmers {
    static int[][] dp;
    public int solution(int temperature, int t1, int t2, int a, int b, int[] onboard) {
        t1 += 10;
        t2 += 10;
        temperature += 10;
        dp = new int[onboard.length][51]; //time, temperature

        for(int i = 0; i < onboard.length; i ++){
            for(int j = 0; j < 51; j ++){
                dp[i][j] = Integer.MAX_VALUE;
            }
        }
        dp[0][temperature] = 0;

        for(int i = 0; i < onboard.length - 1; i ++ ){
            for(int j = 0; j < 51; j ++){
                if(dp[i][j] == Integer.MAX_VALUE) continue;

                //decrease temperature
                if(j - 1 >= 0 &&
                        (onboard[i + 1] == 0 ||
                                (onboard[i + 1] == 1 && j - 1 >= t1 && j - 1 <= t2))){
                    if(temperature >= j){
                        dp[i + 1][j - 1] = Math.min(dp[i + 1][j - 1], dp[i][j] + a);
                    } else {
                        dp[i + 1][j - 1] = Math.min(dp[i + 1][j - 1], dp[i][j]);
                    }
                }

                //increase temperature
                if(j + 1 < 51 &&
                        (onboard[i + 1] == 0 ||
                                (onboard[i + 1] == 1 && j + 1 >= t1 && j + 1 <= t2))){
                    if(temperature <= j){
                        dp[i + 1][j + 1] = Math.min(dp[i + 1][j + 1], dp[i][j] + a);
                    } else {
                        dp[i + 1][j + 1] = Math.min(dp[i + 1][j + 1], dp[i][j]);
                    }
                }

                //keep temperature
                if(onboard[i + 1] == 0 ||
                        (onboard[i + 1] == 1 && j >= t1 && j <= t2)){
                    if(temperature == j) dp[i + 1][j] = Math.min(dp[i + 1][j], dp[i][j]);
                    else dp[i + 1][j] = Math.min(dp[i + 1][j], dp[i][j] + b);
                }
            }
        }

        int answer = Integer.MAX_VALUE;
        for(int i = 0; i < 51; i ++){
            answer = Math.min(answer, dp[onboard.length - 1][i]);
        }

        return answer;
    }
}
