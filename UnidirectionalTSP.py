import sys

class UnidirectionalTSP: pass
def main(args):
    ## Variables ##
    ns = UnidirectionalTSP()
    ns.input_list = []
    ns.num_of_rows = 0
    ns.num_of_columns = 0
    ns.matrix = []
    ns.cheap_path = []
    ns.cheap_weight = 0

    def get_input(file):
        try:
            input = open(file, 'r').read().splitlines()
        except:
            print "Unable to open file"
            raw_input()
            exit(3)
        return split_input_file(input)

    def split_input_file(input):
        list = []
        for item in input:
            temp = item.split(' ')
            list.append(temp)
        return list

    def convert_2D_list_to_int(list):
        temp = []
        for row in list:
            temp.append(map(int, row))
        return temp

    def pretty_print_2D_list(list):
        for item in list:
            print item

    def get_complete_matrix():
        row = ns.input_list.pop(0)
        ns.num_of_rows = row.pop(0)
        ns.num_of_columns = row.pop(0)
        for i in range(1, ns.num_of_columns):
            ns.matrix.append(ns.input_list.pop(0))

    def DFS_start(matrix):
        for i in range(0, ns.num_of_rows):
            DFS(matrix, [i,0], [], 0)
        
    def DFS(matrix, vertex, path, cost):
        #print "Vertex: " + str(matrix[vertex[0]][vertex[1]])
        node = matrix[vertex[0]][vertex[1]]
        path.append(node)
        cost += node

        for edge in adjacent_edges(vertex[0], vertex[1]):
            if edge == [-1,-1]:
                if cost < ns.cheap_weight or not ns.cheap_path:
                    ns.cheap_weight = cost
                    ns.cheap_path = list(path)
                    print ns.cheap_path
                    print len(ns.cheap_path)
                return

            DFS(matrix, edge, path, cost)
            path.pop()


    def adjacent_edges(row, col):
        # Check to see if it is the last column
        if col == (ns.num_of_columns - 1):            
            return [[-1,-1]]

        edges = []
        # Check to see if we need to loop around to the bottom
        if row == 0: # top
            edges.append([row, col + 1]) # straight
            edges.append([row + 1, col + 1]) # down
            edges.append([ns.num_of_rows - 1 , col + 1]) # up
        elif row == ns.num_of_rows - 1: # bottom:
            edges.append([0, col + 1]) # down
            edges.append([row - 1, col + 1]) # up
            edges.append([row, col + 1]) # straight
        else:
            edges.append([row - 1, col + 1]) # up
            edges.append([row, col + 1]) # straight
            edges.append([row + 1, col + 1]) # down

        return edges

    # Read in input and assign values
    #inputFileLocation = args[1]
    inputFileLocation = "C:/Sample.txt"
    ns.input_list = get_input(inputFileLocation)
    ns.input_list = convert_2D_list_to_int(ns.input_list)
    get_complete_matrix()

    print "ns.num_of_rows: " + str(ns.num_of_rows)
    print "ns.num_of_columns: " + str(ns.num_of_columns)
    print "ns.matrix: "
    pretty_print_2D_list(ns.matrix)
    print "input_list: "
    pretty_print_2D_list(ns.input_list) # For Debugging
    DFS_start(ns.matrix)
    print "ns.cheap_path: "
    print ns.cheap_path
    print ns.cheap_weight
    # Hold CLI open when the program is finished
    raw_input()

main(sys.argv)
