order = 0
def solution(word):
    dic = {}
    lst =["A","E","I","O","U"]
    def dfs (s):
        global order
        if len(s) > 5:
            return
        dic[s] = order;
        order += 1
        for i in lst:
            if(len(s+i) > 5):
                return
            dfs(s + i)
    dfs("")
    return dic[word]