#!/bin/bash

source venv/bin/activate
export PYTORCH_ALLOC_CONF=expandable_segments:True
# python main.py --normalvram --enable-manager --listen 0.0.0.0
# python main.py --disable-smart-memory --highvram --enable-manager --listen 0.0.0.0
# python main.py --lowvram --cpu-vae --enable-manager --listen 0.0.0.0
python main.py --lowvram --disable-async-offload --enable-manager --listen 0.0.0.0
