package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class bj_2607 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] words = new String[n];
        for (int i = 0; i < n; i++) words[i] = br.readLine();
        int answer = solution(n, words);
        System.out.println(answer);
    }

    public static int solution ( int n, String[] words){
        int answer = 0;
        int[] freq_strd = new int[26];
        int[] freq_other = new int[26];
        int diff;
        int length = words[0].length();

        counting(freq_strd, words[0]);

        for (int i = 1; i < n; i++) {
            diff = 0;
            Arrays.fill(freq_other, 0);
            counting(freq_other, words[i]);

            for (int k = 0; k < 26; k++) {
                diff += Math.abs(freq_strd[k] - freq_other[k]);
            }

            if (diff == 0 || diff == 1 || diff == 2 && (words[i].length() == length)) answer++;
        }
        return answer;
    }

    public static void counting(int[] freq_strd, String word) {
        for (int i = 0; i < word.length(); i++) {
            freq_strd[word.charAt(i) - 'A']++;
        }
    }
}
