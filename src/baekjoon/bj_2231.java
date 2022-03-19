package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj_2231 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int answer = solution(n);
        System.out.println(answer);
    }

    public static int solution(int n) {
        int answer = 0;

        for (int i = 1; i < n; i++) {
            int k = i;
            int sum = k;

            while (k > 0) {
                sum += (k % 10);
                k /= 10;
            }

            if (sum == n) {
                answer = i;
                break;
            }
        }

        return answer;
    }
}
