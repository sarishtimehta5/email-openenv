# Email Classification OpenEnv

## Overview
This is an AI environment for classifying emails into:
- Spam
- Important
- Promotion

## Tasks
- Easy
- Medium
- Hard

## API Endpoints

### Reset
GET /reset?task=easy

### Step
POST /step
Body:
{
  "action": 0
}

### State
GET /state

## Actions
0 = Spam  
1 = Important  
2 = Promotion  

## Run Locally
uvicorn app:app --reload

## Run Inference
python inference.py