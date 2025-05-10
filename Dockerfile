FROM python:latest
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt -q
COPY . .
CMD ["chainlit", "run", "chainlit_app.py"]
