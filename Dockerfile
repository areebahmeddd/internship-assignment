FROM python:3.11-slim AS builder

WORKDIR /fyle-intern

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --target /dependencies

# Stage 2: Runner Stage
FROM python:3.11-slim AS runner

WORKDIR /fyle-intern

COPY --from=builder /dependencies /usr/local/lib/python3.11/site-packages
COPY . .

EXPOSE 7755
