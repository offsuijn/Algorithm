package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
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

        // Greedy : 돈을 인출하는 데 걸리는 시간이 작은 순서대로!

        Arrays.sort(time);

        int prev = 0;
        int result = 0;
        for (int t : time) {
            prev += t;
            result += prev;
        }

        System.out.println(result);
    }
}
