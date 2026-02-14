def convert_to_binary(number: int) -> str:
    """
    Converte un numero intero positivo nella sua rappresentazione binaria
    utilizzando un approccio ricorsivo.
    """

    # Controllo di guardia: previene input non validi
    if number < 0:
        raise ValueError("Il numero deve essere un intero positivo.")

    # 1. CASO BASE:
    # È la condizione di uscita. Senza di questa, la funzione continuerebbe
    # a chiamarsi all'infinito (causando un RecursionError).
    # Se il numero è 0 o 1, la sua rappresentazione binaria è il numero stesso.
    if number < 2:
        return str(number)

    # 2. PASSO RICORSIVO:
    # Dividiamo il problema in due parti:
    # - La chiamata ricorsiva: 'number // 2' (divisione intera) sposta il calcolo
    #   verso il caso base.
    # - L'operazione corrente: 'number % 2' (modulo) calcola il resto (0 o 1),
    #   ovvero l'ultima cifra binaria a destra.
    return convert_to_binary(number // 2) + str(number % 2)

print(convert_to_binary(123))