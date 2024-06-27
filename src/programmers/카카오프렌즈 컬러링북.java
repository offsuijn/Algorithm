// https://school.programmers.co.kr/learn/courses/30/lessons/1829?language=java

import java.util.*;

class Solution {
    public int[] solution(int m, int n, int[][] picture) {
        int[] dx = {0, 0, -1, +1};
        int[] dy = {-1, +1, 0, 0};
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        Queue<Cord> queue = new LinkedList<>();
        int color, cnt, x, y;
        
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(picture[i][j] == 0) continue;
                else {
                    numberOfArea++;
                    queue.add(new Cord(i, j));
                    cnt = 0;
                    color = picture[i][j];
                    picture[i][j] = 0;

                    while(!queue.isEmpty()) {
                        cnt++;
                        x = queue.peek().first;
                        y = queue.peek().second;
                        queue.poll();
                        for (int k = 0; k < 4; k++) {
                            if(x+dx[k] >= 0 && x+dx[k] < m && y+dy[k] >= 0 && y+dy[k] < n && picture[x+dx[k]][y+dy[k]] == color) {
                                queue.add(new Cord(x+dx[k], y+dy[k]));
                                picture[x+dx[k]][y+dy[k]] = 0;
                            }    
                        }

                    }    
                }
                
                maxSizeOfOneArea = Math.max(maxSizeOfOneArea, cnt);
            }
        }

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
    
    static class Cord {
        int first, second;
        public Cord(int first, int second) {
            this.first = first;
            this.second = second;
        }
    }
}
