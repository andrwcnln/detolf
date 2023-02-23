FROM gorialis/discord.py:minimal

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN pip install -r local-requirements

COPY . .

CMD ["python", "helmi.py"]