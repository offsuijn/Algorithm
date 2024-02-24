# 733. Flood Fill
# https://leetcode.com/problems/flood-fill/description/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        origin_color = image[sr][sc]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def fill(sr, sc):
            image[sr][sc] = color
            
            for (r, c) in dirs:
                new_sr = sr + r
                new_sc = sc + c
                if 0 <= new_sr < len(image) and 0 <= new_sc < len(image[0]) and image[new_sr][new_sc] == origin_color:
                    fill(new_sr, new_sc)                   
            return
        
        if origin_color == color:
            return image
                    
        fill(sr, sc)
        return image
