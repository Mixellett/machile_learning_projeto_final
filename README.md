## 🏗 Estrutura do Projeto

```
raiz/
├── app/
│   ├── api.py/             # Script que implementa a API de previsão
│   ├── main.py/            # Script que executa a API de previsão e retorna o se a avaliação é "Positivo" ou "Negativo"
├── data/
│   ├── raw/                # Diretório contendo os dados baixados manualmente do Kaggle
│   │   ├── test.csv
│   │   ├── train.csv
│   ├── processed/          # Diretório contendo os dados processados 
│   │   ├── amazon_reviews_train_sample.parquet
│   │   ├── amazon_reviews_test_sample.parquet
│   ├── reports/            # Diretório contendo gráficos da distruição de notas e tamanho dos textos
│   │   ├── distribuicao_notas.png
│   │   ├── distribuicao_tamanho_avaliacoes.png
├── model/                  # Diretório contendo o modelo salvo
│   ├── config.json
│   ├── model.safetensors
│   ├── special_tokens_map.json
│   ├── tokenizer_config.json
│   ├── tokenizer.json
│   ├── training_args.bin
│   ├── vocab.txt
├── Dockerfile              # Arquivo para contêinerizar a API com o modelo
├── requirements              
├── data_processing.ipynb   # Notebook para analisar, limpar e dividir os dados              
├── training.ipynb          # Notebook para treinar e salvar o modelo              
├── README.md              

```

## 🔧 Configuração e Instalação

### Baixando dataset do Kaggle

- Baixar manualmente o arquivo amazon_review_polarity_csv.tgz disponível no [Kaggle](https://www.kaggle.com/datasets/kritanjalijain/amazon-reviews/data)  


### Executando os notebooks

#### Crie e ative um ambiente virtual
```base
python -m venv .venv
source .venv/bin/activate  # Linux/MacOS
ou
.venv\Scripts\activate  # Windows
```
  
#### Execute o Jupyter Notebook

```base
jupyter notebook
```
- Carregar e executar o arquivo *data_processing.ipynb*  
  

#### Abra o Colab

- Carregar o arquivo *training.ipynb*  
- Adicionar  os arquivos *amazon_reviews_test_sample.parquet* e *amazon_reviews_train_sample.parquet*  
- Executar o notebook  
- Salvar mlruns.zip  
- Criar uma pasta model na raiz do projeto com o modelo descompactado do mlruns.zip  


### Usando Docker

```bash
# Construa a imagem
docker build -t amazon-reviews-api .

# Execute o container
docker run -p 8000:8000 amazon-reviews-api
```

## 🚀 Executando o Serviço

```bash
# Execute o servidor
python main.py
```

