"""
Controle de Níveis de Água
Simulação de um sistema de monitoramento de reservatório no terminal.
Cada nível de água é exibido com uma mensagem de alerta e uma cor
específica, usando a biblioteca colorama.
"""

import time

from colorama import Fore, Style, init

# Inicializa o colorama (necessário para as cores funcionarem no Windows)
init()

# Lista com os cinco níveis do reservatório, do mais baixo ao máximo
niveis = [
    "Nível 1 - Muito baixo (CRÍTICO): risco de falta de água!",
    "Nível 2 - Baixo: atenção ao consumo.",
    "Nível 3 - Médio: abastecimento normal.",
    "Nível 4 - Alto: reservatório quase cheio.",
    "Nível 5 - Muito alto (ALERTA): risco de transbordamento!",
]


def definir_cor(nivel):
    """Retorna a cor correspondente ao nível informado (1 a 5)."""
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE


def exibir_situacao(nivel):
    """Exibe a situação do reservatório com a cor do nível."""
    cor = definir_cor(nivel)
    mensagem = niveis[nivel - 1]
    print(cor + Style.BRIGHT + mensagem + Style.RESET_ALL)


def main():
    print("=" * 60)
    print("   SISTEMA DE MONITORAMENTO DO RESERVATÓRIO DE ÁGUA")
    print("=" * 60)

    # Simulação: o reservatório enchendo do nível 1 até o nível 5
    print("\nSimulação das leituras do sensor:\n")
    for nivel in range(1, len(niveis) + 1):
        print(f"Leitura {nivel}: ", end="")
        exibir_situacao(nivel)
        time.sleep(1)

    # Nível atual definido no código (sem entrada do usuário)
    nivel_atual = 3
    print("\n" + "-" * 60)
    print("Situação atual do reservatório:")
    exibir_situacao(nivel_atual)
    print("-" * 60)

    # Garante que o terminal volte ao estilo padrão
    print(Style.RESET_ALL + "Monitoramento finalizado.")


if __name__ == "__main__":
    main()
