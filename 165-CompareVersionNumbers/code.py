class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(x) for x in version1.split(".")]
        v2 = [int(x) for x in version2.split(".")]

        for i in range(max(len(v1),len(v2))):
            if i <len(v1):
                vsub1 = v1[i]
            else:
                vsub1 = 0
            if i <len(v2):
                vsub2 = v2[i]
            else:
                vsub2 = 0
            
            if vsub1<vsub2:
                return -1
            elif vsub1>vsub2:
                return 1
        return 0