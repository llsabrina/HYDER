from pathlib import Path
import logging
import pandas as pd

logging.basicConfig(filename='pipeline_test.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    vari = Path("C:/Users/sabri/Desktop/up level/python/hyder/")

    save_relatorio = []

    for arquivo in vari.glob("matriculas_*.csv"):
        df_alunos = pd.read_csv(arquivo)
        mes = arquivo.stem.split("_")[1]
        df_alunos["mes"] = mes
        save_relatorio.append(df_alunos)
        logging.info("Arquivo processado: %s", arquivo)

    df_final = pd.concat(save_relatorio)
    df_final.to_csv("C:/Users/sabri/Desktop/up level/python/hyder/hyder_relatorio.csv", index=False)
    print(len(df_final), "linhas processadas e salvas no arquivo hyder_relatorio.csv")
    logging.info("Relatório gerado com sucesso!")

    df_ativos = df_final[df_final["status"] == "ativo"]
    mensalidade_ativos = df_ativos["mensalidade"].sum()
    total_ativos = len(df_ativos)

    logging.info("Total da mensalidade dos alunos ativos: %d", mensalidade_ativos)
    logging.info("Total de alunos ativos: %d", total_ativos)

    df_desistentes = df_final[df_final["status"] == "desistente"]
    total_desistentes = len(df_desistentes)
    logging.info("Total de alunos desistentes: %d", total_desistentes)
    df_trancados = df_final[df_final["status"] == "trancado"]
    total_trancados = len(df_trancados)
    logging.info("Total de alunos trancados: %d", total_trancados)

except Exception as e:
    logging.error("Erro ao processar arquivos: %s", str(e))


