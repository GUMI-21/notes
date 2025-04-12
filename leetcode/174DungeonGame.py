"""
1.Sub-problem: dp[i][j] represent comes from cell(i,j) to solve princes needed minimum initial HP
2.Relation: dp[i][j] = max(- dungeon[i][j] + min(dp[i][i+1], dp[i+1][j]),1))
3.BaseCase: dp[m-1][n-1] = max(- dungeon[m-1][n-1] + 1, 1)

"""
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    dungeon[i][j] = min(dungeon[i][j], 0) * -1 + 1
                elif i == m-1:
                    dungeon[i][j] = max(dungeon[i][j+1] - dungeon[i][j], 1)
                elif j == n-1:
                    dungeon[i][j] = max(dungeon[i+1][j] - dungeon[i][j], 1)
                else:
                    dungeon[i][j] = max(min(dungeon[i][j+1], dungeon[i+1][j]) - dungeon[i][j], 1)
        return dungeon[0][0]

if __name__ == '__main__':
    dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    Solution().calculateMinimumHP(dungeon)