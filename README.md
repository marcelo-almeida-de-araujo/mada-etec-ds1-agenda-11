# Controle de Níveis de Água

Atividade de Recuperação — Agenda 11 — Desenvolvimento de Sistemas I (Etec).

Sistema simples, executado no terminal, que simula o monitoramento de um
reservatório de água. Cada nível é exibido com uma mensagem de alerta e uma
cor diferente, usando a biblioteca [colorama](https://pypi.org/project/colorama/).

| Nível | Situação              | Cor      |
|-------|-----------------------|----------|
| 1     | Muito baixo (crítico) | Vermelho |
| 2     | Baixo                 | Amarelo  |
| 3     | Médio                 | Verde    |
| 4     | Alto                  | Ciano    |
| 5     | Muito alto (alerta)   | Azul     |

## O que o programa faz

- Armazena as mensagens dos cinco níveis em uma **lista**;
- Importa e usa a biblioteca **colorama**;
- Tem a função `definir_cor(nivel)`, que retorna a cor de acordo com o nível;
- Exibe no terminal a situação do reservatório com a cor correspondente;
- Restaura o estilo padrão do terminal com `Style.RESET_ALL` após cada mensagem.

A simulação usa valores definidos no próprio código (não há entrada do usuário).

## Como executar

```bash
pip install -r requirements.txt
python main.py
```
