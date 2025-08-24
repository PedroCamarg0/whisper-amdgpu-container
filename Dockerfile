FROM rocm/pytorch:latest

RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg git && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir datasets ipywidgets transformers numba openai-whisper

WORKDIR /app
COPY ./build/ /app/build/
RUN python3 /app/build/download.py