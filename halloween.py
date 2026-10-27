import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# ============================================================
# CONFIG
# ============================================================

st.set_page_config(
    page_title="Karnage",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.block-container {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
}

.stApp {
    background: #030006;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# IMAGE DE FOND
# ============================================================

IMAGE_PATH = "karnage.png"

if os.path.exists(IMAGE_PATH):

    with open(IMAGE_PATH, "rb") as image_file:
        encoded_image = base64.b64encode(
            image_file.read()
        ).decode()

    background_css = """
    background-image:
        linear-gradient(
            rgba(3,0,10,0.30),
            rgba(3,0,10,0.75)
        ),
        url("data:image/png;base64,IMAGE_DATA");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    """

    background_css = background_css.replace(
        "IMAGE_DATA",
        encoded_image
    )

else:

    background_css = """
    background:
        radial-gradient(
            circle at center,
            #3c0070 0%,
            #120024 45%,
            #030006 100%
        );
    """


# ============================================================
# HTML
# ============================================================

html = """
<!DOCTYPE html>

<html lang="fr">

<head>

<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
>

<style>

* {
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
    padding: 0;

    overflow-x: hidden;

    color: white;

    font-family:
        Arial,
        Helvetica,
        sans-serif;

    BACKGROUND_CSS
}


/* =========================
   OVERLAY
========================= */

.overlay {

    position: fixed;

    inset: 0;

    background:
        radial-gradient(
            circle at center,
            rgba(90,0,170,0.08),
            rgba(0,0,0,0.72)
        );

    pointer-events: none;

    z-index: 0;
}


/* =========================
   ÉTOILES
========================= */

#stars {

    position: fixed;

    inset: 0;

    width: 100%;
    height: 100%;

    pointer-events: none;

    z-index: 1;
}


/* =========================
   NAVBAR
========================= */

.navbar {

    position: sticky;

    top: 0;

    z-index: 100;

    min-height: 90px;

    padding:
        0
        50px;

    display: flex;

    align-items: center;
    justify-content: space-between;

    background:
        rgba(6,0,16,0.90);

    backdrop-filter:
        blur(18px);

    border-bottom:
        1px solid
        rgba(170,70,255,0.40);

    box-shadow:
        0 0 40px
        rgba(120,0,255,0.25);
}


/* =========================
   KARNAGE
========================= */

.logo {

    font-size: 36px;

    font-weight: 900;

    letter-spacing: 8px;

    background:
        linear-gradient(
            90deg,
            #ffffff,
            #d38cff,
            #7524ff,
            #ffffff
        );

    background-size: 300%;

    -webkit-background-clip: text;

    color: transparent;

    animation:
        logoAnimation
        5s
        linear
        infinite;

    text-shadow:
        0 0 25px
        rgba(160,70,255,0.8);
}


@keyframes logoAnimation {

    from {
        background-position: 0%;
    }

    to {
        background-position: 300%;
    }

}


/* =========================
   MENU
========================= */

.menu {

    display: flex;

    gap: 14px;

    flex-wrap: wrap;
}


.menu button {

    padding:
        12px
        20px;

    border-radius: 14px;

    border:
        1px solid
        rgba(180,70,255,0.40);

    background:
        rgba(35,0,60,0.55);

    color: #ddd;

    font-weight: bold;

    cursor: pointer;

    transition:
        0.25s;
}


.menu button:hover {

    transform:
        translateY(-5px)
        scale(1.05);

    background:
        rgba(110,20,180,0.48);

    border-color:
        #c980ff;

    color: white;

    box-shadow:
        0 0 25px
        rgba(160,50,255,0.80);
}


.menu button.active {

    color: white;

    background:
        linear-gradient(
            135deg,
            #52008f,
            #982eff
        );

    box-shadow:
        0 0 25px
        rgba(160,50,255,0.80);
}


/* =========================
   CONTENU
========================= */

.content {

    position: relative;

    z-index: 5;

    width: 94%;

    max-width: 1450px;

    margin: auto;

    padding:
        60px
        20px
        150px;
}


.page {
    display: none;
}


.page.active {
    display: block;
}


/* =========================
   ACCUEIL
========================= */

.hero {

    min-height: 650px;

    display: flex;

    flex-direction: column;

    justify-content: center;
    align-items: center;

    text-align: center;
}


.hero-small {

    color: #ce8cff;

    letter-spacing: 8px;

    font-weight: bold;

    font-size: 14px;

    text-shadow:
        0 0 15px
        #992eff;
}


.hero h1 {

    margin:
        20px
        0;

    font-size:
        clamp(
            70px,
            11vw,
            160px
        );

    letter-spacing: 12px;

    line-height: 1;

    background:
        linear-gradient(
            180deg,
            #ffffff,
            #d384ff,
            #6616bd
        );

    -webkit-background-clip: text;

    color: transparent;

    filter:
        drop-shadow(
            0 0 25px
            rgba(170,70,255,0.95)
        );
}


.hero-box {

    max-width: 760px;

    padding:
        25px
        35px;

    border-radius: 24px;

    background:
        rgba(10,0,20,0.72);

    backdrop-filter:
        blur(15px);

    border:
        1px solid
        rgba(190,100,255,0.38);

    box-shadow:
        0 0 45px
        rgba(120,0,200,0.30);

    color: #ddd;

    font-size: 19px;

    line-height: 1.7;

    transition:
        0.3s;
}


.hero-box:hover {

    transform:
        translateY(-6px);

    box-shadow:
        0 0 60px
        rgba(160,40,255,0.55);
}


/* =========================
   TITRES
========================= */

.section-title {

    text-align: center;

    font-size: 50px;

    text-shadow:
        0 0 25px
        #9c3cff;

    margin-bottom: 10px;
}


.section-subtitle {

    text-align: center;

    color: #d6c5e3;

    font-size: 18px;

    margin-bottom: 50px;
}


/* =========================
   WINNER
========================= */

.winner {

    max-width: 900px;

    margin:
        0
        auto
        50px;

    padding: 28px;

    text-align: center;

    border-radius: 22px;

    background:
        linear-gradient(
            135deg,
            rgba(100,0,180,0.50),
            rgba(20,0,40,0.88)
        );

    border:
        1px solid
        rgba(210,130,255,0.55);

    box-shadow:
        0 0 40px
        rgba(140,30,255,0.40);

    transition:
        0.3s;
}


.winner:hover {

    transform:
        scale(1.02);

    box-shadow:
        0 0 60px
        rgba(160,60,255,0.65);
}


.winner-name {

    color:
        #e7bdff;

    font-size: 34px;

    font-weight: 900;

    text-shadow:
        0 0 20px
        #a331ff;
}


/* =========================
   VIDÉOS
========================= */

.video-grid {

    display: grid;

    grid-template-columns:
        repeat(
            auto-fit,
            minmax(280px,1fr)
        );

    gap: 30px;
}


.video-card {

    padding: 15px;

    border-radius: 24px;

    background:
        linear-gradient(
            145deg,
            rgba(30,0,55,0.94),
            rgba(5,0,15,0.96)
        );

    border:
        1px solid
        rgba(170,70,255,0.38);

    box-shadow:
        0 15px 50px
        rgba(0,0,0,0.65);

    transition:
        0.35s;
}


.video-card:hover {

    transform:
        translateY(-12px)
        scale(1.02);

    border-color:
        #ce84ff;

    box-shadow:
        0 0 30px
        rgba(150,40,255,0.55),
        0 22px 65px
        rgba(0,0,0,0.80);
}


.video-number {

    color:
        #bd72ff;

    letter-spacing: 3px;

    font-size: 13px;

    margin:
        4px
        5px
        10px;
}


.video-title {

    font-size: 22px;

    font-weight: bold;

    margin:
        0
        5px
        15px;
}


.video {

    position: relative;

    width: 100%;

    aspect-ratio:
        9 / 16;

    overflow: hidden;

    border-radius: 18px;

    background: black;
}


.video iframe {

    position: absolute;

    inset: 0;

    width: 100%;
    height: 100%;

    border: 0;
}


/* =========================
   EMPTY
========================= */

.empty {

    max-width: 700px;

    margin:
        80px
        auto;

    padding: 50px;

    text-align: center;

    border-radius: 24px;

    background:
        rgba(20,0,40,0.78);

    border:
        1px solid
        rgba(160,70,255,0.40);

    color:
        #d1c0dc;

    box-shadow:
        0 0 40px
        rgba(100,0,180,0.28);
}


/* =========================
   MOBILE
========================= */

@media(max-width: 800px) {

    .navbar {

        padding: 20px;

        flex-direction: column;

        gap: 20px;

    }


    .menu {

        justify-content: center;
    }


    .logo {

        font-size: 28px;
    }


    .hero h1 {

        letter-spacing: 5px;
    }


    .section-title {

        font-size: 36px;
    }

}

</style>

</head>

<body>


<div class="overlay"></div>

<canvas id="stars"></canvas>


<!-- ========================
     NAVBAR
======================== -->

<div class="navbar">

    <div class="logo">
        KARNAGE
    </div>

    <div class="menu">

        <button
            class="active"
            onclick="showPage('home', this)">
            🌌 Accueil
        </button>

        <button
            onclick="showPage('giveaway', this)">
            🏆 Preuves Giveaways
        </button>

        <button
            onclick="showPage('horror', this)">
            👻 Horreur
        </button>

        <button
            onclick="showPage('gaming', this)">
            🎮 Gaming
        </button>

    </div>

</div>


<div class="content">


<!-- ========================
     ACCUEIL
======================== -->

<div
    id="home"
    class="page active"
>

    <div class="hero">

        <div class="hero-small">
            ✦ OFFICIAL COMMUNITY ✦
        </div>

        <h1>
            KARNAGE
        </h1>

        <div class="hero-box">

            🌌 Bienvenue dans
            <strong>Karnage</strong>.

            <br><br>

            Retrouve ici les vidéos,
            les preuves de giveaways
            et les contenus de la communauté.

            <br><br>

            ✦ KARNAGE DISCORD ✦

        </div>

    </div>

</div>


<!-- ========================
     GIVEAWAYS
======================== -->

<div
    id="giveaway"
    class="page"
>

    <h1 class="section-title">
        🏆 PREUVES GIVEAWAYS
    </h1>

    <div class="section-subtitle">

        Les preuves vidéo des récompenses
        distribuées aux gagnants.

    </div>


    <div class="winner">

        🏆 GAGNANT

        <br><br>

        <div class="winner-name">
            RatCat067 Winner
        </div>

        <br>

        ✅ Giveaway remis avec succès

    </div>


    <div class="video-grid">


        <div class="video-card">

            <div class="video-number">
                PREUVE #01
            </div>

            <div class="video-title">
                🏆 RatCat067 Winner
            </div>

            <div class="video">

                <iframe
                    src="https://www.youtube.com/embed/SEI618dWsvA"
                    allowfullscreen>
                </iframe>

            </div>

        </div>


        <div class="video-card">

            <div class="video-number">
                PREUVE #02
            </div>

            <div class="video-title">
                🏆 RatCat067 Winner
            </div>

            <div class="video">

                <iframe
                    src="https://www.youtube.com/embed/mh0Zs37EzRo"
                    allowfullscreen>
                </iframe>

            </div>

        </div>


        <div class="video-card">

            <div class="video-number">
                PREUVE #03
            </div>

            <div class="video-title">
                🏆 RatCat067 Winner
            </div>

            <div class="video">

                <iframe
                    src="https://www.youtube.com/embed/mzJArXsVYGY"
                    allowfullscreen>
                </iframe>

            </div>

        </div>


        <div class="video-card">

            <div class="video-number">
                PREUVE #04
            </div>

            <div class="video-title">
                🏆 RatCat067 Winner
            </div>

            <div class="video">

                <iframe
                    src="https://www.youtube.com/embed/X-_70xRBReY"
                    allowfullscreen>
                </iframe>

            </div>

        </div>


        <div class="video-card">

            <div class="video-number">
                PREUVE #05
            </div>

            <div class="video-title">
                🏆 RatCat067 Winner
            </div>

            <div class="video">

                <iframe
                    src="https://www.youtube.com/embed/QAp8FFyEt7Y"
                    allowfullscreen>
                </iframe>

            </div>

        </div>


        <div class="video-card">

            <div class="video-number">
                PREUVE #06
            </div>

            <div class="video-title">
                🏆 RatCat067 Winner
            </div>

            <div class="video">

                <iframe
                    src="https://www.youtube.com/embed/faCYM6QFXfI"
                    allowfullscreen>
                </iframe>

            </div>

        </div>


        <div class="video-card">

            <div class="video-number">
                PREUVE #07
            </div>

            <div class="video-title">
                🏆 RatCat067 Winner
            </div>

            <div class="video">

                <iframe
                    src="https://www.youtube.com/embed/LA7MZjiwlO0"
                    allowfullscreen>
                </iframe>

            </div>

        </div>


    </div>

</div>


<!-- ========================
     HORREUR
======================== -->

<div
    id="horror"
    class="page"
>

    <h1 class="section-title">
        👻 HORREUR
    </h1>

    <div class="empty">

        👻 Les futures vidéos Halloween
        apparaîtront ici.

    </div>

</div>


<!-- ========================
     GAMING
======================== -->

<div
    id="gaming"
    class="page"
>

    <h1 class="section-title">
        🎮 GAMING
    </h1>

    <div class="empty">

        🎮 Les futures vidéos gaming
        Karnage apparaîtront ici.

    </div>

</div>


</div>


<script>

/* =========================
   MENU
========================= */

function showPage(pageId, button) {

    const pages =
        document.querySelectorAll(
            ".page"
        );

    pages.forEach(function(page) {

        page.classList.remove(
            "active"
        );

    });


    document
        .getElementById(pageId)
        .classList.add(
            "active"
        );


    const buttons =
        document.querySelectorAll(
            ".menu button"
        );


    buttons.forEach(function(btn) {

        btn.classList.remove(
            "active"
        );

    });


    button.classList.add(
        "active"
    );


    window.scrollTo({

        top: 0,

        behavior: "smooth"

    });

}


/* =========================
   GALAXIE
========================= */

const canvas =
    document.getElementById(
        "stars"
    );

const ctx =
    canvas.getContext(
        "2d"
    );


let width = 0;

let height = 0;

let mouseX = 0;

let mouseY = 0;


function resizeCanvas() {

    width =
        canvas.width =
        window.innerWidth;

    height =
        canvas.height =
        window.innerHeight;

}


resizeCanvas();


window.addEventListener(
    "resize",
    resizeCanvas
);


/* =========================
   SOURIS
========================= */

document.addEventListener(
    "mousemove",
    function(event) {

        mouseX =
            event.clientX;

        mouseY =
            event.clientY;

    }
);


/* =========================
   ÉTOILES
========================= */

const stars = [];


for (
    let i = 0;
    i < 220;
    i++
) {

    stars.push({

        x:
            Math.random()
            * window.innerWidth,

        y:
            Math.random()
            * window.innerHeight,

        size:
            Math.random()
            * 2.4
            + 0.3,

        speed:
            Math.random()
            * 0.30
            + 0.04,

        depth:
            Math.random()
            * 1.7
            + 0.2,

        twinkle:
            Math.random()
            * Math.PI
            * 2

    });

}


/* =========================
   ANIMATION
========================= */

function animateStars() {

    ctx.clearRect(
        0,
        0,
        width,
        height
    );


    const centerX =
        width / 2;

    const centerY =
        height / 2;


    stars.forEach(
        function(star) {

            star.twinkle +=
                0.025;

            star.y +=
                star.speed;


            if (
                star.y >
                height + 10
            ) {

                star.y = -10;

                star.x =
                    Math.random()
                    * width;

            }


            const offsetX =
                (
                    mouseX
                    - centerX
                )
                * 0.022
                * star.depth;


            const offsetY =
                (
                    mouseY
                    - centerY
                )
                * 0.022
                * star.depth;


            const x =
                star.x
                + offsetX;


            const y =
                star.y
                + offsetY;


            const alpha =
                0.5
                +
                Math.sin(
                    star.twinkle
                )
                * 0.35;


            ctx.beginPath();


            ctx.arc(
                x,
                y,
                star.size,
                0,
                Math.PI * 2
            );


            if (
                star.depth > 1
            ) {

                ctx.fillStyle =
                    "rgba(190,120,255,"
                    + alpha
                    + ")";

                ctx.shadowColor =
                    "#9d45ff";

                ctx.shadowBlur =
                    14;

            }

            else {

                ctx.fillStyle =
                    "rgba(255,255,255,"
                    + alpha
                    + ")";

                ctx.shadowColor =
                    "#ffffff";

                ctx.shadowBlur =
                    7;

            }


            ctx.fill();

        }
    );


    ctx.shadowBlur = 0;


    requestAnimationFrame(
        animateStars
    );

}


animateStars();

</script>


</body>

</html>
"""


# Injecte le fond sans f-string
html = html.replace(
    "BACKGROUND_CSS",
    background_css
)


# ============================================================
# AFFICHAGE
# ============================================================

components.html(
    html,
    height=4200,
    scrolling=True
)