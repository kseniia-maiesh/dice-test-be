# Dice Game - RTP Analysis

A FastAPI-based dice game backend with Return to Player (RTP) analysis.

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the backend:
```bash
uvicorn main:app --reload
```

3. Test the game:
- API will be available at `http://localhost:8000`
- API docs at `http://localhost:8000/docs`

## RTP Analysis

Run the RTP calculation script:
```bash
python test_rtp_simple.py
```

## Game Rules

Roll 5 dice and win based on combinations:
- **Pair**: Two dice with the same value
- **Straight**: Sequential numbers (1-2-3-4-5 or 2-3-4-5-6)
- **Full House**: Three of one value + two of another
- **Balut**: All five dice showing the same value

## API Endpoints

- `POST /init` - Initialize player balance (100 credits)
- `POST /roll` - Roll dice with a bet
  - Request: `{"bet": 10}`
  - Response: Dice values, combination, winnings, and balance
