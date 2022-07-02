from Hand import HandTypes

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
            availableHands.append(HandTypes.Ones)
        if this.getTwos() == -1:
            availableHands.append(HandTypes.Twos)
        if this.getThrees() == -1:
            availableHands.append(HandTypes.Threes)
        if this.getFours() == -1:
            availableHands.append(HandTypes.Fours)
        if this.getFives() == -1:
            availableHands.append(HandTypes.Fives)
        if this.getSixes() == -1:
            availableHands.append(HandTypes.Sixes)
        if this.getToK() == -1:
            availableHands.append(HandTypes.ToK)
        if this.getFoK() == -1:
            availableHands.append(HandTypes.FoK)
        if this.getFullHouse() == -1:
            availableHands.append(HandTypes.FH)
        if this.getSmallStraight() == -1:
            availableHands.append(HandTypes.SS)
        if this.getLargeStraight() == -1:
            availableHands.append(HandTypes.LS)
        if this.getYacht() == -1:
            availableHands.append(HandTypes.Yacht)
        if this.getChance() == -1:
            availableHands.append(HandTypes.Yacht)      
        return availableHands

    def __str__(this):
        returnString = "\nYacht Playcard\n\n"
        score = 0
        if this.getOnes() == -1:
            returnString = returnString + "Ones: 0\n"
        else:
            onesScore = this.getOnes()
            score += onesScore
            returnString = returnString + "Ones: " + str(onesScore) + "\n"
        if this.getTwos() == -1:
            returnString = returnString + "Twos: 0\n"
        else:
            twosScore = this.getTwos()
            score += twosScore
            returnString = returnString + "Twos: " + str(twosScore) + "\n"
        if this.getThrees() == -1:
            returnString = returnString + "Threes: 0\n"
        else:
            threesScore = this.getThrees()
            score += threesScore
            returnString = returnString + "Threes: " + str(threesScore) + "\n"
        if this.getFours() == -1:
            returnString = returnString + "Fours: 0\n"
        else:
            foursScore = this.getFours()
            score += foursScore
            returnString = returnString + "Fours: " + str(foursScore) + "\n"
        if this.getFives() == -1:
            returnString = returnString + "Fives: 0\n"
        else:
            fivesScore = this.getFives()
            score += fivesScore
            returnString = returnString + "Fives: " + str(fivesScore) + "\n"
        if this.getSixes() == -1:
            returnString = returnString + "Sixes: 0\n"
        else:
            sixesScore = this.getSixes()
            score += sixesScore
            returnString = returnString + "Sixes: " + str(sixesScore) + "\n"
        if score >= 63:
            score += 35
            returnString = returnString + "Bonus: " + str(35) + "\n"
        else:
            returnString = returnString + "Bonus: " + str(0) + "\n"
        if this.getToK() == -1:
            returnString = returnString + "Three of a Kind: 0\n"
        else:
            tokScore = this.getToK()
            score += tokScore
            returnString = returnString + "Three of a Kind: " + str(tokScore) + "\n"
        if this.getFoK() == -1:
            returnString = returnString + "Four of a Kind: 0\n"
        else:
            fokScore = this.getFoK()
            score += fokScore
            returnString = returnString + "Four of a Kind: " + str(fokScore) + "\n"
        if this.getFullHouse() == -1:
            returnString = returnString + "Full House: 0\n"
        else:
            fhScore = this.getFullHouse()
            score += fhScore
            returnString = returnString + "Full House: " + str(fhScore) + "\n"
        if this.getSmallStraight() == -1:
            returnString = returnString + "Small Straight: 0\n"
        else:
            ssScore = this.getSmallStraight()
            score += ssScore
            returnString = returnString + "Small Straight: " + str(ssScore) + "\n"
        if this.getLargeStraight() == -1:
            returnString = returnString + "Large Straight: 0\n"
        else:
            lsScore = this.getLargeStraight()
            score += lsScore
            returnString = returnString + "Large Straight: " + str(lsScore) + "\n"
        if this.getYacht() == -1:
            returnString = returnString + "Yacht: 0\n"
        else:
            yachtScore = this.getYacht()
            score += yachtScore
            returnString = returnString + "Yacht: " + str(yachtScore) + "\n"
        if this.getChance() == -1:
            returnString = returnString + "Chance: 0\n"
        else:
            chanceScore = this.getChance()
            score += chanceScore
            returnString = returnString + "Chance: " + str(chanceScore) + "\n"
        returnString = returnString + "\nTotal Score: " + str(score) +  "\n\n"
        return returnString