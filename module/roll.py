class Roll:
    """
    The Roll class represents a roll of dough in the biscuit manufacturing process. 
    It's designed to keep track of the dough's length and the distribution of defects across it. 
    Think of it as a map of where we can (or can't) place biscuits based on these defects.
    """

    def __init__(self, defects, length=500):
        """
        When we create a new roll, we need to know about any defects it has and its length.
        This setup is crucial for figuring out how to optimally place the biscuits later on.

        Parameters:
        defects (DataFrame): Information about where defects are on the dough and their types.
        length (int, optional): How long the dough roll is. Defaults to 500 units.
        """
        self.length = length
        self.roll = self.build_roll(defects, length)

    def build_roll(self, defects, length):
        """
        Here we construct our roll of dough. It's a bit like setting up the game board.
        We take the length of the roll and the defects data to create a detailed map of the roll.
        Each section of the roll will have information about whether it's usable or has defects.

        Parameters:
        defects (DataFrame): Detailed data on the types and locations of defects in the dough.
        length (int): The total length of the dough roll we're working with.

        Returns:
        list: A structured representation of the dough roll, section by section, including defects.
        """
        roll = [{"empty" : -1, 'defects' : {}} for _ in range(0, length)]
        for idx in range(0,length):
            mask_position = defects['x'] == idx
            list_type = ["a","b","c"]
            for type in list_type:
                mask_type = defects['class'] == type
                roll[idx]["defects"][type] = len(defects[mask_position & mask_type])
        return roll

    def check_position_empty(self, position, biscuit_length=1):
        """
        Before placing a biscuit, we need to make sure the spot is empty and not already taken.
        This function checks if a specific section of the roll is free of other biscuits.

        Parameters:
        position (int): The starting position on the roll where we want to place the biscuit.
        biscuit_length (int, optional): How long the biscuit is. Defaults to 1 unit.

        Returns:
        bool: True if the space is empty and ready for a new biscuit, False otherwise.
        """
        if position >=0 and (position + biscuit_length) < self.length :
            return all(element["empty"] == -1 for element in self.roll[position : (position + biscuit_length)])
        print("Can't add biscuit")
        return False
    
    def add_biscuit(self, position, biscuit):
        """
        Time to place a biscuit.
        This function not only checks if the spot is available but also makes sure that the biscuit
        meets our quality standards by checking against the defect constraints.

        Parameters:
        position (int): Where on the roll we're trying to place the biscuit.
        biscuit (Biscuit): The biscuit object we want to add to our roll.

        Returns:
        list: An updated view of our roll, now with the new biscuit added (if everything went well).
        """
        if self.check_position_empty(position, biscuit.length):
            defects_at_position = self.roll[position]["defects"]
            if all(biscuit.check_defect(defect_type, nb_defect) for defect_type,nb_defect in defects_at_position.items()):
                for idx_length in range(0, biscuit.length):
                    self.roll[position + idx_length]["empty"] = biscuit
        return self.roll
    
    def solution(self):
        """
        After all our hard work placing biscuits, let's see what we've got!
        This function tallies up the total value of all the biscuits on the roll.
        It's like calculating the score of how well we did in optimizing our biscuit placement.

        Returns:
        int: The total value of all the biscuits on the roll.
        """
        cpt_value = 0
        idx = 0
        while idx < self.length:
            if self.roll[idx]["empty"] != -1:
                cpt_value += self.roll[idx]["empty"].value
                idx += self.roll[idx]["empty"].length - 1
            idx += 1
        return cpt_value
                    