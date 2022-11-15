import time
print("Seja bem vindo!")
print("A nossa Calculadora de Carbono.")
time.sleep(2)
print("Por favor informe os seguintes dados para a realização do cálculo de CO2.")
diesel={'caminhão':[2.5],
        'caminhão pipa':[2.1],
        'caminhão prancha':[3.6],
        'caminhão carroceria':[3.9],
        'van':[10.5],
        'ônibus':[3.1]}
time.sleep(1)
distancia=float(input("Informe a distância (Km) percorrida pelo transporte (para realizar o percurso de ida e volta) para realizar as entregas. "))
print(distancia,"km, é o total percorrido? Sendo",distancia/2,"km a ida e",distancia/2,"km a volta. ")
res_d=input("Responda com 'Sim' ou 'Não'. ")
res_d.lower()
if res_d=="nao" or res_d=="não" or res_d=="n":
    distancia=float(input("Digite a distância (Km) percorrida pelo transporte (para realizar o percurso de ida e volta) para realizar as entregas. "))
    print(distancia/2,"km a ida e",distancia/2,"km a volta. ")
qntd_trans_materias=int(input("Digite quantos caminhões realizaram o transporte dos materias. "))
tipo_materias=float(input("Digite a capacidade dos caminhões (em toneladas). "))
qntd_materiais=float(input("Digite quantas viagens os caminhões executaram. "))
qntd_trans_agua=int(input("Digite quantos caminhões pipa realizaram o transporte de água. "))
tipo_agua=float(input("Digite a capacidade dos caminhões pipas em metros cúbicos (m³)). "))
qntd_agua=float(input("Digite quantas viagens os caminhões pipa executaram. "))
tipo_pessoa=input("Informe se o transporte dos trabalhadores foi concluído atravéz de 'van' ou 'ônibus'. ")
qntd_trans_pessoa=int(input("Digite quantos veículos (selecionados acima) realizaram o transporte dos trabalhadores. "))
dias=int(input("Informe quantos dias durou a obra. "))
dias_materiais=int(input("Digite em quantos dias durante a obra ocorreram 'entregas' de materiais. "))
dias_agua=int(input("Digite em quantos dias durante a obra ocorreram 'entregas' de água. "))
print("As máquinas utilizadas na obra estão na lista abaixo.")
time.sleep(0.5)
maquinas={'Escavadeira':[29],
          'Rolo Compactador':[20],
          'Motoniveladora':[21],
          'Pá Carregadeira':[12],
          'Retro Escavadeira':[13],
          'Pavimentadora de Asfalto':[14],
          'Plaina de Estradas':[16],
          'Estabilizador de Solo':[20],
          }
print(maquinas.keys())
print("As máquinas utilizadas na obra estão entre as citadas acima.")
res_m=input("Responda com 'Sim' ou 'Não'. ")
res_m.lower()
if res_m=="nao" or res_m=="não" or res_m=="n":
    ad="+"
    while ad=="+":
        ad_maquinas=input("Informe o nome da máquina usada e quanto ela consome de combustivel por quilômetro. ")
        maquinas[ad_maquinas]
        ad=input("Digite '+' para adicionar outra máquina, ou digite '>' para continuar. ")
qntd_trans_maquinas=int(input("Digite quantos caminhões realizaram o transporte das máquinas. "))
op="+"
calculo_maquina=0
while op=="+":
    tipo_maquinas=input("Informe as máquinas que foram usadas na obra (uma por vez). ")
    qntd_maquinas=int(input("Digite quantas máquinas foram usadas. "))
    dis_maquinas=float(input("Qual a distância (km) percorrida pela máquina na obra. "))
    calculo_maquina+= (maquinas[tipo_maquinas][0])*dis_maquinas*qntd_maquinas
    op=input("Digite '+' para adicionar outra máquina, ou digite '>' para continuar. ")
trans_residuos=int(input("Quantos caminhões vão realizar o transportar dos resíduos (resultantes da obra). "))
dis_residuos=int(input("Qual a distância (km) que esses caminhões vão percorrer até o deposito de resíduos. "))
print("Esses caminhões que realizaram o transporte de resíduos executaram mais de uma viagem. ")
res_r=input("Responda com Sim ou Não. ")
res_r.lower()
if res_r=="sim" or res_r=="s":
    qntd_trans_residuos=int(input("Quantas viagens eles realizaram. "))
    total_residuos=((diesel["caminhão carroceria"][0])*2)*trans_residuos*dis_residuos*qntd_trans_residuos
else:
    total_residuos=(diesel["caminhão carroceria"][0])*trans_residuos*dis_residuos
total_maquinas=calculo_maquina+((distancia*diesel["caminhão prancha"][0])*qntd_maquinas*dias)
total_materiais=(distancia*diesel["caminhão"][0])*qntd_trans_materias*qntd_materiais*dias_materiais
total_agua=(distancia*diesel["caminhão pipa"][0])*qntd_trans_agua*qntd_agua*dias_agua
total_pessoas=(distancia*diesel[tipo_pessoa][0])*qntd_trans_pessoa*dias
total_final=total_agua+total_maquinas+total_materiais+total_pessoas+total_residuos
arvore=((total_final)/1000)*7
credito=((total_final)/1000)*365
print("Obrigado pelas informações.")
print("Estamos calculando seu gasto de carbono, isso pode levar alguns segundos.")
print("Agradecemos pela sua paciência.")
time.sleep(5)
print("Após analise dos dados.")
print("Chegamos ao seu gasto de carbono. Que foi equivalente a","%.2f"%total_final,"kg.") 
print("O que tem valor equivalente a",("%.2f"%(total_final/1000)),"toneladas de carbono.")
time.sleep(1.5)
print("Como forma para a compensação desse carbono, você pode escolher entre a compra de crédito ou o plantio de árvores.")
print("O seu gasto de",("%.2f"%(total_final/1000)),"toneladas.")
print("Tem como formas de compensação o plantio de","%.0f"%arvore,"árvores, ou a compra de crédito no valor de R$","%.2f"%credito,".")