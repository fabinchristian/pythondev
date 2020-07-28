FROM python
COPY . /app
WORKDIR /app
RUN pip install matplotlib
CMD python ./shortest_path.py