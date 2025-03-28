from string import ascii_letters

def rot_x(st, rot):
    return "".join(
    chr((ord(c) - 97 + rot) % 26 + 97) if c in ascii_letters and c.islower() else
    chr((ord(c) - 65 + rot) % 26 + 65) if c in ascii_letters and c.isupper() else c
    for c in st
)


rot_x("A man, a plan, a canal: Panama")