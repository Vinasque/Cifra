def cifra_reversa(mensagem):
    resultado = ""
    caracteres_restantes = len(mensagem) - 1

    while caracteres_restantes >= 0:
        resultado = resultado + mensagem[caracteres_restantes]
        caracteres_restantes = caracteres_restantes - 1
    return resultado

def cifra_de_cesar(mensagem, modo, chave):
    resultado = ""

    for caractere in mensagem:

        indice_caractere = dicionario.find(caractere)

        if caractere in dicionario:
            if modo == "encriptar":
                indice_corrigido = indice_caractere + chave
            elif modo == "decriptar":
                indice_corrigido = indice_caractere - chave
            
            # Corrigir os casos especiais

            if indice_corrigido >= len(dicionario):
                indice_corrigido = indice_corrigido - len(dicionario)
            elif indice_corrigido < 0:
                indice_corrigido = indice_corrigido + len(dicionario)

            resultado = resultado + dicionario[indice_corrigido]
        else:
            resultado = resultado + caractere

    return resultado

dicionario = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.,"
