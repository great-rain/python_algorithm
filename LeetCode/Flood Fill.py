class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        target = image[sr][sc]
        from collections import deque

        queue = deque()
        queue.append([sr, sc])
        visited = []

        dx = [-1, 0, 1, 0, 0]
        dy = [0, -1, 0, 1, 0]

        while queue:
            now = queue.popleft()

            for i in range(5):
                move_x = now[0] + dx[i]
                move_y = now[1] + dy[i]

                if 0 <= move_x < len(image) and 0 <= move_y < len(image[0]):
                    if [move_x, move_y] not in visited:
                        visited.append([move_x, move_y])

                        if image[move_x][move_y] == target:
                            queue.append([move_x, move_y])
                            image[move_x][move_y] = color

        return image