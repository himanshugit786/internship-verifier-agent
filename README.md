# Nagpur Internship Agent - Real-Time Job Verifier

An AI Agent that finds real-time, verified internships for students using live Google data via SerpApi. Built to solve the problem of fake internships.

This project was built for the Hackathon.

## Problem
Students in Tier-2 cities like Nagpur face many fake internship listings. This agent verifies every internship with real-time data.

## Solution
1. User asks: "Data Analyst Internship in Nagpur"
2. Agent calls SerpApi Google Search API
3. Agent fetches live results from Shine, Glassdoor, Jooble
4. Agent returns only verified jobs with direct application links

## Features
- Real-time data, no fake jobs
- Powered by SerpApi
- Fast and lightweight
- Easy to extend to other cities

## Tech Stack
- Python
- SerpApi - Google Search API
- Google-Search-Results Library

## How to Run

1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/nagpur-internship-agent.git
