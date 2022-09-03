class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        dicts={
            'type':[i[0] for i in items],
            'color':[i[1] for i in items],
            'name':[i[2] for i in items]
        }
        return len([i for i in dicts[ruleKey]  if i==ruleValue])