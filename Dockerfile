# Asosiy payton rasmini tanlash
FROM python:3.11

# Loyihaning ishlaydigan papkani tanlash
WORKDIR /app

RUN python -m venv /opt/venv


ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

FROM --platform=linux/amd64 python:3.11

WORKDIR /app

# Loyiha fayllarini "workdir" ga kiritish
COPY . /app

# Loyiha uchun talab etilgan qo'shimcha kerakli dasturlarni o'rnatish
RUN pip install --no-cache-dir -r requirements.txt

# Portni o'ngini ochish (kerak bo'lgan holatda)
EXPOSE 8000

# Dasturni ishga tushirish
CMD ["python", "bot.py"]