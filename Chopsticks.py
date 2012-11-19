import sys
import operator

class Namespace: pass
def main(args):
    ## Variables ##
    ns = Namespace()
    ns.numOfTestCases = 0
    ns.numOfGuests = 0             # Including family
    ns.numOfChopsticks = 0
    ns.availableChopsticks = []    # Holds all chopsticks that are still sitting in drawer
    ns.originalChopsticks= []     # ALL Chopsticks. Never modified until new test case
    ns.inputList = []

    def populateListFromInput(file):
        try:
            input = open(file, 'r').read().splitlines()
        except:
            print "Unable to open file"
            exit(3)
        ns.inputList = splitInputFile(input)

        # Error Handling *should* be added here, but I am trusting the user for valid inputs.
        ns.numOfTestCases = int(ns.inputList.pop(0).pop(0))

    def getTestCaseData():
        line = ns.inputList.pop(0)
        ns.numOfGuests = int(line.pop(0))
        ns.numOfGuests += 8 # Add 8 to account for Mr. L's immediate family
        ns.numOfChopsticks = int(line.pop(0))
        ns.availableChopsticks = ns.inputList.pop(0)
        ns.availableChopsticks = map(int, ns.availableChopsticks) # Convert from str to int
        ns.originalChopsticks = ns.availableChopsticks

    def splitInputFile(input):
        list = []
        for item in input:
            temp = item.split(' ')
            list.append(temp)
        return list

    def groupChopsticks():
        potentialSets = []
        pos = 0
        while pos < len(ns.availableChopsticks) - 1:
            tempGroup = [ns.availableChopsticks[pos],ns.availableChopsticks[pos + 1]]
            badness = (ns.availableChopsticks[pos] - ns.availableChopsticks[pos + 1]) * (ns.availableChopsticks[pos] - ns.availableChopsticks[pos + 1])
            potentialSets.append([tempGroup, badness])
            pos += 1
        return potentialSets

    def getLongerChopstick(size):
        reversed = ns.availableChopsticks
        reversed.reverse()

        if reversed[0] > size[0] and reversed > size[1]:
            return reversed[0]
        else:
            return None

    def getBarelyLongerChopstick(size):
        set = ns.availableChopsticks
        
        for item in set:
            if item > size[0] and item > size[1]:
                return item
        return None

    def getLargestBadness(list):
        largest = 0

        for item in list:
            if item[1] > largest:
                largest = item[1]
        return largest

    def totalBadness(list):
        total = 0
        for item in list:
            total += item[1]
        return total

    # Read in input and assign values
    inputFileLocation = args[1]
    #inputFileLocation = "C:/Sample.txt"
    populateListFromInput(inputFileLocation)

    # Run X - Test cases
    for testcase in range(ns.numOfTestCases):
        getTestCaseData()
        tableSetting = []
        for guest in range(ns.numOfGuests):
            # Find Neighboring Pairs with lowest badness score
            chopstickOptions = groupChopsticks()

            sortedChopstickOptions = sorted(chopstickOptions, key=lambda x:(x[1], -x[0][0]))

            chopstickToPlaceOnTable = []
            bool = True
            while(bool):
                #Remove the longestChopsticks with the lowest Badness score
                chopsticks = sortedChopstickOptions.pop(0)

                #Check that there are chopsticks available that are larger
                #longChopstick = getLongerChopstick(chopsticks[0])
                longChopstick = getBarelyLongerChopstick(chopsticks[0])
                if longChopstick != None:
                    chopsticks[0].append(longChopstick)
                    # Remove all used chopsticks
                    ns.availableChopsticks.remove(chopsticks[0][0])
                    ns.availableChopsticks.remove(chopsticks[0][1])
                    ns.availableChopsticks.remove(chopsticks[0][2])
                    bool = False
                    chopstickToPlaceOnTable = chopsticks
                else:
                    if len(sortedChopstickOptions) == 0:
                        print "Unable to find longer chopstick"
                        exit(3)
            
            tableSetting.append(chopstickToPlaceOnTable)

        # Compute largest badness
        print "\n\nTest Case: " + str(testcase)
        print "Total Badness: " + str(totalBadness(tableSetting))
        print "\nChopstick Pairs: "
        print tableSetting
    raw_input()

main(sys.argv)