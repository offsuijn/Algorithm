package book_coding_test.greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class big_law {
    /**
     * 큰 수의 법칙
     */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] arr = new int[N];

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);

        int result = 0;
        int max1 = arr[N - 1];
        int max2 = arr[N - 2];

        // 가장 큰 수가 더해지는 횟수 계산
        int cnt = M / (K + 1) * K;
        cnt += M % (K + 1);

        result += cnt * max1;
        result += (M - cnt) * max2;

        System.out.println(result);

    }
}
