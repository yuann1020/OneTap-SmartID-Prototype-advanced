
# OneTap — Smart ID Verification Prototype

A mobile-first identity verification experience built for Smart ID / MyKad NFC authentication.
Developed for the GODAMLAH! 2.0 Smart ID Hackathon 2025.

This repository contains:

- A **CLI simulator** that walks through the OneTap verification journey.
- A **FastAPI mock backend** showing how NFC, biometric checks, and queue generation
  could be exposed as APIs.
- Design assets and placeholders for your Figma UI and pitch deck.

---

## 🚀 Overview

OneTap provides a fast, secure, and user-friendly way to verify Malaysian Smart ID (MyKad)
using NFC + biometric authentication, then route users into hospital and government counter flows.

This prototype is not production code; it is meant to demonstrate architecture and user flow.

---

## 🎯 Features in This Repo

### 1. CLI Simulator (`app-demo/onetap_cli.py`)

- Service selection: Hospital Check-In or Government Counter.
- Simulated NFC read + identity decryption.
- Mock biometric verification step.
- Queue number generation (e.g., A021, B042).
- Optional "QR token" generation (string you can later map to a QR code).

Run it with:

```bash
python app-demo/onetap_cli.py
```

### 2. FastAPI Mock Backend (`app-demo/api/main.py`)

- `POST /nfc/read` – simulate reading an NFC Smart ID token.
- `POST /verify/biometric` – simulate biometric verification.
- `POST /queue/hospital` – issue a hospital queue number.
- `POST /queue/government` – issue a government counter queue number.

Install dependencies:

```bash
pip install fastapi uvicorn
```

Run the API:

```bash
uvicorn app-demo.api.main:app --reload
```

Then open http://127.0.0.1:8000/docs to explore the endpoints.

---

## 🛠 Suggested Tech Stack

| Part                | Tech          |
|---------------------|--------------|
| UI Design           | Figma        |
| Prototype Logic     | Python       |
| Mock Backend        | FastAPI      |
| Documentation       | Markdown/PDF |

---

## 📂 Repository Structure

- `prototype/` – screenshots, Figma links, flow diagrams.
- `app-demo/onetap_cli.py` – interactive CLI prototype.
- `app-demo/api/main.py` – FastAPI mock backend.
- `assets/` – logos, icons, exported UI.
- `docs/` – pitch deck, proposal, technical overview.

---

## 👥 Team

- Lead Developer – OneTap Prototype
- UI/UX Designer – Figma flows & branding
- Backend/AI Developer – Mock services & architecture
