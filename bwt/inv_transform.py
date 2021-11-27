def build_table(in_string):
    table = ['']*len(in_string)
    for i in range(len(in_string)):
        table = [in_string[i] + table[i] for i in range(len(in_string))]
        table.sort()
    return table

def extract_string(table):
    out_string = [x for x in table if x[-1] == bytes.fromhex('7F').decode('utf-8')][0] 
    return out_string[:-1]

def inv_bwt(in_string):
    out_table = build_table(in_string)
    output = extract_string(out_table)
    return output