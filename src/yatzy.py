class Yatzy:
    
    FIFTY = 50
    ZERO = 0

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
        '''
        Renombrar una variable con un nombre más claro e informativo
        Reemplazar un número mágico por una constante
        '''
        dice_counts = {x: 0 for x in range(1,7)}
        for die in dice:
            dice_counts[die] += 1
        for die in dice_counts:
            if dice_counts[die] == 5:
                return Yatzy.FIFTY
        return Yatzy.ZERO
    
    @staticmethod
    def ones( *dice):
        '''
        Código se halla duplicado
        La lista de parámetros tiene demasiados parámetros
        '''
        sum_ones = 0
        for die in dice:
            if die == 1:
                sum_ones += die
            else:
                continue
        return sum_ones
    

    @staticmethod
    def twos(*dice):
        '''
        Código se halla duplicado
        La lista de parámetros tiene demasiados parámetros
        '''
        sum_twos = 0
        for die in dice:
            if die == 2:
                sum_twos += die
            else:
                continue
        return sum_twos
    
    @staticmethod
    def threes(*dice):
        '''
        Código se halla duplicado
        La lista de parámetros tiene demasiados parámetros
        '''
        sum_threes = 0
        for die in dice:
            if die == 3:
                sum_threes += die
            else:
                continue
        return sum_threes
    
    
    @staticmethod
    def fours(*dice):
        '''
        Renombrar una variable con un nombre más claro e informativo
        Cambiar objetos de referencia (self) a objetos de valor (enteros)
        '''
        sum_fours = 0
        for die in dice:
            if die == 4: 
                sum_fours += die
        return sum_fours
    
    @staticmethod
    def fives(*dice):
        '''
        Renombrar una variable con un nombre más claro e informativo
        Cambiar objetos de referencia (self) a objetos de valor (enteros)
        '''
        sum_fives = 0
        for die in dice:
            if die == 5: 
                sum_fives += die
        return sum_fives
    
    @staticmethod
    def sixes(*dice):
        '''
        Renombrar una variable con un nombre más claro e informativo
        Cambiar objetos de referencia (self) a objetos de valor (enteros)
        '''
        sum_sixes = 0
        for die in dice:
            if die == 6: 
                sum_sixes += die
        return sum_sixes
    
    @staticmethod
    def score_pair(*dice):
        '''
        Código se halla duplicado
        La lista de parámetros tiene demasiados parámetros
        Renombrar una variable con un nombre más claro e informativo
        '''
        dice_counts = {x: 0 for x in range(1,7)}
        for die in dice:
            dice_counts[die] += 1
        
        for i in range(6):
            if dice_counts[6-i] >= 2:
                return (6-i)*2
        return 0
    
    @staticmethod
    def two_pair(*dice):
        '''
        Código se halla duplicado
        La lista de parámetros tiene demasiados parámetros
        Renombrar una variable con un nombre más claro e informativo
        '''
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
        '''
        Código se halla duplicado
        La lista de parámetros tiene demasiados parámetros
        Renombrar una variable con un nombre más claro e informativo
        Reemplazar un número mágico por una constante
        '''
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
        '''
        Código se halla duplicado
        La lista de parámetros tiene demasiados parámetros
        Renombrar una variable con un nombre más claro e informativo
        Reemplazar un número mágico por una constante
        '''
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
        '''
        Código se halla duplicado
        La lista de parámetros tiene demasiados parámetros
        Sustituir un algoritmo complejo por uno simple
        '''
        return 15 if sorted(list(dice)) == [1,2,3,4,5] else 0

    @staticmethod
    def largeStraight(*dice):
        '''
        Código se halla duplicado
        La lista de parámetros tiene demasiados parámetros
        Sustituir un algoritmo complejo por uno simple
        '''
        return 20 if sorted(list(dice)) == [2,3,4,5,6] else 0
    

    @staticmethod
    def fullHouse(*dice):
        '''
        Código se halla duplicado
        La lista de parámetros tiene demasiados parámetros
        Renombrar una variable con un nombre más claro e informativo
        Sustituir un algoritmo complejo por uno simple
        '''
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

