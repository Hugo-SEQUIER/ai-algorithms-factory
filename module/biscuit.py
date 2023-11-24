class Biscuit:
    def __init__(self, type, length, value, max_defects) :
        self.type = type 
        self.length = length
        self.value = value
        self.max_defects = max_defects
        self.defects = {
            'a' : 0,
            'b' : 0,
            'c' : 0
        }
    
    def update_defects(self, dict_defect, type_defect, nb_defect=1):
        for key, value in dict_defect.items() :
            if key == type_defect :
                dict_defect[key] = value + nb_defect
        return dict_defect

    def check_defect(self, defects_on_roll):
        return all(defects_on_roll[k] <= self.max_defects[k] for k in defects_on_roll if k in self.max_defects)
        