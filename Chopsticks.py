import sys
import operator

class Namespace: pass
def main(args):
    ## Variables ##
    ns = Namespace()
    ns.num_of_test_cases = 0
    ns.num_of_guests = 0             # Including family
    ns.num_of_chopsticks = 0
    ns.available_chopsticks = []    # Holds all chopsticks that are still sitting in drawer
    ns.original_chopsticks= []     # ALL Chopsticks. Never modified until new test case
    ns.input_list = []

    def populate_list_from_input(file):
        try:
            input = open(file, 'r').read().splitlines()
        except:
            print "Unable to open file"
            exit(3)
        ns.input_list = split_input_file(input)

        # Error Handling *should* be added here, but I am trusting the user for valid inputs.
        ns.num_of_test_cases = int(ns.input_list.pop(0).pop(0))

    def get_test_case_data():
        line = ns.input_list.pop(0)
        ns.num_of_guests = int(line.pop(0))
        ns.num_of_guests += 8 # Add 8 to account for Mr. L's immediate family
        ns.num_of_chopsticks = int(line.pop(0))
        ns.available_chopsticks = ns.input_list.pop(0)
        ns.available_chopsticks = map(int, ns.available_chopsticks) # Convert from str to int
        ns.original_chopsticks = ns.available_chopsticks

    def split_input_file(input):
        list = []
        for item in input:
            temp = item.split(' ')
            list.append(temp)
        return list

    def group_chopsticks():
        potential_sets = []
        pos = 0
        while pos < len(ns.available_chopsticks) - 1:
            temp_group = [ns.available_chopsticks[pos],ns.available_chopsticks[pos + 1]]
            badness = (ns.available_chopsticks[pos] - ns.available_chopsticks[pos + 1]) * (ns.available_chopsticks[pos] - ns.available_chopsticks[pos + 1])
            potential_sets.append([temp_group, badness])
            pos += 1
        return potential_sets

    def get_longer_chopstick(size):
        reversed = ns.available_chopsticks
        reversed.reverse()

        if reversed[0] > size[0] and reversed > size[1]:
            return reversed[0]
        else:
            return None

    def get_barely_longer_chopstick(size):
        set = ns.available_chopsticks
        
        for item in set:
            if item > size[0] and item > size[1]:
                return item
        return None

    def get_largest_badness(list):
        largest = 0

        for item in list:
            if item[1] > largest:
                largest = item[1]
        return largest

    def total_badness(list):
        total = 0
        for item in list:
            total += item[1]
        return total

    # Read in input and assign values
    input_file_location = args[1]
    #input_file_location = "C:/Sample.txt"
    populate_list_from_input(input_file_location)

    # Run X - Test cases
    for testcase in range(ns.num_of_test_cases):
        get_test_case_data()
        table_setting = []
        for guest in range(ns.num_of_guests):
            # Find Neighboring Pairs with lowest badness score
            chopstick_options = group_chopsticks()

            sorted_chopstick_options = sorted(chopstick_options, key=lambda x:(x[1], -x[0][0]))

            chopstick_to_place_on_table = []

            while(True):
                #Remove the longestChopsticks with the lowest Badness score
                chopsticks = sorted_chopstick_options.pop(0)

                #Check that there are chopsticks available that are larger
                #long_chopstick = get_longer_chopstick(chopsticks[0])
                long_chopstick = get_barely_longer_chopstick(chopsticks[0])
                if long_chopstick != None:
                    chopsticks[0].append(long_chopstick)
                    # Remove all used chopsticks
                    ns.available_chopsticks.remove(chopsticks[0][0])
                    ns.available_chopsticks.remove(chopsticks[0][1])
                    ns.available_chopsticks.remove(chopsticks[0][2])
                    chopstick_to_place_on_table = chopsticks
                    break
                else:
                    if len(sorted_chopstick_options) == 0:
                        print "Unable to find longer chopstick"
                        exit(3)
            
            table_setting.append(chopstick_to_place_on_table)

        # Compute largest badness
        print "\n\nTest Case: " + str(testcase)
        print "Total Badness: " + str(total_badness(table_setting))
        print "\nChopstick Pairs: "
        print table_setting
    raw_input()

main(sys.argv)