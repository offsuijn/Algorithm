// https://school.programmers.co.kr/learn/courses/30/lessons/43238?language=java

import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        Arrays.sort(times);

        long left = 1;
        long right = (long)times[times.length-1] * (long)n;
        long cnt, mid;

        while (left < right) {
            cnt = 0;
            mid = (left + right) / 2;

            for (int t : times) {
                cnt += (mid / t);
            }

            if (cnt >= n) {
                right = mid;
            }
            else {
                left = mid + 1;
            }
        }
        
        return right;
    }
}
