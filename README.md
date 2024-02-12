# Projeto de Transcrição de Imagem

Este projeto oferece uma ferramenta de linha de comando para transcrever textos a partir de imagens utilizando a API do OpenAI.

# Instalar Dependências
```bash
pip install requests python-dotenv openai
```

# Configurar Variáveis de Ambiente
Você precisará de uma chave de API do OpenAI para usar este script. Adicione sua chave de API a um arquivo .env no diretório raiz do projeto
```bash 
OPENAI_API_KEY=sua_chave_de_api_aqui
```

# Uso
```bash 
python script.py <caminho_da_imagem>
```