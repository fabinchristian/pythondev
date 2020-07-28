
node_names =  {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H'}


node_coordinates = {
         'A':(0,5),
         'B':(1,0),
         'C':(5,1),
         'D':(2,4),
         'E':(3,6),
         'F':(0,7),
         'G':(4,8),
         'H':(6,2)
           }


weights_node_coordinates = [[0, 20, 0, 0, 0, 0, 15, 0],
             [20, 0, 8, 9, 0, 0, 0, 0],
             [0,  8,  0,  6, 15, 0, 0, 10],
             [0, 9, 6, 0, 7, 0, 0, 0],
             [0, 0, 15, 7, 0, 22, 18, 0],
             [0, 0, 0, 0, 22, 0, 0, 0],
             [15, 0, 0, 0, 18, 0, 0, 0],
             [0, 0, 10, 0, 0, 0, 0, 0]]


node_paths = {
    'A' : [('B',20), ('G', 15)],
    'B' : [('A', 20),('C', 8), ('D', 9)],
    'C' : [('B', 8),('D', 6), ('E', 15), ('H', 10)],
    'D' : [('B', 9),('C', 6),('E', 7)],
    'E' : [('C', 15),('D', 7),('F', 22),('G', 18)],
    'F' : [('E', 22)],
    'G' : [('A', 15),('E', 18)],
    'H' : [('C', 10)]
    }