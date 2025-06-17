class Solution:
    def __init__(self):
        self.ans = [i for i in range(1, 2000) if i % 3 != 0 and str(i)[-1] != "3"][
            :1003
        ]

    def find(self):
        for _ in range(int(input())):
            print(self.ans[int(input()) - 1])


Solution().find()
