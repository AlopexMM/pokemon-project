FROM python:3.12

WORKDIR /app

COPY ./apps/backend .

RUN pip install uv && uv sync --all-packages

EXPOSE 8000

CMD ["uv", "run", "python", "src/backend/main.py"]