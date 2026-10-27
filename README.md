# Multilingual AI Triage Agent 

A Python-based agent designed to categorize, evaluate urgency, and route incoming user messages across English, French, Spanish, and Portuguese.

## Purpose
This project provides a simple engine for automated customer query triage. It parses input text, detects language, extracts sentiment and priority flags, and routes the payload to the appropriate service handler.

## Core Features
- Multi-language text parsing (EN / FR / ES / PT)
- Intent classification and urgency scoring
- Structured JSON output for API integrations
- Test suite built with pytest

## Tech Stack
- Python 3.11+
- pytest

## Getting Started

1. Clone the repository:
   git clone https://github.com/AntonielAlmeidabr/AI-Multilingual-Agent.git

2. Navigate into the directory:
   cd AI-Multilingual-Agent

3. Run tests:
   pytest