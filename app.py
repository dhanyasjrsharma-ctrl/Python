import random
import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Number Hunt",
    page_icon="🎯",
    layout="centered",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Space+Mono:wght@400;700&display=swap');

/* ── Reset & base ── */
html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
}

.stApp {
    background: #0d0d0d;
    color: #f0f0f0;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }

/* ── Hero title ── */
.hero {
    text-align: center;
    padding: 2.5rem 0 1rem;
}
.hero h1 {
    font-family: 'Space Mono', monospace;
    font-size: 3rem;
    font-weight: 700;
    letter-spacing: -1px;
    color: #ffffff;
    margin: 0;
    line-height: 1.1;
}
.hero h1 span {
    color: #7DF9FF;          /* electric cyan – the one bold accent */
}
.hero p {
    color: #666;
    font-size: 0.95rem;
    margin-top: 0.5rem;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}

/* ── Card container ── */
.card {
    background: #161616;
    border: 1px solid #222;
    border-radius: 16px;
    padding: 2rem 2.2rem;
    margin: 1.5rem 0;
}

/* ── Stat pills (attempts / range) ── */
.stats-row {
    display: flex;
    gap: 0.75rem;
    justify-content: center;
    margin-bottom: 1.4rem;
    flex-wrap: wrap;
}
.stat-pill {
    background: #1e1e1e;
    border: 1px solid #2a2a2a;
    border-radius: 999px;
    padding: 0.35rem 1rem;
    font-family: 'Space Mono', monospace;
    font-size: 0.8rem;
    color: #999;
    letter-spacing: 0.04em;
}
.stat-pill strong { color: #7DF9FF; }

/* ── Feedback banner ── */
.feedback {
    text-align: center;
    padding: 1rem;
    border-radius: 10px;
    margin: 1rem 0;
    font-size: 1.05rem;
    font-weight: 500;
    letter-spacing: 0.01em;
}
.feedback.low  { background: #1a1200; border: 1px solid #4a3200; color: #FFB347; }
.feedback.high { background: #12001a; border: 1px solid #3a0048; color: #CF9FFF; }
.feedback.win  { background: #001a0d; border: 1px solid #00552a; color: #7DF9FF; }
.feedback.info { background: #121212; border: 1px solid #222;    color: #888;    }

/* ── Guess history list ── */
.history-title {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: #444;
    margin-bottom: 0.6rem;
}
.history-row {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    padding: 0.3rem 0;
    border-bottom: 1px solid #1a1a1a;
    font-family: 'Space Mono', monospace;
    font-size: 0.85rem;
    color: #777;
}
.history-row:last-child { border-bottom: none; }
.history-num { color: #f0f0f0; font-weight: 700; min-width: 2.5rem; }
.badge {
    font-size: 0.65rem;
    padding: 0.15rem 0.5rem;
    border-radius: 999px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}
.badge.low  { background: #4a3200; color: #FFB347; }
.badge.high { background: #3a0048; color: #CF9FFF; }
.badge.win  { background: #00552a; color: #7DF9FF; }

/* ── Input override ── */
input[type="number"] {
    background: #1e1e1e !important;
    border: 1px solid #333 !important;
    color: #f0f0f0 !important;
    border-radius: 10px !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 1.1rem !important;
}
input[type="number"]:focus {
    border-color: #7DF9FF !important;
    box-shadow: 0 0 0 3px rgba(125,249,255,0.12) !important;
}

/* ── Button ── */
div.stButton > button {
    width: 100%;
    background: #7DF9FF;
    color: #0d0d0d;
    border: none;
    border-radius: 10px;
    padding: 0.65rem 1rem;
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 1rem;
    letter-spacing: 0.04em;
    transition: opacity 0.15s;
    cursor: pointer;
}
div.stButton > button:hover { opacity: 0.85; }
div.stButton > button:active { opacity: 0.7; }

/* secondary / reset button */
div[data-testid="column"]:nth-child(2) div.stButton > button {
    background: #1e1e1e;
    color: #888;
    border: 1px solid #2a2a2a;
}

/* ── Progress bar ── */
.stProgress > div > div > div > div {
    background: #7DF9FF !important;
}
.stProgress > div > div {
    background: #1e1e1e !important;
}
</style>
""", unsafe_allow_html=True)

# ── Session state init ─────────────────────────────────────────────────────
def init_game():
    st.session_state.number   = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.history  = []          # list of (guess, result)
    st.session_state.won      = False
    st.session_state.lost     = False
    st.session_state.feedback = None
    st.session_state.max_tries = 10

if "number" not in st.session_state:
    init_game()

MAX = st.session_state.max_tries
ss  = st.session_state

# ── Hero ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <h1>NUMBER <span>HUNT</span></h1>
  <p>1 – 100 &nbsp;·&nbsp; 10 chances</p>
</div>
""", unsafe_allow_html=True)

# ── Stats pills ────────────────────────────────────────────────────────────
remaining = MAX - ss.attempts
st.markdown(f"""
<div class="stats-row">
  <div class="stat-pill">Attempts &nbsp;<strong>{ss.attempts}</strong></div>
  <div class="stat-pill">Remaining &nbsp;<strong>{remaining}</strong></div>
  <div class="stat-pill">Range &nbsp;<strong>1 – 100</strong></div>
</div>
""", unsafe_allow_html=True)

# ── Progress bar ───────────────────────────────────────────────────────────
st.progress(ss.attempts / MAX)

# ── Feedback banner ────────────────────────────────────────────────────────
if ss.won:
    st.markdown(f'<div class="feedback win">🎯 Nailed it! The number was <strong>{ss.number}</strong>. You cracked it in <strong>{ss.attempts}</strong> guess{"es" if ss.attempts != 1 else ""}.</div>', unsafe_allow_html=True)
    st.balloons()
elif ss.lost:
    st.markdown(f'<div class="feedback high">💀 Out of guesses. The number was <strong>{ss.number}</strong>. Better luck next round.</div>', unsafe_allow_html=True)
    st.snow()
elif ss.feedback == "low":
    st.markdown('<div class="feedback low">↑ Too low — aim higher.</div>', unsafe_allow_html=True)
elif ss.feedback == "high":
    st.markdown('<div class="feedback high">↓ Too high — come down a bit.</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="feedback info">Pick a number between 1 and 100 and hit Guess.</div>', unsafe_allow_html=True)

# ── Input & buttons ────────────────────────────────────────────────────────
game_over = ss.won or ss.lost

with st.container():
    guess_val = st.number_input(
        "Your guess",
        min_value=1,
        max_value=100,
        step=1,
        key="guess_input",
        disabled=game_over,
        label_visibility="collapsed",
    )

    col1, col2 = st.columns([3, 1])
    with col1:
        if st.button("Guess", disabled=game_over, use_container_width=True):
            guess = int(guess_val)
            ss.attempts += 1

            if guess < ss.number:
                ss.feedback = "low"
                ss.history.append((guess, "low"))
            elif guess > ss.number:
                ss.feedback = "high"
                ss.history.append((guess, "high"))
            else:
                ss.feedback = "win"
                ss.history.append((guess, "win"))
                ss.won = True

            if not ss.won and ss.attempts >= MAX:
                ss.lost = True

            st.rerun()

    with col2:
        if st.button("↺ Reset", use_container_width=True):
            init_game()
            st.rerun()

# ── Guess history ──────────────────────────────────────────────────────────
if ss.history:
    labels = {"low": ("↑ Low", "low"), "high": ("↓ High", "high"), "win": ("✓ Win", "win")}
    rows_html = ""
    for i, (g, r) in enumerate(reversed(ss.history), 1):
        label, cls = labels[r]
        rows_html += f"""
        <div class="history-row">
          <span style="color:#444;min-width:1.5rem">#{len(ss.history)-i+1}</span>
          <span class="history-num">{g}</span>
          <span class="badge {cls}">{label}</span>
        </div>"""

    st.markdown(f"""
    <div class="card">
      <div class="history-title">Guess history</div>
      {rows_html}
    </div>
    """, unsafe_allow_html=True)