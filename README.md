# English Tutor

A voice-based English learning app powered by Claude AI. Speak in English (or mix in Chinese), and the AI will help you sound more natural.

## What it does

1. **You speak** — tap the TALK button and say anything in English or Chinese
2. **AI rephrases** — if your English sounds unnatural, it shows and speaks a more natural version
3. **AI translates** — if you used any Chinese, it translates those parts to English
4. **AI replies** — continues the conversation like a friendly language partner
5. **Tracks your progress** — automatically saves your daily stats and corrections over time

## Setup

### 1. Get a Claude API key

- Go to [console.anthropic.com](https://console.anthropic.com)
- Create an account and add credits ($5 is enough for months of use)
- Go to **API Keys** → **Create Key**
- Copy the key (starts with `sk-ant-...`)

### 2. Run the app

```bash
cd ~/Desktop/english-tutor
python3 server.py
```

Then open **https://localhost:8443** in Chrome.

(Chrome is required for speech recognition. Allow microphone access when prompted.)

### 3. Start practicing

- Paste your API key and click **Start**
- Tap **TALK**, speak, then tap **DONE**
- The tutor will correct, translate, and reply — all by voice

## How it works

- **Speech-to-text**: Chrome Web Speech API (free)
- **AI brain**: Claude API via Anthropic (pay-per-use, ~$0.003–0.01 per message)
- **Text-to-speech**: Browser SpeechSynthesis (free)
- **No backend needed** — runs entirely in your browser + direct API calls

## Files

```
english-tutor/
├── index.html    # The entire app (HTML + CSS + JS)
├── server.py     # Simple HTTPS server for local use
├── cert.pem      # Self-signed SSL certificate
├── key.pem       # SSL private key
└── README.md
```

## Cost

- The app itself is free forever (saved locally)
- Claude API credit: $5 ≈ 1,000+ conversations (several months of daily practice)
- Check balance anytime at [console.anthropic.com](https://console.anthropic.com) → Billing
- When it runs out, just add another $5

## Progress Tracking

The app automatically tracks your English learning progress over time:

- **Daily stats** — messages sent, corrections received, and translations used each day
- **Correction history** — saves your original phrases alongside the improved versions so you can review past mistakes
- **Progress dashboard** — click the **Progress** button in the header to see your stats, daily history, and recent corrections
- **AI analysis** — click **Analyze My Progress** to get personalized feedback from Claude on your patterns, weak areas, and improvement tips

All progress data is stored locally in your browser (localStorage). The dashboard itself costs nothing extra — only the "Analyze" feature uses one API call (~$0.01) per click.

## Tips

- Deliberately make mistakes to see corrections in action
- Mix in Chinese when you don't know a word — the AI will translate it
- The AI speaks slightly slower than normal to help you follow along
- Your API key is saved in the browser — you only enter it once
- Check your Progress dashboard regularly to see your correction rate go down over time

## Known issues & future ideas

- Must run `python3 server.py` in Terminal each time before using (server stops when Terminal closes)
- Speech recognition works best in Chrome (Safari has limited support)
- Phone access didn't work via local network — could deploy to a cloud server to fix this
- Could add: vocabulary tracking, difficulty levels, export progress data
