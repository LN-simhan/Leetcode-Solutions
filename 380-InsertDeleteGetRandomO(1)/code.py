import random
class RandomizedSet:

    def __init__(self):
        self.num_map={}
        self.num_list=[]

    def insert(self, val: int) -> bool:
        if val in self.num_map:
            return False
        else:
            self.num_map[val]=len(self.num_list)
            self.num_list.append(val)
            return True
        
    def remove(self, val: int) -> bool:
        if val in self.num_map:
            idx = self.num_map[val]
            last = self.num_list[-1]
            self.num_list[idx]= last
            self.num_map[last]= idx
            self.num_list.pop()
            del self.num_map[val]
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(self.num_list)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()