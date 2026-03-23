from flask import Flask, render_template, request, send_file
import re
import itertools
import matplotlib.pyplot as plt
import random

app = Flask(__name__)

def check_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"[a-z]", password): score += 1
    if re.search(r"[0-9]", password): score += 1
    if re.search(r"[!@#$%^&*]", password): score += 1

    if score <= 2:
        return "Weak Password", "red"
    elif score == 3:
        return "Medium Password", "orange"
    else:
        return "Strong Password", "green"


def generate_wordlist(name, birth, pet):
    words = []

    name = name.lower()
    pet = pet.lower()

    symbols = ["@", "#", "_", ".", "$"]
    numbers = ["123", "1234", "2024", "007", birth]

    base = [name, pet, birth]

    for b in base:
        words.append(b)
        for n in numbers:
            words.append(b + n)
        for s in symbols:
            words.append(b + s)
            words.append(s + b)

    combos = [
        name + birth,
        birth + name,
        name + pet,
        pet + name,
        name + pet + birth,
        pet + name + birth
    ]

    for c in combos:
        for s in symbols:
            for n in numbers:
                words.append(c + s + n)
                words.append(n + s + c)

    for _ in range(50):
        word = random.choice(base)
        word += random.choice(symbols)
        word += random.choice(numbers)
        word = word.capitalize()
        words.append(word)

    return list(set(words))


@app.route("/", methods=["GET", "POST"])
def index():
    global wordlist
    result = None
    color = "white"

    if request.method == "POST":
        password = request.form["password"]
        name = request.form["name"]
        birth = request.form["birth"]
        pet = request.form["pet"]

        result, color = check_strength(password)
        wordlist = generate_wordlist(name, birth, pet)

        with open("wordlist.txt", "w") as f:
            for w in wordlist:
                f.write(w + "\n")

    return render_template("index.html", result=result, color=color)


@app.route("/download")
def download():
    return send_file("wordlist.txt", as_attachment=True)


@app.route("/graph")
def graph():
    plt.figure()
    plt.bar(["Generated Words"], [len(wordlist)])
    plt.title("Wordlist Size")
    plt.savefig("static/graph.png")
    plt.close()

    return send_file("static/graph.png", mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
