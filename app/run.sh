#!/bin/bash

cd frontend
npm install
npm run dev &

cd ..

pip install -r requirements.txt
python3 main.py
