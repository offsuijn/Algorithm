package baekjoon.baekjoon_2750;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class bj_2750 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        boolean[] arr = new boolean[2001]; // 범위 -1000 ~ 1000, 수가 중복되지 않으므로 boolean 타입의 배열

        for (int i = 0; i < N; i++){
            arr[Integer.parseInt(br.readLine()) + 1000] = true;
        }

        for (int i = 0; i < 2001; i++) {
            if (arr[i]) {
                sb.append(i - 1000).append('\n');
            }
        }
        System.out.println(sb);
    }

}
