// https://www.acmicpc.net/problem/2011

import java.io.*;

public class Boj_2011 {
    public static final int MOD = 1000000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int N = str.length();

        int[] dp = new int[N+1];
        dp[0] = dp[1] = 1;

        // 0으로 시작하는 경우, 해석 불가
        if (str.charAt(0) == '0') {
            System.out.println(0);
            return ;
        }

        for (int i = 2; i <= N; i++) {
            int cur = i - 1;

            // 30, 40 등인 경우, 해석 불가
            if (str.charAt(cur) == '0' && (str.charAt(cur-1) < '1' || str.charAt(cur-1) > '2')) {
                System.out.println(0);
                return ;
            }

            // 현재 숫자가 0이 아닌 경우 -> 한 자리 암호로 해석 가능
            if (str.charAt(cur) != '0') {
                dp[i] += dp[i-1];
            }

            // 10~26 사이인 경우 -> 두 자리 암호로 해석 가능
            if (str.charAt(cur-1) == '1' || (str.charAt(cur-1) == '2' && str.charAt(cur) <= '6')) {
                dp[i] += dp[i-2];
            }

            dp[i] %= MOD;
        }

        System.out.println(dp[N]);

    }
}
