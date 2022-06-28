import Hand

class PlayCard():
    ones = -1
    twos = -1
    threes = -1
    fours = -1
    fives = -1
    sixes = -1
    tok = -1
    fok = -1
    fh = -1
    ss = -1
    ls = -1
    yacht = -1
    chance = -1

    def getOnes(this):
        return this.ones
    
    def setOnes(this, value):
        this.ones = value

    def getTwos(this):
        return this.twos
    
    def setTwos(this, value):
        this.twos = value

    def getThrees(this):
        return this.threes
    
    def setThrees(this, value):
        this.threes = value

    def getFours(this):
        return this.fours
    
    def setFours(this, value):
        this.fours = value

    def getFives(this):
        return this.fives
    
    def setFives(this, value):
        this.fives = value

    def getSixes(this):
        return this.sixes
    
    def setSixes(this, value):
        this.Sixes = value

    def getToK(this):
        return this.tok
    
    def setToK(this, value):
        this.tok = value

    def getFoK(this):
        return this.fok
    
    def setFoK(this, value):
        this.fok = value

    def getFullHouse(this):
        return this.fh
    
    def setFullHouse(this, value):
        this.fh = value

    def getSmallStraight(this):
        return this.ss
    
    def setSmallStraight(this, value):
        this.ss = value

    def getLargeStraight(this):
        return this.ls
    
    def setLargeStraight(this, value):
        this.ls = value

    def getYacht(this):
        return this.yacht
    
    def setYacht(this, value):
        this.yacht = value

    def getChance(this):
        return this.chance
    
    def setChance(this, value):
        this.chance = value

    def totalScore(this):
        score = 0
        if this.getOnes() == -1:
            score += 0
        else:
            score += this.getOnes()
        if this.getTwos() == -1:
            score += 0
        else:
            score += this.getTwos()
        if this.getThrees() == -1:
            score += 0
        else:
            score += this.getThrees()
        if this.getFours() == -1:
            score += 0
        else:
            score += this.getFours()
        if this.getFives() == -1:
            score += 0
        else:
            score += this.getFives()
        if this.getSixes() == -1:
            score += 0
        else:
            score += this.getSixes() 
        if score >= 63:
            score += 35 
        if this.getToK() == -1:
            score += 0
        else:
            score += this.getToK()
        if this.getFoK() == -1:
            score += 0
        else:
            score += this.getFoK()
        if this.getFullHouse() == -1:
            score += 0
        else:
            score += this.getFullHouse()
        if this.getSmallStraight() == -1:
            score += 0
        else:
            score += this.getSmallStraight()
        if this.getLargeStraight() == -1:
            score += 0
        else:
            score += this.getLargeStraight()
        if this.getYacht() == -1:
            score += 0
        else:
            score += this.getYacht()
        if this.getChance() == -1:
            score += 0
        else:
            score += this.getChance() 
              
        return score

    def availableHands(this):
        availableHands = []
        if this.getOnes() == -1:
            availableHands.append(Hand.Ones)
        if this.getTwos() == -1:
            availableHands.append(Hand.Twos)
        if this.getThrees() == -1:
            availableHands.append(Hand.Threes)
        if this.getFours() == -1:
            availableHands.append(Hand.Fours)
        if this.getFives() == -1:
            availableHands.append(Hand.Fives)
        if this.getSixes() == -1:
            availableHands.append(Hand.Sixes)
        if this.getToK() == -1:
            availableHands.append(Hand.ToK)
        if this.getFoK() == -1:
            availableHands.append(Hand.FoK)
        if this.getFullHouse() == -1:
            availableHands.append(Hand.FH)
        if this.getSmallStraight() == -1:
            availableHands.append(Hand.SS)
        if this.getLargeStraight() == -1:
            availableHands.append(Hand.LS)
        if this.getYacht() == -1:
            availableHands.append(Hand.Yacht)
        if this.getChance() == -1:
            availableHands.append(Hand.Yacht)      
        return availableHands