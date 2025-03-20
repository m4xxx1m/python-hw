FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    texlive-latex-base \
    texlive-lang-cyrillic \
    texlive-fonts-recommended \
    texlive-extra-utils \
    texlive-latex-extra \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install uv

WORKDIR /app

COPY src /app

RUN uv sync

CMD ["sh", "-c", "uv run python task2.py && pdflatex -output-directory output -interaction=nonstopmode output/document.tex"]
