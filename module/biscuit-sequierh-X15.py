class Biscuit:
    def __init__(self, nb_biscuit, length, value, max_defects) :
        self.nb_biscuit = nb_biscuit 
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

    def check_defect(self, type_defect, nb_defect=1):
        copy_defect = self.defects.copy()
        copy_defect = self.update_defects(copy_defect, type_defect, nb_defect)
        for key, value in copy_defect.items() :
            if value > self.max_defects[key]:
                print("Can't add biscuit")
                return False
        return True
        