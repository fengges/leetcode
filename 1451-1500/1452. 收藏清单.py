class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        return [i for i, f in enumerate(favoriteCompanies) if not any(set(c) > set(f) for c in favoriteCompanies)]