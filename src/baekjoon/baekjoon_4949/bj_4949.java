package baekjoon.baekjoon_4949;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class bj_4949 {
    public static char[] stack;
    public static int size;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        while (true) {
            char[] arr = br.readLine().toCharArray();
            stack = new char[arr.length];
            size = 0;
            boolean flag = true; // 균형이 맞으면 true

            if (arr.length == 1 && arr[0] == '.') { // '.' 하나가 입력으로 들어오면 종료
                break;
            }

            for(char val : arr) { // 문자열 순회

                if (val == '(' || val == '[') { // '(' 또는 '['가 들어오면 stack에 push
                    push(val);
                }
                else if (val == ')' || val == ']') { // ')' 또는 ']'가 들어오면 stack에서 pop
                    if (size == 0) { // 여는 문자열이 부족함 -> 불균형
                        flag = false;
                        break;
                    }
                    char res = pop();

                    // 짝이 맞는지 비교
                    if (val == ')' && res == '(') {
                        continue;
                    }
                    else if (val == ']' && res == '[') {
                        continue;
                    }
                    else { // 여는 기호와 닫는 기호가 다름 -> 불균형
                        flag = false;
                        break;
                    }
                }
            }
            if (size > 0) { // 여는 기호가 남은 -> 불균형
                flag = false;
            }

            if (flag) {
                sb.append("yes").append('\n');
            }
            else {
                sb.append("no").append('\n');
            }

        }

        System.out.println(sb);
    }

    public static void push(char item) {
        stack[size++] = item;
    }

    public static char pop() {
        return stack[--size];
    }
}