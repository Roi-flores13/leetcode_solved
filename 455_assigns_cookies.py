class Solution:
    def findContentChildren(self, g, s):
        sorter = {"satisfied": [], "unstaisfied": []}
        for children in sorted(g)[::-1]:
            for cookie in sorted(s)[::-1]:
            
                if children  <= cookie:
                    sorter["satisfied"].append(children)
                    s.remove(cookie)
                    break
                else:
                    sorter["unstaisfied"].append(children)
                    g.remove(children)
                    break
                    
        return len(sorter["satisfied"])

g = [10,9,8,7]
s = [5,6,7,8]
sol = Solution()

print(sol.findContentChildren(g,s))

                
                