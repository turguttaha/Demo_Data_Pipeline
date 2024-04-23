FROM python:3.9.19
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt && \
        rm requirements.txt
ENTRYPOINT ["python", "app.py"]
