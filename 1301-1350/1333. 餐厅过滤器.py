import functools
def cmp(a,b):
    if a[1]==b[1]:
        return a[0]-b[0]
    else:
        return a[1]-b[1]

class Solution:
    def filterRestaurants(self, restaurants, veganFriendly: int, maxPrice: int, maxDistance: int) :
        res=[r for r in restaurants if r[2]>=veganFriendly and r[3]<=maxPrice and r[4]<=maxDistance]
        res.sort(key=functools.cmp_to_key(cmp),reverse=True)
        return [r[0] for r in res]