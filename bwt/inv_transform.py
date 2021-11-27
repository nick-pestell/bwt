def build_table(in_string):
    table = ['']*len(in_string)
    for i in range(len(in_string)):
        table = sorted([table[i] + in_string[i] for i in range(len(in_string))])
    return table

def inv_bwt(in_string):
    output = build_table(in_string)
    return output