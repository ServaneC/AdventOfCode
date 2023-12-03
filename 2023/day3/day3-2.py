file = open("input.txt", "r")

symbols = []
matching = []
result = 0 

# find all * 
for i, line in enumerate(file):
    line_symbols = []
    match_array = []
    for i, c in enumerate(line):
        if c == '*':
            line_symbols.append(i)
            match_array.append([])
    symbols.append(line_symbols)
    matching.append(match_array)


file.seek(0)
for i_file, line in enumerate(file):
    current_nb_str = ""
    idx_list = []
    for i_line, c in enumerate(line):
        if c.isdigit():
            current_nb_str += c
            idx_list.append(i_line)
        elif current_nb_str != "":
            idx_list.append(idx_list[-1] + 1)
            idx_list.append(idx_list[0] - 1)
            # check top line
            if i_file > 0:
                for i_s, s in enumerate(symbols[i_file-1]):
                    if s in idx_list:
                        matching[i_file-1][i_s].append(int(current_nb_str))
            # check nb line
            for i_s, s in enumerate(symbols[i_file]):
                if s in idx_list:
                    matching[i_file][i_s].append(int(current_nb_str))
            #check bottom line
            if i_file+1 < len(symbols):
                for i_s, s in enumerate(symbols[i_file+1]):
                    if s in idx_list:
                        matching[i_file+1][i_s].append(int(current_nb_str))
            idx_list = []
            current_nb_str = ""

for line in matching:
    for m in line:
        if len(m) == 2:
            result += m[0] * m[1]

print(result)
