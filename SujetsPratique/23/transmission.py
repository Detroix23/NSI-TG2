class Transmission:
    _id: int | None
    _temperature: float | None
    _humidite: int | None
    _trame: str


    def __init__(self, trame: str) -> None:
        self._id = None
        self._temperature = None
        self._humidite = None
        self._trame = trame

        self.decoder()

    def __repr__(self) -> str:
        """ Méthode permettant l'affichage """
        return f"ID : {self._id} / Temp. : {self._temperature}°C / Hum. : {self._humidite}%"

    def decoder(self) -> None:
        self.decoder_id()
        self.decoder_temperature()
        self.decoder_humidite()

    def decoder_id(self) -> None:
        # int(s, 2) : conversion binaire -> décimal
        self._id = int(self._trame[0:8], 2)

    def decoder_temperature(self) -> None:
        temperature: float = (int(self._trame[16:28], 2) - 900) / 10
        self._temperature = (temperature
            if temperature >= -10
            else None
        ) 
    
    def decoder_humidite(self) -> None:
        humidite: int
        if self._trame[28:36] == "10100000":
            humidite = 100
        else:
            humidite = int(self._trame[28:32], 2) * 10 + int(self._trame[32: 36], 2)
        
        self._humidite = humidite
    
    def get_id(self) -> int | None:
        return self._id

    def get_temperature(self) -> float | None:
        return self._temperature

    def get_humidite(self) -> int | None:
        return self._humidite

    def est_valide(self) -> bool:
        if len(self._trame) != 40:
            return False

        # Comptage de `1`s et parité.
        even_id: int = count_character(self._trame[0: 8], "1") % 2
        even_key: int = count_character(self._trame[8: 16], "1") % 2
        even_temperature: int = count_character(self._trame[16: 28], "1") % 2
        even_humidity: int = count_character(self._trame[28: 36], "1") % 2

        #print(f"C: {even_id}{even_key}{even_temperature}{even_humidity}")
        #print(f"V: {self._trame[36:40]}")
        
        return (
            even_id == int(self._trame[36])
            and even_key == int(self._trame[37])
            and even_temperature == int(self._trame[38])
            and even_humidity == int(self._trame[39])
        )

def count_character(string: str, character: str) -> int:
    """
    Compte les occurences de `character` dans `string`.
    """
    count: int = 0
    for sub in string:
        if sub == character:
            count += 1
    
    return count
