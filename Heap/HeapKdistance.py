'''
Given a non-empty string str and an integer k, rearrange the string such that the same characters are at least distance k from each other.
All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string.

Example 1: str = "aabbcc", k = 3
Result: "abcabc"
'''

'''
'''

def reorganizeStringKdistance( s: str,k) -> str:

    if not s or k == 0:
        return s

    d = defaultdict(int)
    for c in s:
        d[c] += 1

    ans = []
    maxHeap = [(freq, c) for c, freq in d.items()]
    heapq.heapify(maxHeap)

    while maxHeap:

        cur = []

        for _ in range(k):

            if not maxHeap:
                return ''.join(ans) if len(ans) == len(s) else ''

            freq,c = heapq.heappop(maxHeap)
            ans.append(c)

            freq -= 1

            if freq > 0:
                cur.append((freq,c))

        for count,char in cur:
            heapq.heappush(maxHeap,(count,char))

    return ''.join(ans)
