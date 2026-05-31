import matplotlib.pyplot as plt
from transmission import Transmission

# Tests.

def tests_transmission_valeurs() -> None:
    print("## Test: transmission_temperature_humidite - Début.")

    t1 = Transmission("0010101011001000010010001100011000101101")
    assert t1.get_temperature() == 26.4
    assert t1.get_humidite() == 62, t1.get_humidite()

    assert t1.est_valide()

    print("## Test: transmission_temperature_humidite - Passé.")

def main() -> None:
    tests_transmission_valeurs()

    # Extraction des données
    with open("data.txt", "r") as f:
        trames: list[str] = f.read().split("\n")
        trames.pop()  # La dernière ligne est vide, on la supprime

    # Création d'une liste de températures pour les transmissions valides
    transmissions: list[Transmission] = [Transmission(t) for t in trames]
    temperatures: list[float | None] = [t.get_temperature() for t in transmissions if t.est_valide()]

    print(f"Nombre de trames reçues : {len(trames)}")
    print(f"Nombre de trames valides : {len(temperatures)}")

    # Affichage des températures
    plt.figure(figsize=(10, 5))
    plt.plot(temperatures, label="Température (°C)")  # pyright: ignore[reportArgumentType]
    plt.title("Évolution de la température")
    plt.xlabel("Mesures")
    plt.ylabel("Température (°C)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
