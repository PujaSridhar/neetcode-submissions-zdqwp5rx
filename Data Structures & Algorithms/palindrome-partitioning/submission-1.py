class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palindrome(s:str) -> bool:
            return s == s[::-1]
        def backtrack(start: str,path: List[str]):    
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start+1,len(s)+1):
                if palindrome(s[start:end]):
                    path.append(s[start:end])
                    backtrack(start +end -start, path)
                    path.pop()

        result = []
        backtrack(0,[])
        return result