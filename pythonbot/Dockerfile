FROM python:3.10.11

# Establecer el directorio de trabajo
WORKDIR /pythonbot

# Copia los archivos necesarios al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto utilizado por el bot de Telegram
EXPOSE 8443

# Define el comando de inicio
CMD ["python", "Bot.py"]