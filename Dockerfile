FROM python:3.13.0b3
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt -q
COPY . .
CMD ["chainlit", "run", "chainlit_app.py"]
