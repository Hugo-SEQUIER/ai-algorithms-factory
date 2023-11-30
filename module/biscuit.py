class Biscuit:
    """
    This class is all about individual biscuits - their type, size, value, 
    and how finicky they are about defects. Each biscuit is an opportunity to earn some dough, 
    but we've got to play by the rules.
    """
    def __init__(self, type, length, value, max_defects) :
        """
        We need to define what it is, how big it is, how valuable it is, 
        and what defects it can tolerate.

        Parameters:
        type (str): The type or variety of the biscuit.
        length (int): How long the biscuit is, because size matters here!
        value (int): What's the biscuit worth? Higher value means more profit.
        max_defects (dict): A playbook of what defects this biscuit can handle and how many.
        """
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
        """
        Biscuits are picky about their neighbors. This method updates the defect count to see if 
        our biscuit can handle the local defect environment. It's like checking the air quality 
        before going for a run.

        Parameters:
        dict_defect (dict): Current defect count around the biscuit.
        type_defect (str): The type of defect we're particularly looking at.
        nb_defect (int, optional): How many defects of this type are there? Defaults to 1.

        Returns:
        dict: Updated defect count, now including the new defects we just counted.
        """
        for key, value in dict_defect.items() :
            if key == type_defect :
                dict_defect[key] = value + nb_defect
        return dict_defect

    def check_defect(self, type_defect, nb_defect=1):
        """
        Can our biscuit handle the defects at its planned position on the roll? 
        This function is like a quality control inspector. It checks if the local defect levels 
        exceed our biscuit's tolerance. If it's too much, we might have to find a new spot.

        Parameters:
        type_defect (str): The type of defect we're evaluating.
        nb_defect (int): The number of defects of this type.

        Returns:
        bool: True if the biscuit can deal with these defects, False if it's a no-go.
        """
        copy_defect = self.defects.copy()
        copy_defect = self.update_defects(copy_defect, type_defect, nb_defect)
        for key, value in copy_defect.items() :
            if value > self.max_defects[key]:
                print("Can't add biscuit")
                return False
        return True