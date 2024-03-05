# 841. Keys and Rooms
# https://leetcode.com/problems/keys-and-rooms/description/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        queue = deque(rooms[0])
        
        visited = [0] * len(rooms)
        visited[0] = 1
        
        while queue:
            k = queue.popleft()
            
            if visited[k]:
                continue
            else:
                visited[k] = 1
                queue.extend(rooms[k])
                    
        if sum(visited) == len(rooms):
            return True
        else:
            return False
