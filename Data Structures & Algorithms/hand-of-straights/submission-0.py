class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # If the total number of cards isn't divisible by groupSize, return False
        if len(hand) % groupSize != 0:
            return False
        
        # Count the frequency of each card
        count = Counter(hand)
        
        # Sort the unique cards
        sorted_keys = sorted(count)
        
        for card in sorted_keys:
            if count[card] > 0:
                # Number of groups to form starting from this card
                num_groups = count[card]
                
                # Try to form a group with consecutive cards
                for i in range(card, card + groupSize):
                    if count[i] < num_groups:
                        return False
                    count[i] -= num_groups
        
        return True       