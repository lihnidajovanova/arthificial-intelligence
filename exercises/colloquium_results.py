"""
Резултати од колоквиуми Problem 5 (2 / 29)
Од стандарден влез се чита природен број _n_, а потоа и податоци за _n_ студенти - резултати од колоквиуми по предметот
Вештачка интелигенција. Податоците да се зачуваат во листа од речници, каде што секој речник ќе ги содржи податоците за
еден студент: индексот на студентот, името на предметот, како и бројот на поени што ги освоил студентот на првиот
односно вториот колоквиум, соодветно. Форматот на секој речник е следниот:

{'indeks' : _brojIndeks_, 'predmet' : _'Veshtachka inteligencija'_, 'Kolokvium 1' : _brojPoeni1_, 'Kolokvium 2' : _brojPoeni2_}

каде што _brojIndeks_, _brojPoeni1_ и _brojPoeni2_ се податоците за студентот (прочитани од стандарден влез).

Да се дефинира функција suma_kolokviumi(), која на влез прима еден аргумент – листа од речници со податоци за студенти
(како што беше опишано погоре), а како резултат ја враќа истата листа, но во која секој речник е променет т.ш. наместо
податоците за секој од двата колоквиуми ќе го содржи само вкупниот резултат (збирот на поени) од колоквиумите. Повикајте
ја оваа функција за листата од речници со податоците прочитани од стандарден влез. Резултатот од функцискиот повик
испечатете го на стандарден излез.
"""


def suma_kolokviumi(rezultati):
    for student in rezultati:
        student["Vkupno od kolokviumi"] = student["Kolokvium 1"] + student["Kolokvium 2"]
        del student["Kolokvium 1"]
        del student["Kolokvium 2"]

    return rezultati


if __name__ == "__main__":
    n = int(input())
    results = []  # ova e listata od rechnici
    for i in range(0, n):
        r = {}  # rechnik koj kje chuva podatoci za eden student
        brojIndeks = input()
        brojPoeni1 = float(input())
        brojPoeni2 = float(input())
        r["indeks"] = brojIndeks
        r["Predmet"] = "Veshtachka inteligencija"
        r["Kolokvium 1"] = brojPoeni1
        r["Kolokvium 2"] = brojPoeni2
        results.append(r)

    print(suma_kolokviumi(results))
