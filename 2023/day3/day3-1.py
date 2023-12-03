file = open("input.txt", "r")

symbols = []
result = 0 

# find all symbols
for i, line in enumerate(file):
    line_symbols = []
    for i, c in enumerate(line):
        if c.isdigit() == False and c != '.' and c != '\n':
            line_symbols.append(i)
    symbols.append(line_symbols)

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
            match = False
            # check top line
            if i_file > 0:
                for s in symbols[i_file-1]:
                    if s in idx_list:
                        match = True
            # check nb line
            for s in symbols[i_file]:
                if s in idx_list:
                    match = True
            #check bottom line
            if i_file+1 < len(symbols):
                for s in symbols[i_file+1]:
                    if s in idx_list:
                        match = True     
            if match:
                result += int(current_nb_str)
            idx_list = []
            current_nb_str = ""
print(result)
