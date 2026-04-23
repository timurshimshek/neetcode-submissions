class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        x = {}
        k = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        iter = 0
        for i in strs:
            temp_k = k.copy()
            for j in i:
                temp_k[ord(j)- 97] += 1
            temp_k = tuple(temp_k)
            if temp_k in x:
                output[x[temp_k]].append(i)
            else:
                x[temp_k] = iter
                output.append([i])
                iter +=1
        return output