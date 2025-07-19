class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        papers=[0]*(n+1)
        for i in citations:
            if i>n:
                papers[n]+=1
            else:
                papers[i]+=1
        
        h_index=0
        h_papers=0
        for i in range(len(papers)-1,-1,-1):
            h_index = i
            h_papers = h_papers+papers[i]

            if h_papers>=h_index:
                return h_index

            
