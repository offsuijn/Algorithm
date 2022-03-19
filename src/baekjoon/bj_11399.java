package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class bj_11399 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] time = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for(int i = 0; i < N; i++) {
            time[i] = Integer.parseInt(st.nextToken());
        }

        int result = solution(time, N);
        
        System.out.println(result);
    }

    public static int solution(int[] time, int n) {
        int answer = 0;

        Arrays.sort(time);

        for (int i = 0; i < n; i++) {
            answer += time[i] * (n - i);
        }

        return answer;
    }
}
