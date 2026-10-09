class Solution:
    def shipWithinDays(self, ws: List[int], d: int) -> int:
        i = max(ws)
        j = sum(ws)

        while i<j:
            mid=(i+j)//2
            t = 0
            n = 1

            for w in ws:
                if t+w<=mid:
                    t+=w
                else:
                    n+=1
                    t = w

            if n<=d:
                j = mid
            else:
                i = mid+1

        return j












        # i = max(w)
        # j = sum(w)
        # while i<j:
        #     mid = (i+j)//2
        #     t = 0
        #     n = 1
        #     for wo in w:
        #         if t+wo<=mid:
        #             t+=wo
        #         else:
        #             n+=1
        #             t = wo
        #     if n<=d:
        #         j = mid
        #     else:
        #         i = mid+1

        # return i