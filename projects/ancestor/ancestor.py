
def earliest_ancestor(ancestors, starting_node):
    #pass
    #print(ancestors[0][0])# parent
    #print(ancestors[0][1])# child
    #print(starting_node)#the child or parent you start on to work you way up
    #could I use a dictinary key set?
    # keys = [child: [parent 1, parent 2]] MAKE DECENDING so I only check lowest
    keys = {"count": 0}
    for values in ancestors:
        try:
            hold_test = keys[ str(values[1]) ]
            #print("try worked")
            hold_test.append(values[0])
            sorted(hold_test)
        except KeyError:
            #print("try failed")
            keys[ str(values[1]) ] = []
            keys[ str(values[1]) ].append(values[0])

    #print(keys)
    #print(keys[ str(starting_node) ])

    def recusion(key_to_check_for):
        try:
            #print(keys[ str(key_to_check_for) ][0])
            hold = keys[ str(key_to_check_for) ]
            keys["count"] += 1
            recusion(keys[ str(key_to_check_for) ][0])
        except KeyError:
            #print(f"recusion faild {key_to_check_for}")
            #print(key_to_check_for)
            if keys["count"] > 0:
                keys["result"] = key_to_check_for
            else:
                keys["result"] = -1


    recusion(starting_node)
    return keys["result"]


    #filter by loop or recusion up the family tree

    #Write a function (sugest recursion prefered)
    #returns their earliest known ancestor(farthest distance from the input individual)
        #If more than one | return the one with the lowest numeric ID
        #If the input individual has no parents, the function should return -1.
