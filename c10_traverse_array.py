array = [   1, 
            2, 
            3, 
            [4, 5, 6], 
            7, 
            [8,

                [9, 10, 11,

                    [12, 13, 14]

                ]
            ], 
            [15, 16, 17, 18, 19,

                [20, 21, 22,

                    [23, 24, 25,

                        [26, 27, 29]

                    ], 
                    30,
                    31

                ], 
                32
            ], 
            33
        ]

def traverse_array(array: list) -> None:
    '''Traverse array and print numbers.
    
    Traverse an array at all levels
    and print the value if they're not
    an array themselves. 
        
    Keyword arguments:
    array: the array to be traversed in list format.
    '''
    for entry in array:
        # Check if the current entry is an instance of the
        # list type
        if isinstance(entry, list):
            traverse_array(entry)
        else: 
            print(entry)

traverse_array(array)