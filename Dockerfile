# Usar la imatge base de Python
FROM python:3.8

# Establir el directori de treball dins del contenedor
WORKDIR /app

# Copia el archiu de requisits al directori de treball
COPY requirements.txt /app/

# Instala les dependencies del projecte
RUN pip install --no-cache-dir -r requirements.txt

# Copia el codi de l'aplicació al directori de treball
COPY . /app/

# Exposa el port 8000 per a que Django pugui ser accedit
EXPOSE 8000

# Comanda para ejecutar el servidor de desenvolupamen de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]