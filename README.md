# <div align="center">Projeto Gaviões</div>

## <div align="center">📌 Objetivo</div>
O **Projeto Gaviões** tem como objetivo localizar as unidades da **Academia Gaviões** utilizando a **Google Places API**.  
A API permite realizar buscas com base em **strings** e foi implementada em **Python** pela sua facilidade de uso e popularidade.

---

## <div align="center">🛠️ Tecnologias Utilizadas</div>
- **Linguagem:** Python 3.x  
- **Biblioteca:** [googlemaps](https://googlemaps.github.io/google-maps-services-python/docs/)  
- **API:** [Google Places API](https://developers.google.com/maps/documentation/places/web-service?hl=pt-br)  

---

## <div align="center">📦 Instalação</div>
Antes de rodar o projeto, instale a biblioteca necessária:

```bash
pip install googlemaps
```

---

## <div align="center">⚙️ Decisão Técnica</div>
Foi escolhida a biblioteca **googlemaps** em vez de `requests` devido à:  
✅ Maior legibilidade do código  
✅ Facilidade de manutenção  
✅ Suporte completo aos serviços e parâmetros da API  

> **Nota:** Apesar das vantagens, a biblioteca adiciona uma dependência extra e só funciona diretamente com as APIs do Google, limitando integrações com outras APIs.

---

## <div align="center">🔍 Funcionalidades</div>

### **Comando `.places()`**
- **Função:** Pesquisa por estabelecimentos usando **texto** (ex.: `query="Academia Gavioes Brasil"`)  
- **Vantagens:**  
  - Pesquisa simples por string  
  - Retorna `place_id` (identificador único do estabelecimento)  
  - Permite definir idioma (`language="pt-BR"`)  

- **Desvantagens:**  
  - Retorna apenas **20 resultados por página** (máx. 3 páginas) → requer paginação  
  - Pode trazer resultados irrelevantes  
  - Não retorna detalhes completos (ex.: horários)  

---

### **Comando `.place()`**
- **Função:** Retorna **detalhes específicos** de um estabelecimento a partir do `place_id`  
- **Vantagens:**  
  - Retorna informações detalhadas (horários, endereço completo, etc.)  
  - Possibilidade de filtrar dados com `fields=[]` para reduzir processamento  

- **Desvantagens:**  
  - Necessário para obter horários, gerando mais requisições → **aumenta custo**  
  - Requisições individuais deixam o programa mais lento (necessário `time.sleep(2)`)  
  - Dados dependem da qualidade das informações cadastradas no Google Maps  

---

## <div align="center">📚 Documentação de Referência</div>
- [Documentação da biblioteca googlemaps para Python](https://googlemaps.github.io/google-maps-services-python/docs/)  
- [Documentação oficial Google Places API](https://developers.google.com/maps/documentation/places/web-service?hl=pt-br)  

---

## <div align="center">👨‍💻 Desenvolvedor</div>
<div align="center">
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/roque-arantes" title="Matheus Roque Arantes">
        <img src="https://avatars.githubusercontent.com/u/202198493?v=4" width="100px;" alt="Foto do Integrante Matheus Roque"/><br>
        <sub><b>Matheus Roque Arantes</b></sub>
      </a>
    </td>
  </tr>
</table>
</div>
