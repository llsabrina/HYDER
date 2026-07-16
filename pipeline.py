from pathlib import Path
import logging
import pandas as pd

logging.basicConfig(filename='pipeline_test.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    vari = Path("C:/Users/sabri/Desktop/up level/python/hyder/")

    save_relatorio = []

    for arquivo in vari.glob("*.csv"):
        df_alunos = pd.read_csv(arquivo)
        mes = arquivo.stem.split("_")[1]
        df_alunos["mes"] = mes
        save_relatorio.append(df_alunos)
        logging.info("Arquivo processado: %s", arquivo)

    pd.concat(save_relatorio).to_csv("C:/Users/sabri/Desktop/up level/python/hyder/hyder_relatorio.csv", index=False)
    logging.info("Relatório gerado com sucesso!")
except Exception as e:
    logging.error("Erro ao processar arquivos: %s", str(e))