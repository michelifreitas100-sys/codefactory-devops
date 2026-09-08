# Imagem base leve
FROM python:3.12-slim

# Diretório de trabalho dentro do container
WORKDIR /usr/src/app

# Copia apenas o requirements primeiro (aproveita cache de camadas do Docker)
COPY app/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY app/ ./

# Porta exposta pela aplicação Flask
EXPOSE 5000

# Variável de ambiente padrão (pode ser sobrescrita no docker run/compose)
ENV PORT=5000

# Comando executado quando o container sobe
CMD ["python", "main.py"]
