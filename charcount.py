# Modulo di python che permette di gestire i file indipendentemente dal tipo
# di sistema operativo che si utilizza.
import os
# Modulo di python che rende semplice scrivere comandi di linea di interfaccia,
# genera automaticamente messaggi di aiuto, utilizzo ed errore.
import argparse
# Modulo di python che permette di seguire al meglio il corso d'esecuzione di
# un programma in python e scovarne bug e potenziali difetti.
# (da usare preferibilmente al posto del semplice print)
import logging
# Esegue la configurazione di base per il sistema di logging.
logging.basicConfig(level=logging.INFO)

# Creo un stringa.
_description = 'Measure the releative frequencies of letters in a text file'


# Definisco una funzione chiamata process che vuole come argomento il
# path di un file.
def process(file_path):
    """Main processing method.
    Basic sanity check: make sure that the file_argument points to an
    existing text file.
    Questa funzione permette di generare un errore se una condizione e' falsa,
    la prima condizione verifica che il file e' un file di testo
    """
    assert file_path.endswith('.txt')
    """ La seconda condizione verifica se il path specificato e' un file
    esistente oppure no.
    """
    assert os.path.isfile(file_path)

    # Open the input file (note that we are taking advantage of context
    # management, using a with statement).

    # Printa un messaggio d'informazione
    logging.info('Opening input file "%s"', file_path)
    # Usiamo il with per rendere il codice piu' leggibile
    with open(file_path) as input_file:
        # Crea una varibile con il testo del file
        data = input_file.read()
    #Printa un messaggio d'informazione
    logging.info('Done. %d character(s) found.', len(data))

    # Prepare a dictionary to hold the letter frequencies, and initialize
    # all the counts to zero.
    # Crea un stringa con tutte le lettere nell'alfabeto.
    letters = 'abcdefghijklmnopqrstuvxyz'
    # Crea un dizionario chiamato freq_dict.
    freq_dict = {}
    # Riempie il dizionario con le lettere nella stringa e setta i valori
    # di ogni chiave a zero.
    for ch in letters:
        freq_dict[ch] = 0

    # Loop over the input data (note the call to the lower() string method
    # that is casting everything in lower case).

    # Legge lettera per lettera il testo in modalita' lower e ogni volta che
    # incontra una lettera nell'alfabeto aumenta di uno il valore della chiave
    # corrispondente.
    for ch in data.lower():
        if ch in letters:
            freq_dict[ch] += 1

    # One last loop over the letters to normalize the occurrences to 1.

    # Conta tutti i valori delle lettere nel dizionario.
    # (Lettere totali nel testo)
    num_chars = float(sum(freq_dict.values()))
    # Divide ogni valore di ogni chiave per le lettere totali del
    # dizionario.
    for ch in letters:
        freq_dict[ch] /= num_chars

    # We're done---print the glorious output. (And here it is appropriate to
    # use print() instead of logging.)

    # Printa le percentuali di frequenza delle lettere nel testo.
    for ch, freq in freq_dict.items():
        print('{}: {:.3f}%'.format(ch, freq * 100.))

    

# Quando Python egue del codice, tra leprime cose che faassegna alcune variabili
# speciali, tra cui troviamo anche la variabile __name__ .
# Questa condizione verifica se il nostro codice sta venendo eseguito come
# script a se stante, oppure sta venendo richiamato come modulo in un altro
# programma.
if __name__ == '__main__':
    # Tiene conto di tutte le informazioni necessarie per analizzare la linea
    # di comando.
    parser = argparse.ArgumentParser(description=_description)
    # Riempie l'ArgumentParser con tutte le informazioni sugli argomenti del
    # programma
    parser.add_argument('infile', help='path to the input file')
    # Analizza gli argomenti 
    args = parser.parse_args()
    # Esegue la funzione 
    process(args.infile)
