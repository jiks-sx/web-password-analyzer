# Web Password Analyzer

A modern web-based Password Analyzer built using Python and Flask. This application evaluates password strength, generates advanced wordlists, and visualizes data through graphs. It is designed with a clean user interface and an animated cybersecurity-themed background.

---

## Overview

This project demonstrates how password security can be analyzed and improved using simple rules and data visualization. It also simulates real-world attack scenarios by generating strong wordlists based on user inputs.

---

## Key Features

* Password strength evaluation (Weak, Medium, Strong)
* Advanced wordlist generation using combinations, symbols, and mutations
* Downloadable wordlist file
* Graph visualization using Matplotlib
* Modern and responsive user interface using Bootstrap
* Animated background (Matrix-style)

---

## Tech Stack

* Python
* Flask
* Matplotlib
* HTML5
* CSS3
* Bootstrap
* JavaScript (Canvas Animation)

---

## Project Structure

```id="p3d8xv"
web-password-analyzer/
│
├── app.py
├── templates/
│   └── index.html
└── static/
```

---

## Installation and Setup

Clone the repository:

```id="a2k9vd"
git clone https://github.com/jiks-sx/web-password-analyzer.git
```

Navigate to the project directory:

```id="t9w2mr"
cd web-password-analyzer
```

Install required dependencies:

```id="k8q7sx"
pip install flask matplotlib
```

---

## Running the Application

Start the Flask server:

```id="m4l1zo"
python3 app.py
```

Open your browser and visit:

```id="b5y6ru"
http://127.0.0.1:5000
```

---

## How It Works

1. The user enters a password and optional personal inputs
2. The system evaluates password strength based on multiple criteria
3. A strong wordlist is generated using permutations and mutations
4. The wordlist is saved and available for download
5. A graph is generated to visualize the size of the wordlist
6. Results are displayed with a modern UI and animated background

---

## Use Cases

* Learning password security concepts
* Demonstrating brute-force wordlist generation
* Cybersecurity project for academic submission
* Beginner-friendly web security tool

---

## Future Enhancements

* Password entropy calculation
* Machine learning-based strength prediction
* Cloud deployment (Render / Railway)
* Advanced analytics dashboard

---

## Author

GitHub: https://github.com/jiks-sx
