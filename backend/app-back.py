import csv

def carregar_acessos():
  y = []
  p = []
  m = 0

  #le o csv
  arquivo = open('despesa_orcamentaria_da_uniao.csv', 'r')
  leitor = csv.reader(arquivo)

  #pula a primeira linha do csv para ela nao entrar nos arrays
  next(leitor) 

  #percorre todas as colunas do cvs
  for ano_de_referencia,total,despesas_correntes,pessoal_e_encargos_sociais,juros_e_encargos_da_divida,outras_despesas_correntes,transferencias_a_estados,df_e_municipios,beneficios_previdenciarios,demais_despesas_correntes,despesas_de_capital,investimentos,inversoes_financeiras,amortizacao_da_divida,refinanciamento,refinanciamento_da_divida_mobiliaria,refinanciamento_da_divida_contratual,outras_despesas_de_capital in leitor:
    y.append(int(ano_de_referencia))
    p.append(int(pessoal_e_encargos_sociais))
    #descobre o maior valor gasto nos ultimos 10 anos (que se tem no csv)
    if(int(ano_de_referencia) >= 2008) and (int(total) > m):
      m = int(total)

  #retorna apenas os ultimos 10 dados do csv
  return y[-10:], p[-10:], m 