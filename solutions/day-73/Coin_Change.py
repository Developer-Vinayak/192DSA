class Solution:
    def coinChange(self, arr: List[int], amount: int) -> int:
        q=deque()
        q.append((0,0,0))
        n=len(arr)
        visit=set()
        while q:
            a,i,coin=q.popleft()
            if a==amount: return coin
            if a>amount: continue
            for j in range(i,n):
                val=a+arr[j]
                if val<=amount and val not in visit: 
                    q.append((val,j,coin+1))
                    visit.add(val)
        return -1
