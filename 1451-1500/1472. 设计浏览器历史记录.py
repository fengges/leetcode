class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack=[homepage]
        self.size=0

    def visit(self, url: str) -> None:
        self.stack=self.stack[:self.size+1]+[url]
        self.size+=1

    def back(self, steps: int) -> str:
        self.size=max(0,self.size-steps)
        return self.stack[self.size]

    def forward(self, steps: int) -> str:
        self.size=min(self.size+steps,len(self.stack)-1)
        return self.stack[self.size]



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)