package baekjoon.baekjoon_9012;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class bj_9012 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        String inputs[] = new String[T];
        for (int i = 0; i < T; i++) inputs[i] = br.readLine();
        String answer[] = solution(T, inputs);

        for (int i = 0; i < T; i++) System.out.println(answer[i]);
    }

        public static String[] solution ( int T, String[] inputs){
            String answer[] = new String[T];

            Stack<Character> stack = new Stack<Character>();
            boolean flag;

            for (int t = 0; t < T; t++) {
                stack.clear();
                flag = true;
                for (int i = 0; i < inputs[t].length(); i++) {
                    if (inputs[t].charAt(i) == '(') stack.add('(');
                    else {
                        if (!stack.empty()) stack.pop();
                        else {
                            flag = false;
                            break;
                        }
                    }
                }

                if (flag && stack.empty()) answer[t] = "YES";
                else answer[t] = "NO";
            }

            return answer;

        }
}
