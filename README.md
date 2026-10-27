# 💼 BizSabi AI

> **Your AI-powered partner for smarter business communication.**  
> *Developed as a Capstone Project for the 3MTT Meta Generative AI Programme.*

---

## 📌 1. Project Overview

**BizSabi AI** is an AI-powered business communication and marketing assistant built specifically for Nigerian micro, small, and medium-sized enterprises (MSMEs) and online vendors.

Many small business owners—fashion designers, bakers, caterers, hairdressers, food vendors, tech retailers, and freelancers—juggle daily operations alone. Writing persuasive WhatsApp sales pitches, creating engaging Instagram captions, writing clear product descriptions, and replying to customer inquiries professionally takes valuable hours away from serving clients.

**BizSabi AI** solves this problem by using **Meta Llama 3.3 (70B)** to generate tailored, brand-consistent, culturally authentic, and truthful business communications in seconds.

---

## 🚀 2. Core Features

1. **🏢 Business Profile Customization:**  
   Captures business name, industry, offerings, location, unique selling points (USPs), target audience, and communication tone to deeply personalize all outputs.
2. **📱 WhatsApp Sales Message Generator:**  
   Produces high-converting messages tailored for Nigerian WhatsApp commerce, generating both **Short Status Updates** (for status/stories) and **Detailed Broadcasts** (for DMs and broadcast lists).
3. **🏷️ Product & Service Description Generator:**  
   Transforms raw product specifications into compelling, benefit-focused descriptions. Strictly grounded: **never hallucinates fake prices, fake specs, or false guarantees.**
4. **📸 Social Media Caption Generator:**  
   Tailors captions with scroll-stopping hooks, engaging body copy, clear calls-to-action (CTAs), and curated Nigerian hashtags for **Instagram, Facebook, TikTok, and WhatsApp Status**.
5. **💬 Professional Customer Reply Generator:**  
   Drafts polite, respectful, and reassuring replies to price inquiries, delivery questions, complaints, order acknowledgments, and follow-ups. Strictly avoids making unauthorized financial or delivery promises.
6. **🧪 Built-in 10 Realistic Capstone Test Scenarios:**  
   One-click testing interface demonstrating all 10 realistic Nigerian business scenarios required by the 3MTT rubric.

---

## 🛠️ 3. Technology Stack

* **Programming Language:** Python 3.12+
* **User Interface:** [Streamlit](https://streamlit.io/) (Clean, responsive web UI)
* **Generative AI Model:** **Meta Llama 3.3 (70B-Versatile)** via [Groq Cloud](https://console.groq.com/)
* **Environment Management:** `python-dotenv`
* **Version Control:** Git & GitHub

---

## 📁 4. Project Structure

```text
capstone_meta/
│
├── .env                  # Secret API keys (local only, ignored by Git)
├── .env.example          # Template showing required environment variables
├── .gitignore            # Protects secrets and virtual environment from GitHub
├── requirements.txt      # Python dependencies
├── README.md             # Complete project documentation
├── CAPSTONE_PITCH_SCRIPT.md # Capstone defense presentation script
├── test_app.py           # Automated test suite running 10 capstone scenarios
│
├── app.py                # Main Streamlit web application
│
├── core/                 # Core modular logic
│   ├── __init__.py
│   ├── ai_client.py      # Modular AI wrapper (Groq Meta Llama + Demo Fallback)
│   └── prompts.py        # System prompt and task prompt engineering templates
│
└── data/                 # Sample profiles & test scenarios
    ├── __init__.py
    └── samples.py        # 5 Nigerian business profiles & 10 capstone test cases
```

---

## ⚡ 5. Quick Setup & Installation Guide

Follow these simple steps in your terminal to set up and run BizSabi AI:

### Step 1: Clone or Open the Repository
```bash
cd capstone_meta
```

### Step 2: Create and Activate a Virtual Environment
```bash
# On Linux / macOS:
python3 -m venv venv
source venv/bin/activate

# On Windows (PowerShell):
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Required Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Your Free API Key (Optional but Recommended)
1. Visit [console.groq.com/keys](https://console.groq.com/keys) and create a free account.
2. Click **Create API Key** and copy your key (starts with `gsk_...`).
3. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
4. Open `.env` and paste your key:
   ```env
   GROQ_API_KEY=gsk_your_actual_key_here
   ```
> *Note: If you don't enter an API key, BizSabi AI will automatically run in **Demonstration Mode**, providing realistic previews without crashing!*

### Step 5: Launch the Streamlit Web Application
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

---

## 🧪 6. Automated Testing (10 Scenarios)

To run the automated verification test across all 10 realistic business scenarios:
```bash
python test_app.py
```

All 10 scenarios test:
1. Baker promoting a birthday cake on WhatsApp Status.
2. Fashion designer advertising new clothing.
3. Food vendor writing a WhatsApp sales message.
4. Hairdresser creating an Instagram caption.
5. Online retailer describing a tech product.
6. Customer asking about product prices.
7. Customer asking about delivery arrangements.
8. Business owner responding politely to a complaint.
9. Business owner acknowledging an order and payment.
10. Business owner following up with an interested customer.

---

## 🧠 7. Prompt Engineering Highlights

For your capstone evaluation, the prompt engineering framework in `core/prompts.py` enforces:
1. **Cultural Grounding:** Tone and vocabulary tailored to Nigerian business etiquette (warmth, politeness, respect).
2. **Zero-Hallucination Guardrails:** Explicit instructions that prohibit the AI from inventing prices, stock counts, delivery fees, or refund promises.
3. **Structured Dual Outputs:** Providing short status versions alongside detailed broadcasts for WhatsApp.

---

## 👤 Author & Acknowledgments

* **Developer:** 3MTT Fellow (Generative AI Track)
* **Sponsor:** Federal Ministry of Communications, Innovation and Digital Economy (3MTT Nigeria) & Meta

