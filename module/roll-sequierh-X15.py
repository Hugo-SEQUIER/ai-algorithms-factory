class Roll:
    def __init__(self, defects, length=500):
        self.length = length
        self.roll = self.build_roll(defects, length)

    def build_roll(self, defects, length):
        roll = [{"empty" : -1, 'defects' : {}} for _ in range(0, length)]
        for idx in range(0,length):
            mask_position = defects['x'] == idx
            list_type = ["a","b","c"]
            for type in list_type:
                mask_type = defects['class'] == type
                roll[idx]["defects"][type] = len(defects[mask_position & mask_type])
        return roll

    def check_position_empty(self, position, biscuit_length=1):
        if position >=0 and (position + biscuit_length) < self.length :
            return all(element["empty"] == -1 for element in self.roll[position : (position + biscuit_length)])
        print("Can't add biscuit")
        return False
    
    def add_biscuit(self, position, biscuit):
        if self.check_position_empty(position, biscuit.length):
            defects_at_position = self.roll[position]["defects"]
            if all(biscuit.check_defect(defect_type, nb_defect) for defect_type,nb_defect in defects_at_position.items()):
                for idx_length in range(0, biscuit.length):
                    self.roll[position + idx_length]["empty"] = biscuit
        return self.roll
    
    def solution(self):
        cpt_value = 0
        idx = 0
        while idx < self.length:
            if self.roll[idx]["empty"] != -1:
                cpt_value += self.roll[idx]["empty"].value
                idx += self.roll[idx]["empty"].length - 1
            idx += 1
        return cpt_value
                    