from Hand import HandTypes
from Constants import *

class PlayCard():
    ones = INCOMPLETE_ENTRY
    twos = INCOMPLETE_ENTRY
    threes = INCOMPLETE_ENTRY
    fours = INCOMPLETE_ENTRY
    fives = INCOMPLETE_ENTRY
    sixes = INCOMPLETE_ENTRY
    tok = INCOMPLETE_ENTRY
    fok = INCOMPLETE_ENTRY
    fh = INCOMPLETE_ENTRY
    ss = INCOMPLETE_ENTRY
    ls = INCOMPLETE_ENTRY
    yacht = INCOMPLETE_ENTRY
    chance = INCOMPLETE_ENTRY

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
        this.sixes = value

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
        if this.getOnes() == INCOMPLETE_ENTRY:
            score += 0
        else:
            score += this.getOnes()
        if this.getTwos() == INCOMPLETE_ENTRY:
            score += 0
        else:
            score += this.getTwos()
        if this.getThrees() == INCOMPLETE_ENTRY:
            score += 0
        else:
            score += this.getThrees()
        if this.getFours() == INCOMPLETE_ENTRY:
            score += 0
        else:
            score += this.getFours()
        if this.getFives() == INCOMPLETE_ENTRY:
            score += 0
        else:
            score += this.getFives()
        if this.getSixes() == INCOMPLETE_ENTRY:
            score += 0
        else:
            score += this.getSixes() 
        if score >= 63:
            score += 35 
        if this.getToK() == INCOMPLETE_ENTRY:
            score += 0
        else:
            score += this.getToK()
        if this.getFoK() == INCOMPLETE_ENTRY:
            score += 0
        else:
            score += this.getFoK()
        if this.getFullHouse() == INCOMPLETE_ENTRY:
            score += 0
        else:
            score += this.getFullHouse()
        if this.getSmallStraight() == INCOMPLETE_ENTRY:
            score += 0
        else:
            score += this.getSmallStraight()
        if this.getLargeStraight() == INCOMPLETE_ENTRY:
            score += 0
        else:
            score += this.getLargeStraight()
        if this.getYacht() == INCOMPLETE_ENTRY:
            score += 0
        else:
            score += this.getYacht()
        if this.getChance() == INCOMPLETE_ENTRY:
            score += 0
        else:
            score += this.getChance() 
              
        return score

    def availableHands(this):
        availableHands = []
        if this.getOnes() == INCOMPLETE_ENTRY:
            availableHands.append(HandTypes.Ones)
        if this.getTwos() == INCOMPLETE_ENTRY:
            availableHands.append(HandTypes.Twos)
        if this.getThrees() == INCOMPLETE_ENTRY:
            availableHands.append(HandTypes.Threes)
        if this.getFours() == INCOMPLETE_ENTRY:
            availableHands.append(HandTypes.Fours)
        if this.getFives() == INCOMPLETE_ENTRY:
            availableHands.append(HandTypes.Fives)
        if this.getSixes() == INCOMPLETE_ENTRY:
            availableHands.append(HandTypes.Sixes)
        if this.getToK() == INCOMPLETE_ENTRY:
            availableHands.append(HandTypes.ToK)
        if this.getFoK() == INCOMPLETE_ENTRY:
            availableHands.append(HandTypes.FoK)
        if this.getFullHouse() == INCOMPLETE_ENTRY:
            availableHands.append(HandTypes.FH)
        if this.getSmallStraight() == INCOMPLETE_ENTRY:
            availableHands.append(HandTypes.SS)
        if this.getLargeStraight() == INCOMPLETE_ENTRY:
            availableHands.append(HandTypes.LS)
        if this.getYacht() == INCOMPLETE_ENTRY:
            availableHands.append(HandTypes.Yacht)
        if this.getChance() == INCOMPLETE_ENTRY:
            availableHands.append(HandTypes.Yacht)      
        return availableHands

    def __str__(this):
        returnString = "\nYacht Playcard\n\n"
        score = 0
        if this.getOnes() == INCOMPLETE_ENTRY:
            returnString = returnString + "Ones: 0\n"
        else:
            onesScore = this.getOnes()
            score += onesScore
            returnString = returnString + "Ones: " + str(onesScore) + "\n"
        if this.getTwos() == INCOMPLETE_ENTRY:
            returnString = returnString + "Twos: 0\n"
        else:
            twosScore = this.getTwos()
            score += twosScore
            returnString = returnString + "Twos: " + str(twosScore) + "\n"
        if this.getThrees() == INCOMPLETE_ENTRY:
            returnString = returnString + "Threes: 0\n"
        else:
            threesScore = this.getThrees()
            score += threesScore
            returnString = returnString + "Threes: " + str(threesScore) + "\n"
        if this.getFours() == INCOMPLETE_ENTRY:
            returnString = returnString + "Fours: 0\n"
        else:
            foursScore = this.getFours()
            score += foursScore
            returnString = returnString + "Fours: " + str(foursScore) + "\n"
        if this.getFives() == INCOMPLETE_ENTRY:
            returnString = returnString + "Fives: 0\n"
        else:
            fivesScore = this.getFives()
            score += fivesScore
            returnString = returnString + "Fives: " + str(fivesScore) + "\n"
        if this.getSixes() == INCOMPLETE_ENTRY:
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
        if this.getToK() == INCOMPLETE_ENTRY:
            returnString = returnString + "Three of a Kind: 0\n"
        else:
            tokScore = this.getToK()
            score += tokScore
            returnString = returnString + "Three of a Kind: " + str(tokScore) + "\n"
        if this.getFoK() == INCOMPLETE_ENTRY:
            returnString = returnString + "Four of a Kind: 0\n"
        else:
            fokScore = this.getFoK()
            score += fokScore
            returnString = returnString + "Four of a Kind: " + str(fokScore) + "\n"
        if this.getFullHouse() == INCOMPLETE_ENTRY:
            returnString = returnString + "Full House: 0\n"
        else:
            fhScore = this.getFullHouse()
            score += fhScore
            returnString = returnString + "Full House: " + str(fhScore) + "\n"
        if this.getSmallStraight() == INCOMPLETE_ENTRY:
            returnString = returnString + "Small Straight: 0\n"
        else:
            ssScore = this.getSmallStraight()
            score += ssScore
            returnString = returnString + "Small Straight: " + str(ssScore) + "\n"
        if this.getLargeStraight() == INCOMPLETE_ENTRY:
            returnString = returnString + "Large Straight: 0\n"
        else:
            lsScore = this.getLargeStraight()
            score += lsScore
            returnString = returnString + "Large Straight: " + str(lsScore) + "\n"
        if this.getYacht() == INCOMPLETE_ENTRY:
            returnString = returnString + "Yacht: 0\n"
        else:
            yachtScore = this.getYacht()
            score += yachtScore
            returnString = returnString + "Yacht: " + str(yachtScore) + "\n"
        if this.getChance() == INCOMPLETE_ENTRY:
            returnString = returnString + "Chance: 0\n"
        else:
            chanceScore = this.getChance()
            score += chanceScore
            returnString = returnString + "Chance: " + str(chanceScore) + "\n"
        returnString = returnString + "\nTotal Score: " + str(score) +  "\n\n"
        return returnString