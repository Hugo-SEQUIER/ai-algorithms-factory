class Greedy_Best_First_Search:
    @staticmethod
    def search(roll, biscuits):
        """
        Implements a Greedy Best-First Search algorithm to optimally place biscuits on a roll.
        This method iteratively selects the biscuit with the highest value-to-length ratio that can fit in the current position,
        aiming to maximize the total value of biscuits placed on the roll.

        Parameters:
        roll (Roll): The roll of dough to place biscuits on.
        biscuits (list): A list of available biscuit types.

        Returns:
        roll: The roll with biscuits placed, optimized for total value.
        """

        current_position = 0
        while current_position < roll.length:
            # Initializing variables to find the optimal biscuit for the current position   
            best_biscuit = None
            best_value_per_length = 0

            # Find the biscuit with the best value per unit length that fits
            for biscuit in biscuits:
                value_per_length = biscuit.value / biscuit.length
                if value_per_length > best_value_per_length and roll.check_position_empty(current_position, biscuit.length):
                    best_biscuit = biscuit
                    best_value_per_length = value_per_length

            # If a biscuit is found, add it to the roll
            if best_biscuit:
                added = roll.add_biscuit(current_position, best_biscuit)
                if added:
                    current_position += best_biscuit.length
                else:
                    current_position += 1  # Move to the next position if biscuit can't be added
            else:
                current_position += 1  # Move to the next position if no biscuit fits

        return roll