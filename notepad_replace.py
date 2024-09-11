from Npp import editor

def replace(match):
    col = int(match.group(2))
    if (col > 1):
        return 'S2_Q' + match.group(1) + '_' + str(col - 1)
    else:
        if (col == 1):
            return 'S2_Q' + match.group(1) + '_C' + str(col)
    return 'S2_Q' + match.group(1) + '_' + str(col)

editor.rereplace('txt_S2_R(\d{1,2})_Q(\d)', replace)
