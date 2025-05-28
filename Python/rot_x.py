from string import ascii_lowercase, ascii_uppercase

def rot_x(st, rot):
    alpha = ascii_lowercase + ascii_uppercase
    if rot > 26:
        rot %= 26
    rot_chars = ascii_lowercase[rot:] + ascii_lowercase[:rot] + ascii_uppercase[rot:] + ascii_uppercase[:rot]
    shift = str.maketrans(alpha, rot_chars)
    return st.translate(shift)