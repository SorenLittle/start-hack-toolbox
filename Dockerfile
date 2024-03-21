FROM python:3.10-slim as base

ENV VIRTUAL_ENV=/.venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

FROM base AS builder

# Requirements
RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt --no-warn-script-location

FROM base AS final

WORKDIR /src/app

COPY --from=builder /.venv /.venv
COPY . .

EXPOSE 8000:8000

CMD ["uvicorn", "src.app.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--reload-include", "*.html", "--reload-include", "*.css"]
