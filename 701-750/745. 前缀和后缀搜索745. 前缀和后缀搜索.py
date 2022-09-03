class WordFilter:
    def __init__(self, words: List[str]):
        self.a={}
        for ind,i in enumerate(words):
            for j in range(len(i)+1):
                for k in range(len(i)+1):
                    now=i[:j]+'$'+i[k:]
                    self.a[now]=ind
    def f(self, prefix: str, suffix: str) -> int:
        k=prefix+'$'+suffix
        return self.a.get(k,-1)
