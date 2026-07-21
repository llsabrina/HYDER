## 🎓 Projeto Hyder
## 📌 Sobre o projeto

Projeto criado do zero com dados de uma universidade fictícia chamada Hyder, desenvolvida com o propósito de automatizar processos de ingressos e evasões. O sistema controla o lucro total gerado pelos alunos ativos ao longo de 4 meses (janeiro a abril), além de contabilizar o total de trancamentos e desistências no período.

## 🎯 Objetivo

O projeto Hyder nasceu da necessidade de leitura rápida de dados para um fechamento ágil e confiável todos os dias, oferecendo cálculo, filtragem e rotas de erro de forma automática a cada execução.

O pipeline foi construído para ser idempotente: pode ser executado múltiplas vezes sem gerar dados duplicados, garantindo confiabilidade no processo de fechamento diário.

## 🛠️ Tecnologias utilizadas
🐍 Linguagem:  Python
📚 Bibliotecas: Pandas, logging, pathlib
🐙 Versionamento: Git, GitHub

## 📂 Estrutura de dados

Entrada — matriculas_janeiro.csv, matriculas_fevereiro.csv, matriculas_marco.csv, matriculas_abril.csv:

id_aluno, nome, curso, semestre, status, mensalidade

Saída — hyder_relatorio.csv (consolidado dos 4 meses):

id_aluno, nome, curso, semestre, status, mensalidade, mes

## 📊 Resultados
💰 Mensalidade total (alunos ativos): R$ 98.500,00
✅ Alunos ativos: 47
❌ Desistentes: 4
🔒 Trancados: 2
📁 Total processado: 53 registros (jan-abr)

## 🚀 Como executar
Clone o repositório
Instale as dependências: pip install pandas
Coloque os arquivos matriculas_*.csv na pasta do projeto
Execute: python pipeline_hyder.py
O relatório consolidado será gerado em hyder_relatorio.csv

## 🔜 Próximos passos
Análise avançada em SQL
Dashboard interativo em Power BI
Migração para Cloud (AWS ou GCP)