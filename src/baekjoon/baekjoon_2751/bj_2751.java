package baekjoon.baekjoon_2751;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class bj_2751 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        ArrayList<Integer> arrList = new ArrayList<>();

        for (int i = 0; i < N; i++){
            arrList.add(Integer.parseInt(br.readLine()));
        }

        Collections.sort(arrList);

        for (int value : arrList) {
            sb.append(value).append('\n');
        }

        System.out.println(sb);
    }

}
