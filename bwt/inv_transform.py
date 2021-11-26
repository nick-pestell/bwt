# TODO parse table back in to recursive function is the whole
# table but needs to be just the bwt transformed message each 
# recurssive call
def build_table(table):
    if len(table[0])<len(table):
        sorted_table = sorted(table)
        for i in range(len(sorted_table)):
            sorted_table[i]+=table[i]
        build_table(sorted_table)
    return sorted_table

def inv_bwt(in_string):
    table = list(in_string)
    output = build_table(table)
    return output