package baekjoon.baekjoon_1181;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class bj_1181 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        String[] arr = new String[N];
        for(int i = 0; i < N; i++){
            arr[i] = br.readLine();
        }

        Arrays.sort(arr, (s1, s2) -> {
            if (s1.length() == s2.length()) { // 길이가 같을 경우, 사전식 정렬
                return s1.compareTo(s2);
            }
            else if (s1.length() > s2.length()) { // 오름차순 정렬
                return 1;
            }
            return -1;
        });

        sb.append(arr[0]).append('\n');
        for(int i = 1; i < N; i++) {
            if (!arr[i].equals(arr[i - 1])) { // 중복 문자는 한 번만 출력
                sb.append(arr[i]).append('\n');
            }
        }

        System.out.println(sb);

    }
}
