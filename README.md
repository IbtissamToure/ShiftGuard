# ShiftGuard 🛡️

> AI-powered shift safety validator that protects workers from dangerous scheduling patterns.

## The Problem

In 2024, a Saudi physician lost her life in a car accident 
after finishing an exhausting shift. Fatigue-related incidents 
among shift workers are not rare — they are a systemic failure 
in how organizations schedule their people.

Overworked employees don't just underperform. They are at risk.

## What is ShiftGuard?

ShiftGuard analyzes employee shift schedules and:

- 🔍 Detects dangerous rest patterns based on global safety standards
- 📊 Calculates a risk score (0-100) for each employee
- 💡 Suggests the safest available replacement

## Who is it for?

- HR Managers
- Operations & Scheduling Teams
- Any organization managing shift-based work

## Safety Standards

- Minimum 11 hours rest between shifts (ILO standard)
- Risk score: 0 = safe, 100 = critical danger

## How to Run

### 1. Clone the repo
```bash
git clone https://github.com/IbtissamToure/ShiftGuard.git
cd shiftguard
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run ShiftGuard
```bash
python src/main.py --employee "Sara Ahmed"
```

### Output
```
==========================================
     ShiftGuard 🛡️  Safety Report
==========================================
Employee   : Sara Ahmed
Rest Hours : 2.0 hours
Risk Score : 91.7 / 100 🔴 DANGEROUS
------------------------------------------
💡 Suggestion: Ahmed Ali — 13.0 hours rest
==========================================
```

## Tech Stack

- Python
- Pandas

## Project Status

✅ Complete — open for contributions