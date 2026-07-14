# -*- coding: utf-8 -*-
"""
GUIDA INTERATTIVA: PROGRAMMAZIONE A OGGETTI (OOP) E GESTIONE DELLE ECCEZIONI IN PYTHON

Questo script funge sia da codice di riferimento sia da tutorial eseguibile.
Contiene spiegazioni teoriche integrate nei docstring e tutti gli esempi pratici 
svolti, inclusa l'estensione sulla gestione degli errori avanzata e personalizzata.
"""

def separa_sezione(titolo):
    """Funzione di utilità per formattare l'output nel terminale."""
    print("\n" + "="*80)
    print(f" {titolo} ".center(80, "="))
    print("="*80 + "\n")


# ================================================================================
# 1. FONDAMENTI DELLA PROGRAMMAZIONE A OGGETTI (OOP)
# ================================================================================
separa_sezione("1. FONDAMENTI DELLA OOP & METODI SPECIALI")

class Veicolo:
    """
    Classe Base (o Classe Madre) che definisce un veicolo generico.
    Mostra l'uso del costruttore __init__, del parametro self e dei dunder methods.
    """
    def __init__(self, marca, modello):
        # Inizializzazione degli attributi d'istanza
        self.marca = marca
        self.modello = modello

    def __str__(self):
        """Definisce la stringa restituita quando l'oggetto viene passato a print()."""
        return f"Veicolo: {self.marca} {self.modello}"

    def __repr__(self):
        """Rappresentazione formale dell'oggetto, ottima per il debugging."""
        return f"Veicolo(marca='{self.marca}', modello='{self.modello}')"

# Test della Sezione 1
print("Istanziamo un oggetto Veicolo ed esaminiamo i Dunder Methods:")
veicolo_generico = Veicolo("Fiat", "Panda")
print(f"-> Output di __str__ (print diretto): {veicolo_generico}")
print(f"-> Output di __repr__ (rappresentazione): {repr(veicolo_generico)}")


# ================================================================================
# 2. PARAMETRI OPZIONALI E IL TRABOCCHETTO DEI DEFAULT MUTABILI
# ================================================================================
separa_sezione("2. PARAMETRI OPZIONALI & IL TRABOCCHETTO DEI MUTABILI")

class CanguroSbagliato:
    """
    ATTENZIONE: Questa classe mostra l'errore comune.
    Usando una lista vuota `[]` come default, l'oggetto mutabile viene istanziato 
    una sola volta a compile-time e condiviso da tutte le istanze successive.
    """
    def __init__(self, contenuto_tasca=[]):
        self.contenuto_tasca = contenuto_tasca
        
    def intasca(self, oggetto):
        self.contenuto_tasca.append(oggetto)

class Canguro:
    """
    SOLUZIONE CORRETTA (Pattern 'None'):
    Si usa None come default. All'interno del costruttore si controlla se il parametro
    è None e, in tal caso, si assegna una NUOVA lista vuota all'istanza corrente.
    """
    def __init__(self, contenuto_tasca=None):
        if contenuto_tasca is None:
            self.contenuto_tasca = []  # Nuova lista indipendente in memoria
        else:
            self.contenuto_tasca = contenuto_tasca

    def intasca(self, oggetto):
        self.contenuto_tasca.append(oggetto)

    def __str__(self):
        return f"Canguro con tasca: {self.contenuto_tasca}"

# Test della Sezione 2
print("--- COMPORTAMENTO ERRATO (Default Mutabile []) ---")
cs1 = CanguroSbagliato()
cs2 = CanguroSbagliato()
cs1.intasca("Monete")
print(f"CanguroSbagliato 1 ha: {cs1.contenuto_tasca}")
print(f"CanguroSbagliato 2 ha: {cs2.contenuto_tasca}  <-- Involontariamente modificato!")

print("\n--- COMPORTAMENTO CORRETTO (Default impostato a None) ---")
c1 = Canguro()
c2 = Canguro()
c1.intasca("Mela")
print(f"CanguroCorretto 1 (c1) -> {c1}")
print(f"CanguroCorretto 2 (c2) -> {c2}  <-- Corretto! Resta isolato e vuoto.")


# ================================================================================
# 3. EREDITARIETÀ E POLIMORFISMO
# ================================================================================
separa_sezione("3. EREDITARIETÀ E POLIMORFISMO")

class Auto(Veicolo):
    """Sottoclasse di Veicolo. Mostra l'uso di super() e l'override dei metodi."""
    def __init__(self, marca, modello, numero_porte):
        # super() delega l'inizializzazione di marca e modello alla classe base Veicolo
        super().__init__(marca, modello)
        self.numero_porte = numero_porte

    def __str__(self):
        # Override completo del metodo __str__
        return f"Auto -> {self.marca} {self.modello}, Porte: {self.numero_porte}"

class Moto(Veicolo):
    """Un'altra sottoclasse di Veicolo con un attributo specifico differente."""
    def __init__(self, marca, modello, tipo):
        super().__init__(marca, modello)
        self.tipo = tipo

    def __str__(self):
        return f"Moto -> {self.marca} {self.modello}, Tipo: {self.tipo}"

# Test Ereditarietà Semplice
mia_auto = Auto("Alfa Romeo", "Giulia", 4)
mia_moto = Moto("Ducati", "Monster", "Sportiva")
print("Istanze delle sottoclassi che sovrascrivono il comportamento della classe madre:")
print(mia_auto)
print(mia_moto)

print("\n--- EREDITARIETÀ MULTI-LIVELLO (A CASCATA) ---")

class Poligono:
    def __init__(self, num_lati):
        self.num_lati = num_lati
    def descrizione(self):
        return f"Sono un poligono con {self.num_lati} lati"

class Quadrilatero(Poligono):
    def __init__(self):
        super().__init__(4)  # Passa direttamente 4 alla classe base Poligono
    def descrizione(self):
        return "Sono un quadrilatero"

class Rettangolo(Quadrilatero):
    def __init__(self, base, altezza):
        super().__init__()  # Chiama Quadrilatero (che a sua volta chiama Poligono)
        self.base = base
        self.altezza = altezza
    def descrizione(self):
        # Estende la descrizione della classe madre immediata
        return f"{super().descrizione()} con base {self.base} e altezza {self.altezza}"
    def area(self):
        return self.base * self.altezza
    def perimetro(self):
        return 2 * (self.base + self.altezza)

# Test Ereditarietà Multi-livello
rett = Rettangolo(10, 5)
print(rett.descrizione())
print(f"Area Calcolata: {rett.area()} | Perimetro Calcolato: {rett.perimetro()}")


# ================================================================================
# 4. GESTIONE DEGLI ERRORI E DELLE ECCEZIONI
# ================================================================================
separa_sezione("4. GESTIONE DELLE ECCEZIONI E ERRORI PERSONALIZZATI")

class TascaTroppoPienaError(Exception):
    """
    Eccezione personalizzata (Custom Exception).
    Eredita dalla classe nativa Exception per definire un errore specifico di dominio.
    """
    def __init__(self, limite, messaggio="La tasca del canguro ha superato la capienza massima!"):
        self.limite = limite
        super().__init__(f"{messaggio} (Limite: {limite} oggetti consentiti)")

class CanguroConLimite(Canguro):
    """Estensione di Canguro che integra un controllo di sicurezza con eccezioni."""
    def __init__(self, limite_oggetti=2, contenuto_tasca=None):
        super().__init__(contenido_tasca)
        self.limite_oggetti = limite_oggetti

    def intasca(self, oggetto):
        # Controllo della regola di business prima di inserire l'oggetto
        if len(self.contenuto_tasca) >= self.limite_oggetti:
            # Sollevamento forzato dell'eccezione mirata
            raise TascaTroppoPienaError(self.limite_oggetti)
        super().intasca(oggetto)

# Esecuzione e gestione tramite blocco strutturato: try-except-else-finally
kanga = CanguroConLimite(limite_oggetti=2)

print("Esecuzione guidata del blocco Try-Except-Else-Finally:")
try:
    print("-> Inserisco oggetto 1: 'Occhiali'")
    kanga.intasca("Occhiali")
    print("-> Inserisco oggetto 2: 'Chiavi'")
    kanga.intasca("Chiavi")
    print("-> Inserisco oggetto 3: 'Mappa' (Questo causerà il raise dell'errore)")
    kanga.intasca("Mappa")
except TascaTroppoPienaError as e:
    # Gestione mirata dell'errore personalizzato
    print(f"[ECCEZIONE INTERCETTATA] Errore specifico: {e}")
except Exception as e:
    # Fallback per qualsiasi altro tipo di errore imprevisto
    print(f"[ECCEZIONE INTERCETTATA] Errore generico: {e}")
else:
    # Viene eseguito solo se tutto nel blocco try va a buon fine
    print("[SUCCESS] Tutti gli elementi inseriti senza eccezioni!")
finally:
    # Viene eseguito SEMPRE, utile per ripulire lo stato o chiudere connessioni/file
    print(f"[FINALLY] Operazione terminata. Stato finale della tasca: {kanga.contenuto_tasca}")

print("\n" + "="*80)
print(" SCRIPT CONCLUSO CON SUCCESSO ".center(80, "#"))
print("="*80)
