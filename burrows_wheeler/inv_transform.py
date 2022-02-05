'''
Module for performing inverse Burrows-Wheelr transform on python strings
'''

def build_inv_table(in_string):
    '''
    Returns a table (list) of strings derived from the transformed string

        Parameters:
            in_string (str): transformed input string

        Returns:
            table (list): of length len(in_string), last element contains 
                de-transformed string
    '''
    # TODO: this algorithm is very slow - rewrite
    # create table of empty strings
    table = ['']*len(in_string)
    # Repeats algorithm for len(in_string)
    for i in range(len(in_string)):
        # preppends each subsequent character in the transformed input string
        # (in_string) to the string contained in each subsequent element of 
        # the output list (table).
        table = [in_string[i] + l for i,l in enumerate(table)] # seems like a probem here is that table is re-written everytime this line is executed -> could be why it's so slow.
        # sort the elements of table into lexicographical order
        table.sort()
    return table

def extract_string(table):
    '''
        Returns de-transformed text string given an input table (list)
    '''
    # searches table for the element with the appended EOF character
    out_string = [x for x in table if x[-1] == '\x7f'][0] 
    return out_string[:-1]

def inv_bwt(in_string):
    '''
        Performs BWT inverse transform. Processes transformed string and 
        returns de-transformed string 
    '''
    out_table = build_inv_table(in_string)
    output = extract_string(out_table)
    return output