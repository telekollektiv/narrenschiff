FROM python:3
RUN useradd -m python
RUN mkdir /app
RUN chown python. /app
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY server.py ./
COPY templates/ templates/
COPY static/ static/
USER python
RUN mkdir persistent
EXPOSE 5000 5500
ENTRYPOINT ["/app/server.py"]
