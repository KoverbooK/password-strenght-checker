def check(mdp) :

    # Init
    score=lowerCase=digit=upperCase=special=0
    if (taille:=len(mdp)) == 0 :
        return 0
    set_mdp = set(mdp)
    proportion = len(set_mdp)/taille
    err_mess=""

    # Longueur du mdp
    if taille > 8 :
        score+=2
    else :
        err_mess+="-Trop court\n"

    # Different charactère
    if proportion >= 0.9 :
        score+=2
    elif proportion >=0.7 :
        score+=1
        err_mess+="-Quelques répétitions\n"
    else :
        err_mess+="-Trop de répétitions\n"

    # Compter les types
    for c in mdp :
        if c.islower():
            lowerCase+=1
        elif c.isupper():
            upperCase+=1
        elif c.isdigit():
            digit+=1
        else:
            special+=1

    # Scorer les types
    if (lowerCase+upperCase)/taille >= 0.5 :
        score+=1
    else :
        err_mess+="-Pas assez de Lettres\n"
    if special/taille >= 0.2 :
        score+=1
    else :
        err_mess+="-Pas assez de caractères spéciaux\n"
    if digit/taille >= 0.1 :
        score+=1
    else :
        err_mess+="-Pas assez de chiffres\n"

    # Correlation des types (low, upp, spé, digit)
    corr = (corrType(mdp) + corrType(mdp, 2) + corrType(mdp, 3))/3
    if corr < 0.5 :
        score+=1
    elif corr > 0.7 :
        score-=1
        err_mess+="-Pattern prévisible (Beta)"

    err_mess = "-Pas d'erreur trouvée\n" if err_mess == "" else err_mess

    return score, err_mess

def corrType(mdp, lag=1):
    def t(c):
        if c.islower(): return 0
        if c.isupper(): return 1
        if c.isdigit(): return 2
        return 3

    types = [t(c) for c in mdp]
    if len(types) <= lag:
        return 0

    matches = sum(
        1 for i in range(len(types) - lag)
        if types[i] == types[i + lag]
    )

    return matches / (len(types) - lag)



GOOD = ["QpR7!xL9@", "e3-+sVnKr*,8V]<~", "A5?5ts0C|f#=LO0I", "H*4#qYvi5b]<q@s=", "+/<5480H!{ep5)a~", "1rn!3MWf{%5DFgMk", ")TYD1q]CANDmyE7", "|W<&A`Mw2-e2+jxC", "QBX8Af?0?G/Gg%w<", "|wity<%Uy1u9BL1D", "3ky-b,W~<~[A*WPO", "MdSS@#{}khy1GF^R", "*b9GoSv~l1KLp8gE", ").VkLUF(N_w_P=c1"]

# TEST ____________________________

import argparse
from getpass import getpass

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Mesure la force d'un mot de passe, notée sur 8.")
    parser.add_argument("--mdp", type=str, help="Mot de passe à tester")
    parser.add_argument("--secure-mode", action="store_true", help="Saisie sécurisée du mot de passe")
    parser.add_argument("--advice", action="store_true", help="Conseil d'amélioration")

    args = parser.parse_args()
    mdp = None

    if args.mdp:
        mdp = args.mdp
        print(f" *\n* *\nScore pour {mdp} : {check(mdp)[0]} / 8")

    elif args.secure_mode :
        mdp = getpass("Entrer le mot de passe en discrétion : ")
        print(f" *\n* *\nScore pour [secret-mode] : {check(mdp)[0]} / 8")

    else :
        print("--EXEMPLE--")
        for code in GOOD :
            print(f"{code} : {check(code)[0]}/8")

    if args.advice and mdp != None :
        print(f" *\n* *\nConseil d'amélioration :\n{check(mdp)[1]}")

    else :
        print(f" *\n* *\nPas de conseils sans mot de passe")
