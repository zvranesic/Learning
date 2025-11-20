import random


def igra_kamen_skarje_papir():
    # Definicija možnih izbir
    moznosti = ["kamen", "škarje", "papir"]

    # Pozdrav in navodila
    print("👋 Dobrodošel/došla v igri Kamen, Škarje, Papir!")
    print("Izberi: kamen, škarje ali papir. Za izhod vpiši 'izhod'.")
    print("-" * 30)

    # Glavna zanka igre
    while True:
        # 1. Uporabnikov vnos
        uporabnikova_izbira = input(
            "Tvoja izbira (kamen/škarje/papir/izhod): ").lower()

        # Preverjanje za izhod
        if uporabnikova_izbira == "izhod":
            print("Hvala za igro! Se vidimo kmalu. 😉")
            break

        # Preverjanje veljavnosti vnosa
        if uporabnikova_izbira not in moznosti:
            print("❌ Neveljaven vnos. Prosim, izberi 'kamen', 'škarje' ali 'papir'.")
            continue

        # 2. Računalnikova izbira
        racunalnikova_izbira = random.choice(moznosti)
        print(
            f"🤖 Računalnik je izbral: **{racunalnikova_izbira.capitalize()}**")

        # 3. Določitev zmagovalca
        rezultat = ""

        # Neodločeno
        if uporabnikova_izbira == racunalnikova_izbira:
            rezultat = "Neodločeno!"

        # Zmaga uporabnika
        elif (uporabnikova_izbira == "kamen" and racunalnikova_izbira == "škarje") or \
             (uporabnikova_izbira == "škarje" and racunalnikova_izbira == "papir") or \
             (uporabnikova_izbira == "papir" and racunalnikova_izbira == "kamen"):
            rezultat = "🎉 Čestitam! Zmagal/a si!"

        # Zmaga računalnika
        else:
            rezultat = "😔 Žal mi je, računalnik je zmagal."

        # Izpis rezultata
        print(f"➡️  **{rezultat}**")
        print("-" * 30)


# Zaženemo igro
if __name__ == "__main__":
    igra_kamen_skarje_papir()
