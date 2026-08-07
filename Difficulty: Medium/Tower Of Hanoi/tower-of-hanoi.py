class Solution:
    def towerOfHanoi(self, n, fromm, to, aux):
        if n == 1:
            return 1

        return (
            self.towerOfHanoi(n - 1, fromm, aux, to)
            + 1
            + self.towerOfHanoi(n - 1, aux, to, fromm)
        )