FROM python:3.11-slim

LABEL authors="harshit"

WORKDIR /application

COPY . .

EXPOSE 8000

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "qr_maker:app" , "--host", "0.0.0.0" , "--port" ,"8000"]
