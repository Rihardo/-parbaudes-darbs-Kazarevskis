# ----------------------------------------------------------------------
# C2. Degviela un braucieni
# ----------------------------------------------------------------------

# Tvertnē ir 50 litri degvielas. Viens brauciens patērē 7 litrus. Izvadi, cik braucienu var veikt un cik degvielas paliek pāri. Visu kodu raksti pats.
#
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas.
# ----------------------------------------------------------------------                                                                                                Katru rezultāta rindu beidz ar punktu.

tvertne = 50
brauciens = 7
while tvertne > brauciens:
    tvertne = tvertne - brauciens
    a = 50 - tvertne
    a = a / brauciens
print("kopa sanāca", a, "braucieni", "un palika", tvertne, "L.")
