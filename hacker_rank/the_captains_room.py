class Solution():
    def the_captains_room(self, k:int, rooms:str):
        
        rooms_list = rooms.split()
        rooms_counter = dict()
        
        previous_captain = []

        for room in rooms_list:
            if room in rooms_counter.keys():
                rooms_counter[room] += 1
                
            else:
                rooms_counter[room] = 1
                
        for k, v in rooms_counter.items():
            if v == 1:
                print(k)
                break    
    
s = Solution()
s.the_captains_room(int(input()), input())