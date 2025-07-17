FROM pytorch/pytorch:2.7.1-cuda12.6-cudnn9-devel

WORKDIR /workspace

COPY . .

RUN pip install --no-cache-dir -r requirements.txt