class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        t1=sum(distance)
        t2=sum(distance[min(start,destination):max(start,destination)])
        return min(t2,t1-t2)