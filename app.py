import webbrowser

def fiscalizacao_pp():
    print("=== SIMULADOR DE FISCALIZAÇÃO DE PRODUTOS PERIGOSOS (PRÉVIA) ===")
    
    # --- ETAPA 0: CONDUTOR ---
    nome_condutor = input("\nNome do Condutor: ")
    mopp = input("Possui CETPP (MOPP) ativo no App Senatran? (s/n): ").lower()
    
    if mopp == 'n':
        print("\n[!] ALERTA DE INFRAÇÃO (CONDUTOR):")
        print("- CTB: Art. 162, VII (Falta de curso especializado)")
        print("- ANTT: Art. 43, §2º, XIX/XX (Transportador) e §6º, XIII/XXIV (Expedidor)")
        print("- OBS: Avaliar Crime Ambiental (Art. 56 Lei 9.605/98) se houver grande risco.")
    
    # --- ETAPA 0.1: TACÓGRAFO ---
    pbt = float(input("\nInforme o PBT do veículo (em kg): "))
    if pbt > 4536:
        print(">> Veículo OBRIGADO a uso de Cronotacógrafo.")
        ver_inmetro = input("Deseja abrir o site do Inmetro para verificar a placa? (s/n): ").lower()
        if ver_inmetro == 's':
            webbrowser.open("https://cronotacografo.rbmlq.gov.br/certificados/consultar")
    else:
        print(">> Veículo DISPENSADO de Cronotacógrafo.")

    # --- ETAPA 1: FILTRO DE MODALIDADE ---
    print("\nMODALIDADE DE TRANSPORTE:")
    print("1 - A Granel (Tanque, Caçamba, etc)")
    print("2 - Fracionado (Caixas, Tambores, etc)")
    modalidade = input("Escolha: ")

    # --- ETAPA 1.1: INTELIGÊNCIA DE ISENÇÃO (QUANTIDADE LIMITADA) ---
    # Simulação de base de dados simplificada (ONU: Limite em kg)
    db_isencao = {"1203": 333, "1202": 1000, "1005": 20} # Exemplos: Gasolina, Diesel, Amônia
    
    onu = input("\nDigite o Número ONU da carga: ")
    qtd = float(input("Digite a Quantidade Total (kg/L): "))

    isento = False
    if onu in db_isencao:
        limite = db_isencao[onu]
        if qtd <= limite:
            isento = True
            print(f"\n✅ CARGA IDENTIFICADA COMO QUANTIDADE LIMITADA (Limite: {limite}kg).")
            print(">> Dispensa: MOPP, CIV, CIPP e Sinalização Externa.")
        else:
            print(f"\n⚠️ CARGA PLENA DETECTADA (Limite de {limite}kg excedido).")
    else:
        print("\n⚠️ ONU não encontrado na base de isenção simples. Tratando como CARGA PLENA.")

    # --- ETAPA 2: DOCUMENTAÇÃO TÉCNICA (SOMENTE SE CARGA PLENA) ---
    if not isento:
        print("\n--- CHECKLIST DE DOCUMENTAÇÃO (CARGA PLENA) ---")
        
        # NF
        declara_exp = input("Possui 'Declaração do Expedidor' na NF? (s/n): ").lower()
        if declara_exp == 'n':
            print("[!] INFRAÇÃO: Art. 43, III, 'a' da Res. 5.998/22 (Falta de Declaração).")

        # CIV/CIPP (Somente Granel)
        if modalidade == '1':
            print("\nVERIFICAÇÃO DE CERTIFICADOS (A GRANEL):")
            civ = input("CIV está válido e presente? (s/n): ").lower()
            if civ == 'n':
                print("[!] INFRAÇÃO: Art. 43, II, 'f' da Res. 5.998/22 (CIV Inválido/Ausente).")
            
            cipp = input("CIPP é compatível com o produto e está válido? (s/n): ").lower()
            if cipp == 'n':
                print("[!] INFRAÇÃO: Art. 43, II, 'f' ou 'd' (CIPP Incompatível/Vencido).")

    print("\n=== FIM DA SIMULAÇÃO ATÉ O MOMENTO ===")

# Executar teste
if __name__ == "__main__":
    fiscalizacao_pp()
