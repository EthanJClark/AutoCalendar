# AutoCalendar

An AI-assisted academic planner that helps schedule tasks, classes, and study blocks intelligently. Uses AI agents to interpret natural language tasks (e.g. “study for biology exam next week”), resolve time constraints, and propose balanced schedules. This project was developed to help me save time since college has been so busy and hard to stay on track!

## Purpose
Reduce planning friction for school by:
- Converting free-form task descriptions into structured schedule entries
- Prioritizing by urgency, estimated effort, and deadlines
- Avoiding overload by respecting existing calendar constraints

## Features
- Natural language task ingestion (e.g. “Finish lab report by Friday 5pm”)
- AI agent pipeline for parsing, estimating effort, and scheduling
- Syncs with google calendar
- Jupyter Notebook experimentation for heuristics and model evaluation

(Implementations can be modular so individual agents are replaceable or upgraded.)

## Tech Stack
- Jupyter Notebook (prototyping, experimentation)
- Python (core scheduling + agent orchestration)

## Future Ideas
- Adaptive effort estimates based on historical completion variance
- Reinforcement loop: adjust future scheduling based on overruns
- Embedding similarity for auto-tagging tasks
- Discription Agent that provides a detailed description for each event block in google calendar

## Status
Exploratory; core scheduling and agent scaffolding under development.
