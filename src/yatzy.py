class Yatzy:

    @staticmethod
    def chance(*dice):
        '''
        Código se halla duplicado
        La lista de parámetros tiene demasiados parámetros
        '''
        
        total = 0
        for i in dice:
            total += i
        return total

    @staticmethod
    def yatzy(*dice):
        dice_counts = {x: 0 for x in range(1,7)}
        for die in dice:
            dice_counts[die] += 1
        for die in dice_counts:
            if dice_counts[die] == 5:
                return 50
        return 0
    
    @staticmethod
    def ones( *dice):
        sum_ones = 0
        for die in dice:
            if die == 1:
                sum_ones += die
            else:
                continue
        return sum_ones
    

    @staticmethod
    def twos(*dice):
        sum_twos = 0
        for die in dice:
            if die == 2:
                sum_twos += die
            else:
                continue
        return sum_twos
    
    @staticmethod
    def threes(*dice):
        sum_threes = 0
        for die in dice:
            if die == 3:
                sum_threes += die
            else:
                continue
        return sum_threes
    

    def __init__(self, d1, d2, d3, d4, _5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5
    
    @staticmethod
    def fours(*dice):
        sum_fours = 0
        for die in dice:
            if die == 4: 
                sum_fours += die
        return sum_fours
    
    @staticmethod
    def fives(*dice):
        sum_fives = 0
        for die in dice:
            if die == 5: 
                sum_fives += die
        return sum_fives
    
    @staticmethod
    def sixes(*dice):
        sum_sixes = 0
        for die in dice:
            if die == 6: 
                sum_sixes += die
        return sum_sixes
    
    @staticmethod
    def score_pair(*dice):
        dice_counts = {x: 0 for x in range(1,7)}
        for die in dice:
            dice_counts[die] += 1
        
        for i in range(6):
            if dice_counts[6-i] >= 2:
                return (6-i)*2
        return 0
    
    @staticmethod
    def two_pair(*dice):
        dice_counts = {x: 0 for x in range(1,7)}
        for die in dice:
            dice_counts[die] += 1
        pairs_count = 0
        score = 0
        for i in range(6):
            if dice_counts[6-i] >= 2:
                pairs_count += 1
                score += (6-i)
                if pairs_count == 2:
                    return score * 2
        return 0        
    
    @staticmethod
    def four_of_a_kind(*dice):
        FOUR = 4
        dice_counts = {x: 0 for x in range(1,7)}
        for die in dice:
            dice_counts[die] += 1
        
        for i in range(6):
            if dice_counts[6-i] >= FOUR:
                return (6-i)*FOUR
        return 0
    

    @staticmethod
    def three_of_a_kind(*dice):
        THREE = 3
        dice_counts = {x: 0 for x in range(1,7)}
        for die in dice:
            dice_counts[die] += 1
        
        for i in range(6):
            if dice_counts[6-i] >= THREE:
                return (6-i)*THREE
        return 0
    

    @staticmethod
    def smallStraight(*dice):
        return 15 if sorted(list(dice)) == [1,2,3,4,5] else 0

    @staticmethod
    def largeStraight(*dice):
        return 20 if sorted(list(dice)) == [2,3,4,5,6] else 0
    

    @staticmethod
    def fullHouse(*dice):
        dice_counts = {x: 0 for x in range(1,7)}
        for die in dice:
            dice_counts[die] += 1
        
        isPair = False
        isTrio = False

        for die in dice_counts:
            if dice_counts[die] == 2: 
                isPair = True
            elif dice_counts[die] == 3:
                isTrio = True
                
        if isPair and isTrio:
            return sum(dice)
        else:
            return 0

