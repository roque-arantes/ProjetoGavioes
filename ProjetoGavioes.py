import googlemaps
import os
import time

API_KEY = "KEYAPI" ### Chave da Places API

gmapsapi = googlemaps.Client(key=API_KEY) ### Chamada da API

def buscar_unidades(nome_local: str, traducao: str) -> list:
    unidades_lista = []       ### Lista para armazenar as unidades encontradas
    resultado_places = gmapsapi.places(query=nome_local, language=traducao)       ### Faz a primeira busca usando Places API (Text Search)

    while True:
        for unidades_places in resultado_places.get("results", []): ### Percorre todos os locais encontrados nessa página
            guardar_id = unidades_places["place_id"] ### Obtém o 'place_id' — identificador único do local na API

            detalhes_unidade = gmapsapi.place(
                place_id=guardar_id,
                language=traducao,
                fields=["name", "formatted_address", "opening_hours"]
            ) ### Busca detalhes do local (nome, endereço e os horários de funcionamento)

            info_unidade = detalhes_unidade.get("result", {}) ### Pega os dados retornados pela API
            unidades_lista.append({
                "nome": info_unidade.get("name"),
                "endereco": info_unidade.get("formatted_address"),
                "horarios": info_unidade.get("opening_hours", {}).get("weekday_text")
            }) ### Adiciona as informações na lista de unidades

        if "next_page_token" in resultado_places:           ### Caso exita mais que uma página de resultados, passar para a próxima
            time.sleep(2)                                   ### Necessário para evitar erro de requisição
            resultado_places = gmapsapi.places(
                query=nome_local,
                language=traducao,
                page_token=resultado_places["next_page_token"]
            )                                               ### Busca a próxima página usando o 'next_page_token'

        else:   ### Se não houver mais páginas, sai do loop
            break

    return unidades_lista

###############################################
###          Execução do programa           ###
###############################################

os.system("cls")

print("Procurando unidades...")
unidades_encotradas = buscar_unidades("Academia Gavioes brasil", "pt-BR") ### Executa a DEF buscar_unidades

print(f"Total de unidades encontradas: {len(unidades_encotradas)}\n") ### Exibe o total de unidades encontradas

for i, unidades_encotradas in enumerate(unidades_encotradas, start=1): ### Enumerate para mostrar os dados formatados no console
    print(f"{i}. {unidades_encotradas['nome']}")
    print(f"   Endereço: {unidades_encotradas['endereco']}")
    if unidades_encotradas["horarios"]: ### Mostra o horario se existir
        print("   Horários:")
        for horario in unidades_encotradas["horarios"]: ### Percorre a lista de horários
              print(f"     - {horario}")
    else: ### Se não existir, mostra que não está disponível
          print("   Horários: Não disponível")
    print("-" * 50) ### Linha separadora para melhor visualização