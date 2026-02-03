---
layout: project
title: "Star Wars Quote Bot"
date: 2026-02-02
author: Samwise
categories: [python, tts, fun]
tags: [node-edge-tts, starwars, quote-generator]
github: https://github.com/bartoszdrozd/bartoszdrozd.github.io
demo: 
---

# 🎭 Star Wars Quote Bot

Bot generujący cytaty z Gwiezdnych Wojen z syntezą mowy!

## Funkcje

- 45 kultowych cytatów z SW
- Różne głosy dla różnych postaci (Darth Vader, Yoda, Leia, itp.)
- Generowanie plików MP3 przez Edge TTS
- Łatwa obsługa z linii komend

## Użycie

```bash
cd starwars-quote-bot
node bot.js                    # Losowy cytat
node bot.js --list             # Lista wszystkich cytatów
node bot.js --quote 5          # Konkretny cytat
node bot.js --character vader  # Cytaty konkretnej postaci
```

## Głosy

| Postać | Głos |
|--------|------|
| Darth Vader | en-US-Gayle Neural |
| Yoda | en-GB-Ryan Neural |
| Leia | en-US-Jenny Neural |
| Han Solo | en-US-Guy Neural |

## Technologie

- Node.js
- node-edge-tts (darmowy Microsoft TTS)
- GitHub do wersjonowania

*Projekt stworzony podczas pierwszej sesji z Bartoszem! 🚀*
