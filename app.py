# -*- coding: utf-8 -*-
from flask import Flask, render_template_string
from datetime import date

app = Flask(__name__)

STYLE = """
<style>
.poem {
    white-space: pre-line;
    font-size: 16px;
    line-height: 1.8;
    margin-top: 25px;
}

body {
    background: linear-gradient(to bottom, #ffdde1, #ee9ca7);
    font-family: Georgia, serif;
    text-align: center;
    padding: 20px;
    margin: 0;
    color: #2c2c2c;
    overflow-x: hidden;
}
h1 { font-size: 30px; }
h2 { font-size: 20px; margin: 15px 0; }
p { font-size: 16px; line-height: 1.7; }

.images {
    display: flex;
    flex-direction: column;
    align-items: center;
}
.images img {
    width: 90%;
    max-width: 320px;
    margin: 12px 0;
    border-radius: 18px;
    box-shadow: 0 10px 20px rgba(0,0,0,0.2);
}

.nav a {
    display: inline-block;
    padding: 12px 20px;
    margin: 10px;
    font-size: 16px;
    border-radius: 25px;
    background: rgba(255,255,255,0.6);
    color: #000;
    text-decoration: none;
    font-weight: bold;
    text-decoration: none;
}

.fade {
    animation: fadeIn 1.8s ease-in;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(15px); }
    to { opacity: 1; transform: translateY(0); }
}

.heart {
    position: fixed;
    bottom: -20px;
    font-size: 22px;
    animation: floatUp 6s linear infinite;
    opacity: 0.6;
}
@keyframes floatUp {
    0% { transform: translateY(0); opacity: 0; }
    50% { opacity: 0.8; }
    100% { transform: translateY(-100vh); opacity: 0; }
}
#music-btn {
    margin-top: 20px;
    padding: 10px 18px;
    font-size: 15px;
    border-radius: 20px;
    border: none;
    background: rgba(255,255,255,0.7);
    font-weight: bold;
}

</style>

<script>
function createHeart() {
    const heart = document.createElement("div");
    heart.className = "heart";
    heart.innerHTML = "💖";
    heart.style.left = Math.random() * 100 + "vw";
    document.body.appendChild(heart);
    setTimeout(() => heart.remove(), 6000);
}
setInterval(createHeart, 700);
</script>
"""

AUDIO = """
<audio id="bg-music" loop>
    <source src="/static/love.mp3" type="audio/mpeg">
</audio>

<button onclick="toggleMusic()" id="music-btn">🎵 Play Music</button>

<script>
let playing = false;
function toggleMusic() {
    const music = document.getElementById("bg-music");
    const btn = document.getElementById("music-btn");
    if (!playing) {
        music.play();
        btn.innerText = "⏸ Pause Music";
        playing = true;
    } else {
        music.pause();
        btn.innerText = "🎵 Play Music";
        playing = false;
    }
}
</script>
"""
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



@app.route("/start")
def start():

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
        BASE_HTML.format(
            style=STYLE,
            audio=AUDIO,
            content=content
        )
    )


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
        BASE_HTML.format(
            style=STYLE,
            audio=AUDIO,
            content=content
        )
    )


@app.route("/promise")
def promise():
    return render_template_string(
f"""{STYLE}
{AUDIO}

<div class="fade">
    <h1>One Promise 🕊️</h1>

    <p>
        I don’t know what the future looks like.<br>
        I don’t know where life will take us.<br><br>

        But I know one thing for sure.<br><br>

        I choose you.<br>
        In the calm days.<br>
        In the hard days.<br>
        In the days when nothing makes sense.<br><br>

        I promise to stand by you,<br>
        to listen to you,<br>
        to protect your peace,<br>
        and to love you in ways that feel safe and true.<br><br>

        No matter what changes,<br>
        this choice never will.
    </p>

    <h2>Always you. Always us. ❤️</h2>

    <div class="nav">
        <a href="/">⬅ Back Home</a>
    </div>
</div>
"""
)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
