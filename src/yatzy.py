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
    def smallStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1):
            return 15
        return 0
    

    @staticmethod
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
            and tallies[5] == 1):
            return 20
        return 0
    

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
