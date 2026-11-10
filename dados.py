saldo = 0

import json
import os

ARQUIVO_SALDO = "saldo.json"

def carregar_saldo():
    if not os.path.exists(ARQUIVO_SALDO):
        return 0.0
    with open(ARQUIVO_SALDO, "r", encoding="utf-8") as f:
        return json.load(f)["saldo"]

def salvar_saldo(saldo):
    with open(ARQUIVO_SALDO, "w", encoding="utf-8") as f:
        json.dump({"saldo": saldo}, f, indent=4)


saldo = carregar_saldo()