# -*- coding: utf-8 -*-

from flask import Flask, render_template_string
from datetime import date
import os

app = Flask(__name__)

# ================== STYLE ==================

STYLE = """
<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    background: linear-gradient(180deg, #ffe6f0, #ffffff);
    color: #333;
    overflow-x: hidden;
}

/* FLOATING HEARTS */
.hearts {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;
}

.heart {
    position: absolute;
    bottom: -20px;
    font-size: 18px;
    color: rgba(194, 24, 91, 0.25);
    animation: floatUp 8s linear infinite;
}

@keyframes floatUp {
    from { transform: translateY(0) scale(1); opacity: 1; }
    to { transform: translateY(-110vh) scale(1.6); opacity: 0; }
}

/* TAP TO BEGIN */
#tap-screen {
    position: fixed;
    inset: 0;
    background: linear-gradient(180deg, #ffe6f0, #ffffff);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 9999;
}

.tap-box {
    text-align: center;
    animation: glowPulse 2s infinite;
}

.tap-box h1 {
    color: #c2185b;
    font-size: 34px;
}

.tap-box p {
    font-size: 16px;
    opacity: 0.8;
}

@keyframes glowPulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.08); }
    100% { transform: scale(1); }
}

/* MAIN */
.container {
    max-width: 720px;
    margin: auto;
    padding: 20px 16px 40px;
    text-align: center;
    position: relative;
    z-index: 1;
    animation: fadeSlide 1.2s ease;
}

@keyframes fadeSlide {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

h1 {
    color: #c2185b;
    font-size: 28px;
}

h2 {
    color: #880e4f;
    font-size: 18px;
}

p {
    font-size: 15px;
    line-height: 1.8;
}

.poem {
    white-space: pre-line;
    text-align: left;
    font-size: 15px;
    line-height: 1.9;
    margin-top: 24px;
}

.images {
    display: flex;
    flex-direction: column;
    gap: 14px;
    margin-top: 24px;
}

.images img {
    width: 100%;
    border-radius: 18px;
    animation: floatImage 6s ease-in-out infinite;
}

@keyframes floatImage {
    0% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0); }
}

audio { display: none; }

.nav {
    margin-top: 32px;
}

.nav a {
    background: #c2185b;
    color: white;
    padding: 12px 22px;
    border-radius: 999px;
    text-decoration: none;
    font-size: 14px;
    margin: 6px;
    display: inline-block;
}

/* Desktop */
@media (min-width: 768px) {
    h1 { font-size: 34px; }
    p, .poem { font-size: 16px; }

    .images {
        flex-direction: row;
        justify-content: center;
    }

    .images img {
        max-width: 48%;
    }
}
</style>
"""

# ================== AUDIO ==================

AUDIO = """
<audio id="music" autoplay>
    <source src="/static/love_v2.mp3" type="audio/mpeg">
</audio>
"""

# ================== TAP SCRIPT ==================

TAP_SCRIPT = """
<div id="tap-screen">
    <div class="tap-box">
        <h1>Tap to Begin ❤️</h1>
        <p>For Hazel</p>
    </div>
</div>

<script>
const music = document.getElementById("music");
const tapScreen = document.getElementById("tap-screen");

if (sessionStorage.getItem("musicUnlocked") === "yes") {
    tapScreen.style.display = "none";
    music.play().catch(() => {});
}

tapScreen.addEventListener("click", () => {
    sessionStorage.setItem("musicUnlocked", "yes");
    music.play().catch(() => {});
    tapScreen.style.display = "none";
});
</script>
"""

# ================== HEARTS ==================

HEARTS = """
<div class="hearts">
""" + "".join(
    f'<div class="heart" style="left:{i*10}%; animation-delay:{i}s;">❤️</div>'
    for i in range(1, 10)
) + """
</div>
"""

# ================== COUNTDOWN ==================

COUNTDOWN = """
<div class="countdown">
    <h3>Countdown to Our Anniversary 💖</h3>
    <div id="timer">Loading...</div>
</div>

<script>
function updateCountdown() {
    const nowUTC = new Date();
    const nowIST = new Date(nowUTC.getTime() + (5.5 * 60 * 60 * 1000));

    let year = nowIST.getFullYear();
    let anniversary = new Date(Date.UTC(year, 9, 8));

    if (nowIST > anniversary) {
        anniversary = new Date(Date.UTC(year + 1, 9, 8));
    }

    const diff = anniversary - nowIST;

    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
    const minutes = Math.floor((diff / (1000 * 60)) % 60);
    const seconds = Math.floor((diff / 1000) % 60);

    document.getElementById("timer").innerText =
        `${days}d ${hours}h ${minutes}m ${seconds}s`;
}

setInterval(updateCountdown, 1000);
updateCountdown();
</script>
"""

# ================== BASE HTML ==================

BASE_HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>For Hazel ❤️</title>
{style}
</head>
<body>
{hearts}
{audio}
{tap}
<div class="container">
{content}
</div>
</body>
</html>
"""

# ================== ROUTES ==================

@app.route("/")
def home():
    met_days = (date.today() - date(2024, 9, 4)).days
    dating_days = (date.today() - date(2024, 10, 8)).days

    content = f"""
    <h1>Our Beginning ❤️</h1>
    {COUNTDOWN}

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
    """
    return render_template_string(BASE_HTML.format(
        style=STYLE, hearts=HEARTS, audio=AUDIO, tap=TAP_SCRIPT, content=content
    ))

@app.route("/poem")
def poem():
    content = """
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
    """
    return render_template_string(BASE_HTML.format(
        style=STYLE, hearts=HEARTS, audio=AUDIO, tap=TAP_SCRIPT, content=content
    ))

@app.route("/poem2")
def poem2():
    content = """
    <h1>Always You ❤️</h1>

    <div class="poem">
Hazel
Remember ? The time we first met ..
Remember ? The blue lagoon ..
Remember? How you were trying to comfort me when I was all shy
Remember ? The note I gave you and left without even saying goodbye

Because I remember,
I remember the time i first saw your eyes
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
    """
    return render_template_string(BASE_HTML.format(
        style=STYLE, hearts=HEARTS, audio=AUDIO, tap=TAP_SCRIPT, content=content
    ))

@app.route("/promise")
def promise():
    content = """
    <h1>One Promise 🕊️</h1>

    <p>
        I choose you.<br>
        Every day.<br><br>
        Always you.<br>
        Always us. ❤️
    </p>

    <div class="nav">
        <a href="/">⬅ Back Home</a>
    </div>
    """
    return render_template_string(BASE_HTML.format(
        style=STYLE, hearts=HEARTS, audio=AUDIO, tap=TAP_SCRIPT, content=content
    ))

# ================== RUN ==================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
