'''
Module for performing inverse Burrows-Wheelr transform on python strings
'''

def build_table(in_string):
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
        # appends each subsequent character in the transformed input string
        # (in_string) to the string contained in each subsequent element of 
        # the output list (table).
        table = [in_string[i] + table[i] for i in range(len(in_string))]
        # sort the elements of table into lexicographical order
        table.sort()
    return table

def extract_string(table):
    '''
        Returns de-transformed text string given an input table (list)
    '''
    # searches table for the element which with the appended EOF character
    out_string = [x for x in table if x[-1] == bytes.fromhex('7F').decode('utf-8')][0] 
    return out_string[:-1]

def inv_bwt(in_string):
    '''
        Performs BWT inverse transform. Processes transformed string and 
        returns de-transformed string 
    '''
    out_table = build_table(in_string)
    output = extract_string(out_table)
    return output