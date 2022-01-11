package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class bj_11047 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int cnt = 0;

        ArrayList<Integer> coin_types = new ArrayList<>();

        while(N-- > 0) {
            int a = Integer.parseInt(br.readLine());
            if(a > K) break; // coin의 단위가 K보다 크면 입력을 멈춘다.

            coin_types.add(a);
        }

        for (int i = coin_types.size()-1; i >= 0; i--) {
            int coin = coin_types.get(i);

            if(K < coin || coin == 0) continue;

            cnt += K / coin;
            K %= coin;
        }

        System.out.println(cnt);
    }

}
