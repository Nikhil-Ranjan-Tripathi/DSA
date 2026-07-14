class Solution:
    def maxCoins(self, t, a, b):
        boxes = list(zip(b, a))  

        boxes.sort(reverse=True)

        ans = 0

        for coins, plates in boxes:
            if t == 0:
                break

            take = min(plates, t)
            ans += take * coins
            t -= take

        return ans