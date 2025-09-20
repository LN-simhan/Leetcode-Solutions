import collections
from bisect import bisect_left, bisect_right
class Router:

    def __init__(self, memoryLimit: int):
        self.max = memoryLimit
        self.uniquePackets = set()
        self.packets = collections.deque()
        self.destinations = collections.defaultdict(collections.deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source,destination,timestamp)
        if packet in self.uniquePackets:
            return False
        if len(self.packets)==self.max:
            pack = self.packets.popleft()
            self.uniquePackets.remove(pack)
            self.destinations[pack[1]].popleft()
        self.uniquePackets.add(packet)
        self.packets.append(packet)
        self.destinations[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.uniquePackets:
            return []
        pack = self.packets.popleft()
        self.uniquePackets.remove(pack)
        self.destinations[pack[1]].popleft()
        return list(pack)
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.destinations:
            return 0
        timestamps = self.destinations[destination]
        leftIndex = bisect_left(timestamps,startTime)
        rightIndex = bisect_right(timestamps,endTime)
        return rightIndex-leftIndex

        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)