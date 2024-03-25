#!/bin/bash

cd frontend
npm install
npm run dev &

cd ..

cd backend
pip install -r requirements.txt
python3 app.py
