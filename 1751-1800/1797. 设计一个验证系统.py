class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive=timeToLive
        self.dict={}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.dict[tokenId]=currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.dict and currentTime-self.dict[tokenId]<self.timeToLive:
            self.dict[tokenId]=currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        # print(self.dict)
        return len([a for a in self.dict if currentTime-self.dict[a]<self.timeToLive])

