package baekjoon.baekjoon_17298;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class bj_17298 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();


        int N = Integer.parseInt(br.readLine());

        int[] seq = new int[N];
        Stack<Integer> idx = new Stack<>(); // index 저장할 stack

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        // 수열 배열 초기화
        for (int i = 0; i < N; i++) {
            seq[i] = Integer.parseInt(st.nextToken());
        }


        for (int j = 0; j < N; j++) {

            // stack이 비어있지 않고, 현재 값이 stack의 값보다 클 경우
            // stack 값을 다 꺼낸 후 해당 index 값을 현재 값으로 변경
            while (!idx.isEmpty() && seq[j] > seq[idx.peek()]) {
                    seq[idx.pop()] = seq[j];
            }

            idx.push(j);
        }

        // stack에 남아있는 인덱스의 값 -1로 변경
        while (!idx.isEmpty()) {
            seq[idx.pop()] = -1;
        }

        for (int val : seq){
            sb.append(val).append(' ');
        }

        System.out.println(sb);
    }
}