# -*- coding: utf-8 -*-

from flask import Flask, render_template_string, redirect, url_for
from datetime import date
import os

app = Flask(__name__)

# ---------------- STYLE ----------------

STYLE = """
<style>
body {
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
    background: linear-gradient(to bottom, #ffe6f0, #ffffff);
    text-align: center;
}

.fade {
    animation: fadeIn 1.2s ease-in;
    padding: 20px;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

h1 { color: #c2185b; }
h2 { color: #880e4f; }

p {
    font-size: 16px;
    line-height: 1.7;
}

.poem {
    white-space: pre-line;
    font-size: 16px;
    line-height: 1.8;
    margin-top: 25px;
}

.images {
    margin-top: 20px;
}

.images img {
    width: 90%;
    max-width: 300px;
    margin: 10px;
    border-radius: 15px;
}

.nav {
    margin: 30px 0;
}

.nav a {
    text-decoration: none;
    color: white;
    background: #c2185b;
    padding: 12px 22px;
    border-radius: 25px;
    margin: 5px;
    display: inline-block;
}
</style>
"""

# ---------------- AUDIO ----------------
# NOTE: Audio file is renamed to avoid cache issues

AUDIO = """
<audio id="bg-music" controls loop style="width:90%; margin:20px auto; display:block;">
    <source src="/static/love_v2.mp3" type="audio/mpeg">
</audio>

<script>
const music = document.getElementById("bg-music");

// Resume music after page change if it was playing
if (localStorage.getItem("musicPlaying") === "yes") {
    music.play().catch(() => {});
}

music.addEventListener("play", () => {
    localStorage.setItem("musicPlaying", "yes");
});

music.addEventListener("pause", () => {
    localStorage.setItem("musicPlaying", "no");
});
</script>
"""

# ---------------- BASE HTML ----------------

BASE_HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>For Hazel ❤️</title>
{style}
</head>
<body>
{audio}
{content}
</body>
</html>
"""

# ---------------- HOME (FIRST PAGE) ----------------

@app.route("/")
def home():
    met_days = (date.today() - date(2024, 9, 4)).days
    dating_days = (date.today() - date(2024, 10, 8)).days

    content = f"""
    <div class="fade">
        <h1>Our Beginning ❤️</h1>

        <p>
            We met on <b>4th September 2024</b><br>
            And started dating on <b>8th October 2024</b>
        </p>

        <h2>⏳ {met_days} days since we met</h2>
        <h2>💖 {dating_days} days since we became us</h2>

        <div class="images">
            <img src="/static/img1.jpg">
            <img src="/static/img2.jpg">
        </div>

        <div class="nav">
            <a href="/poem">Next ➜</a>
        </div>
    </div>
    """

    return render_template_string(
        BASE_HTML.format(style=STYLE, audio=AUDIO, content=content)
    )

# ---------------- POEM 1 ----------------

@app.route("/poem")
def poem():
    content = """
    <div class="fade">
        <h1>For You 💖</h1>

        <div class="poem">
The brown eyes ,
The long hair

The beautiful fragrance
Is it what I fell for ?
From considering love to be a distraction,
To falling harder for you everyday ...
From being an cold hearted boy ,
To being a emotional soft hearted person ...
From being an independent guy ,
To being Totally dependent on your love
Just the eyes , the hair , and the fragrance couldn't be all that I fell for ...

Now that I think ,
Now that I know ,
It was something that was planned
I think they call this destiny !
You came like a bright light into my dull life
You came like a ray of hope into my hopeless mind
You came like a blessing ....
YOU are what I fell for ...

You are my home
My safe place , my peace
You are my strength ..
For you I would cross a 1000 miles
There are no boundaries
I will always be there ,
To protect you ,
To guide you
To support you ..
I'll be your shadow
You will never be alone ...

I love you ..
        </div>

        <div class="images">
            <img src="/static/img3.jpg">
            <img src="/static/img4.jpg">
        </div>

        <div class="nav">
            <a href="/">⬅ Back</a>
            <a href="/poem2">Next ➜</a>
        </div>
    </div>
    """

    return render_template_string(
        BASE_HTML.format(style=STYLE, audio=AUDIO, content=content)
    )

# ---------------- POEM 2 ----------------

@app.route("/poem2")
def poem2():
    content = """
    <div class="fade">
        <h1>Always You ❤️</h1>

        <div class="poem">
Hazel
Remember ? The time we first met ..
Remember ? The blue lagoon ..
Remember? How you were trying to comfort me when I was all shy
Remember ? The note I gave you and left without even saying goodbye

Because I remember,
I remember the time I first saw your eyes
I remember getting lost again and again being around you
I remember how the world became silent for some time when you were around me
I remember the blue lagoon
I remember how I just gave you the note and left without saying goodbye ,
just because I didn't want to say goodbye ,
hoping we would meet again
It's been a year remember ?
        </div>

        <div class="images">
            <img src="/static/img5.jpg">
            <img src="/static/img6.jpg">
        </div>

        <div class="nav">
            <a href="/poem">⬅ Back</a>
            <a href="/promise">Next ➜</a>
        </div>
    </div>
    """

    return render_template_string(
        BASE_HTML.format(style=STYLE, audio=AUDIO, content=content)
    )

# ---------------- PROMISE ----------------

@app.route("/promise")
def promise():
    content = """
    <div class="fade">
        <h1>One Promise 🕊️</h1>

        <p>
            No matter what life brings,<br>
            No matter how hard days get,<br><br>

            I choose you.<br>
            Every day.<br><br>

            Always you.<br>
            Always us. ❤️
        </p>

        <div class="nav">
            <a href="/">⬅ Back Home</a>
        </div>
    </div>
    """

    return render_template_string(
        BASE_HTML.format(style=STYLE, audio=AUDIO, content=content)
    )

# ---------------- SAFE ENTRY ----------------

@app.route("/start")
def start():
    return redirect(url_for("home"))

# ---------------- RUN ----------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
