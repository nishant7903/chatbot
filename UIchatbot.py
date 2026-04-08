
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# ─────────────────────────────────────────────
#  MODEL
# ─────────────────────────────────────────────
model = ChatMistralAI(model="mistral-small-2506", temperature=0.7)

# ─────────────────────────────────────────────
#  SYSTEM PROMPT
# ─────────────────────────────────────────────
SYSTEM_PROMPT = """
You are Marco, a warm and enthusiastic staff member at "DELIZIOSA Pizza" — a cozy, authentic Italian pizza restaurant.
Your job is to:
1. Greet customers warmly and make them feel welcome.
2. Help customers explore the menu and answer questions about any dish.
3. Make personalised pizza recommendations based on their taste, mood, or dietary preferences.
4. Handle order-taking conversationally (collect: pizza name, size, crust, quantity, any extras).
5. Inform about ongoing deals and combos.
6. Handle complaints or special requests with grace and positivity.
7. Provide estimated delivery/dine-in times when asked (~25-35 min delivery, ~15 min dine-in).
8. Always stay in character as a friendly Italian restaurant staff member. Use light Italian expressions like "Perfetto!", "Mamma mia!", "Benissimo!" naturally.

━━━ OUR MENU ━━━

🍕 CLASSIC PIZZAS (12" Regular | 14" Large | 16" XL)
• Margherita       ₹299 | ₹399 | ₹499  — Fresh tomato sauce, mozzarella, basil
• Pepperoni        ₹399 | ₹499 | ₹599  — Loaded pepperoni, mozzarella, tomato
• BBQ Chicken      ₹449 | ₹549 | ₹649  — Smoky BBQ sauce, grilled chicken, onions
• Veggie Supreme   ₹349 | ₹449 | ₹549  — Bell peppers, mushrooms, olives, corn, onions
• Farmhouse        ₹399 | ₹499 | ₹599  — Capsicum, mushroom, paneer, tomato
• Four Cheese      ₹449 | ₹549 | ₹649  — Mozzarella, cheddar, parmesan, gouda
• Paneer Tikka     ₹429 | ₹529 | ₹629  — Spiced paneer, capsicum, onion, tikka sauce

🍕 SIGNATURE SPECIALS
• DELIZIOSA Special  ₹549 | ₹649 | ₹749  — Chef's secret sauce, prosciutto, arugula, truffle oil
• Spicy Fiesta      ₹449 | ₹549 | ₹649  — Jalapeños, chorizo, red onion, sriracha drizzle
• White Garden      ₹399 | ₹499 | ₹599  — Garlic cream base, zucchini, spinach, ricotta

🥖 CRUSTS (no extra charge)
• Classic Hand-Tossed | Thin & Crispy | Stuffed Cheese Crust (+₹80) | Whole Wheat

🥗 SIDES & EXTRAS
• Garlic Bread          ₹129
• Cheesy Garlic Bread   ₹159
• Pasta Arrabbiata      ₹249
• Pasta Alfredo         ₹279
• Caesar Salad          ₹199
• Chicken Wings (6pc)   ₹329

🥤 BEVERAGES
• Soft Drinks (Pepsi/7Up/Mirinda)  ₹79
• Fresh Lemonade                   ₹99
• Iced Tea                         ₹109
• Mocktail of the Day              ₹149

🎉 COMBOS & DEALS
• Couple Combo: Any Large Pizza + 2 Soft Drinks + Garlic Bread = ₹699 (save ₹120)
• Family Feast: 2 Large Pizzas + Pasta + 4 Drinks + Garlic Bread = ₹1,399 (save ₹280)
• Solo Meal: Regular Pizza + Drink + Garlic Bread = ₹499 (save ₹90)
• Tuesday Special: Buy 1 Large, Get 1 Regular FREE

━━━ POLICIES ━━━
• Free delivery on orders above ₹499
• Delivery charge: ₹49 below ₹499
• Customisations welcome — extra toppings ₹49 each
• Veg & Non-Veg kitchen areas are separate
• Allergen info available on request

Always be helpful, cheerful, and make the customer feel like they're dining in Italy! 🇮🇹
"""

# ─────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="DELIZIOSA Pizza",
    page_icon="🍕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
#  CUSTOM CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Lato:wght@300;400;700&display=swap');

/* ── GLOBAL ── */
html, body, [data-testid="stAppViewContainer"] {
    background: #1a0a00;
    font-family: 'Lato', sans-serif;
}

[data-testid="stAppViewContainer"] {
    background: 
        radial-gradient(ellipse at 20% 20%, rgba(180,50,10,0.18) 0%, transparent 60%),
        radial-gradient(ellipse at 80% 80%, rgba(220,100,10,0.12) 0%, transparent 60%),
        #1a0a00;
}

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #200d00 0%, #2d1200 60%, #1a0a00 100%) !important;
    border-right: 1px solid rgba(220,100,20,0.25);
}

[data-testid="stSidebar"] * {
    color: #f0d9b5 !important;
}

/* ── SIDEBAR LOGO AREA ── */
.sidebar-logo {
    text-align: center;
    padding: 1.5rem 1rem 1rem;
    border-bottom: 1px solid rgba(220,100,20,0.3);
    margin-bottom: 1rem;
}
.sidebar-logo .logo-emoji {
    font-size: 3.5rem;
    display: block;
    margin-bottom: 0.4rem;
    filter: drop-shadow(0 0 12px rgba(255,140,0,0.6));
}
.sidebar-logo h1 {
    font-family: 'Playfair Display', serif !important;
    font-size: 1.55rem !important;
    color: #ff9a3c !important;
    margin: 0 0 0.15rem !important;
    letter-spacing: 0.03em;
    text-shadow: 0 0 20px rgba(255,140,0,0.4);
}
.sidebar-logo p {
    font-size: 0.75rem !important;
    color: #c08840 !important;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin: 0 !important;
}

/* ── MENU CARD ── */
.menu-section {
    background: rgba(255,140,0,0.06);
    border: 1px solid rgba(220,100,20,0.2);
    border-radius: 10px;
    padding: 0.85rem 1rem;
    margin-bottom: 0.75rem;
}
.menu-section h4 {
    font-family: 'Playfair Display', serif !important;
    color: #ff9a3c !important;
    font-size: 0.9rem !important;
    margin: 0 0 0.5rem !important;
    letter-spacing: 0.05em;
}
.menu-item {
    display: flex;
    justify-content: space-between;
    padding: 0.2rem 0;
    font-size: 0.78rem;
    color: #d4b896 !important;
    border-bottom: 1px solid rgba(255,255,255,0.04);
}
.menu-item:last-child { border-bottom: none; }
.menu-price { color: #ffa040 !important; font-weight: 700; }

/* ── BADGE ── */
.badge {
    display: inline-block;
    background: linear-gradient(135deg, #c0392b, #e74c3c);
    color: white !important;
    font-size: 0.65rem;
    padding: 0.15rem 0.5rem;
    border-radius: 20px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    font-weight: 700;
}

/* ── MAIN HEADER ── */
.main-header {
    text-align: center;
    padding: 2rem 1rem 1.5rem;
    position: relative;
}
.main-header::before {
    content: '';
    position: absolute;
    top: 0; left: 50%;
    transform: translateX(-50%);
    width: 120px; height: 2px;
    background: linear-gradient(90deg, transparent, #ff6b00, transparent);
}
.main-header h1 {
    font-family: 'Playfair Display', serif !important;
    font-size: 2.6rem !important;
    color: #ff9a3c !important;
    margin: 0 !important;
    text-shadow: 0 0 40px rgba(255,140,0,0.3);
    letter-spacing: -0.01em;
}
.main-header h1 em {
    color: #fff3e0;
    font-style: italic;
}
.main-header .subtitle {
    color: #a07040;
    font-size: 0.85rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    margin-top: 0.3rem;
}
.header-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255,100,0,0.4), transparent);
    margin: 1rem auto;
    max-width: 400px;
}

/* ── CHAT AREA ── */
.chat-container {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(220,100,20,0.15);
    border-radius: 16px;
    padding: 1.2rem;
    min-height: 420px;
    max-height: 520px;
    overflow-y: auto;
    margin-bottom: 1rem;
    scrollbar-width: thin;
    scrollbar-color: rgba(255,140,0,0.3) transparent;
}

/* ── USER BUBBLE ── */
[data-testid="stChatMessageContent"] {
    border-radius: 14px !important;
}
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) [data-testid="stChatMessageContent"] {
    background: linear-gradient(135deg, #c0392b 0%, #922b21 100%) !important;
    color: #fff !important;
    border-radius: 18px 18px 4px 18px !important;
    box-shadow: 0 4px 14px rgba(192,57,43,0.35);
}
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) [data-testid="stChatMessageContent"] {
    background: linear-gradient(135deg, #2d1a00 0%, #3d2200 100%) !important;
    color: #f0d9b5 !important;
    border: 1px solid rgba(220,100,20,0.25) !important;
    border-radius: 18px 18px 18px 4px !important;
    box-shadow: 0 4px 14px rgba(0,0,0,0.3);
}
[data-testid="stChatMessage"] p { color: inherit !important; }

/* ── CHAT INPUT ── */
[data-testid="stChatInput"] {
    background: rgba(30,15,0,0.8) !important;
    border: 1.5px solid rgba(220,100,20,0.35) !important;
    border-radius: 12px !important;
    color: #f0d9b5 !important;
    box-shadow: 0 0 0 0px rgba(255,100,0,0);
    transition: box-shadow 0.3s, border-color 0.3s;
}
[data-testid="stChatInput"]:focus-within {
    border-color: rgba(255,140,0,0.7) !important;
    box-shadow: 0 0 0 3px rgba(255,100,0,0.12) !important;
}
[data-testid="stChatInput"] textarea {
    color: #f0d9b5 !important;
    font-family: 'Lato', sans-serif !important;
}
[data-testid="stChatInput"] button {
    background: linear-gradient(135deg, #c0392b, #ff6b00) !important;
    border-radius: 8px !important;
}

/* ── QUICK BUTTONS ── */
.stButton button {
    background: rgba(255,140,0,0.08) !important;
    border: 1px solid rgba(220,100,20,0.35) !important;
    color: #ffa040 !important;
    border-radius: 20px !important;
    font-size: 0.78rem !important;
    padding: 0.3rem 0.9rem !important;
    transition: all 0.2s;
    font-family: 'Lato', sans-serif !important;
    letter-spacing: 0.03em;
}
.stButton button:hover {
    background: rgba(255,100,0,0.2) !important;
    border-color: rgba(255,140,0,0.6) !important;
    color: #ffcf80 !important;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(255,100,0,0.2) !important;
}

/* ── STATS ROW ── */
.stat-box {
    background: rgba(255,140,0,0.06);
    border: 1px solid rgba(220,100,20,0.2);
    border-radius: 10px;
    text-align: center;
    padding: 0.75rem 0.5rem;
}
.stat-box .stat-val {
    font-family: 'Playfair Display', serif;
    font-size: 1.4rem;
    color: #ff9a3c;
    font-weight: 700;
    display: block;
}
.stat-box .stat-label {
    font-size: 0.68rem;
    color: #7a5530;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}

/* ── DEAL BANNER ── */
.deal-banner {
    background: linear-gradient(135deg, rgba(192,57,43,0.15), rgba(255,100,0,0.1));
    border: 1px solid rgba(192,57,43,0.3);
    border-left: 3px solid #c0392b;
    border-radius: 0 8px 8px 0;
    padding: 0.6rem 0.9rem;
    margin-bottom: 0.5rem;
    font-size: 0.78rem;
    color: #f0c090;
}
.deal-banner strong { color: #ff8040; }

/* ── STATUS PILL ── */
.status-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: rgba(39,174,96,0.12);
    border: 1px solid rgba(39,174,96,0.3);
    border-radius: 20px;
    padding: 0.25rem 0.75rem;
    font-size: 0.72rem;
    color: #6fcf97;
    letter-spacing: 0.05em;
}
.dot { width:7px; height:7px; border-radius:50%; background:#2ecc71;
       box-shadow: 0 0 6px #2ecc71; animation: pulse 1.8s infinite; display:inline-block; }
@keyframes pulse { 0%,100%{opacity:1;} 50%{opacity:0.4;} }

/* ── MISC ── */
.section-label {
    font-size: 0.68rem;
    color: #7a5530;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    margin-bottom: 0.5rem;
    font-weight: 700;
}
hr { border-color: rgba(220,100,20,0.15) !important; }
[data-testid="stMarkdownContainer"] p { color: #b08050; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  SESSION STATE
# ─────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content=SYSTEM_PROMPT)]
if "chat_count" not in st.session_state:
    st.session_state.chat_count = 0


# ─────────────────────────────────────────────
#  SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:

    st.markdown("""
    <div class="sidebar-logo">
        <span class="logo-emoji">🍕</span>
        <h1>DELIZIOSA Pizza</h1>
        <p>Authentic Italian Since 1998</p>
    </div>
    """, unsafe_allow_html=True)

    # Status
    st.markdown("""
    <div style="text-align:center; margin-bottom:1rem;">
        <div class="status-pill"><span class="dot"></span> Marco is Online</div>
    </div>
    """, unsafe_allow_html=True)

    # Menu sections
    st.markdown('<div class="section-label">🍕 Quick Menu</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="menu-section">
        <h4>🍕 Classic Pizzas</h4>
        <div class="menu-item"><span>Margherita</span><span class="menu-price">₹299+</span></div>
        <div class="menu-item"><span>Pepperoni</span><span class="menu-price">₹399+</span></div>
        <div class="menu-item"><span>BBQ Chicken</span><span class="menu-price">₹449+</span></div>
        <div class="menu-item"><span>Four Cheese</span><span class="menu-price">₹449+</span></div>
        <div class="menu-item"><span>Paneer Tikka</span><span class="menu-price">₹429+</span></div>
    </div>
    <div class="menu-section">
        <h4>⭐ Signatures</h4>
        <div class="menu-item"><span> DELIZIOSA Special</span><span class="menu-price">₹549+</span></div>
        <div class="menu-item"><span>Spicy Fiesta</span><span class="menu-price">₹449+</span></div>
        <div class="menu-item"><span>White Garden</span><span class="menu-price">₹399+</span></div>
    </div>
    """, unsafe_allow_html=True)

    # Deals
    st.markdown('<div class="section-label" style="margin-top:0.5rem">🎉 Today\'s Deals</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="deal-banner"><strong>Tuesday Special:</strong> Buy 1 Large → Get 1 Regular FREE</div>
    <div class="deal-banner"><strong>Couple Combo:</strong> Large Pizza + 2 Drinks + Bread = ₹699</div>
    <div class="deal-banner"><strong>Free Delivery</strong> on orders above ₹499</div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Stats
    st.markdown('<div class="section-label">📊 Restaurant Info</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="stat-box">
            <span class="stat-val">4.8⭐</span>
            <span class="stat-label">Rating</span>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="stat-box">
            <span class="stat-val">25m</span>
            <span class="stat-label">Avg. Delivery</span>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🔄 New Conversation", use_container_width=True):
        st.session_state.messages = [SystemMessage(content=SYSTEM_PROMPT)]
        st.session_state.chat_count = 0
        st.rerun()


# ─────────────────────────────────────────────
#  MAIN AREA
# ─────────────────────────────────────────────
st.markdown("""
<div class="maiDELIZIOSA-header">
    <h1>🍕 <em></em> Pizza</h1>
    <div class="subtitle">Your personal Italian dining assistant</div>
    <div class="header-divider"></div>
</div>
""", unsafe_allow_html=True)

# Quick-action prompt buttons
st.markdown('<div class="section-label" style="text-align:center;">✨ Quick Actions</div>', unsafe_allow_html=True)

q_cols = st.columns(4)
quick_prompts = [
    ("📋 See Full Menu", "Show me your full menu please"),
    ("🔥 Best Sellers", "What are your best selling pizzas?"),
    ("🎉 Today's Deals", "Tell me about today's deals and combos"),
    ("🌱 Veg Options", "What vegetarian options do you have?"),
]

for i, (label, prompt) in enumerate(quick_prompts):
    with q_cols[i]:
        if st.button(label, use_container_width=True):
            st.session_state._quick_prompt = prompt

st.markdown("<br>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  CHAT HISTORY
# ─────────────────────────────────────────────
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user", avatar="👤"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant", avatar="👨‍🍳"):
            st.write(msg.content)

# Greeting on first load
if len(st.session_state.messages) == 1:
    with st.chat_message("assistant", avatar="👨‍🍳"):
        greeting = "Benvenuto! 🍕 Welcome to **DELIZIOSA Pizza**! I'm **Marco**, your personal dining assistant. Whether you're craving a classic Margherita, our signature  Special, or want to explore our deals — I'm here to help! What can I get started for you today? 😊"
        st.write(greeting)


# ─────────────────────────────────────────────
#  INPUT HANDLING
# ─────────────────────────────────────────────
def handle_message(user_input: str):
    """Process a user message and get AI response."""
    st.session_state.messages.append(HumanMessage(content=user_input))
    st.session_state.chat_count += 1

    with st.chat_message("user", avatar="👤"):
        st.write(user_input)

    with st.chat_message("assistant", avatar="👨‍🍳"):
        with st.spinner("Marco is preparing your answer... 🍕"):
            response = model.invoke(st.session_state.messages)
        st.write(response.content)

    st.session_state.messages.append(AIMessage(content=response.content))


# Handle quick-prompt button click
if hasattr(st.session_state, "_quick_prompt") and st.session_state._quick_prompt:
    prompt = st.session_state._quick_prompt
    st.session_state._quick_prompt = None
    handle_message(prompt)
    st.rerun()

# Handle typed input
user_input = st.chat_input("Ask Marco anything — menu, recommendations, orders, deals...")

if user_input:
    handle_message(user_input)
    st.rerun()


# ─────────────────────────────────────────────
#  FOOTER
# ─────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style="text-align:center; padding: 0.5rem 0 1rem;">
    <span style="color:#5a3a1a; font-size:0.75rem; letter-spacing:0.1em;">
        🍕 DELIZIOSA PIZZA &nbsp;·&nbsp; Authentic Italian &nbsp;·&nbsp; Open 11 AM – 11 PM &nbsp;·&nbsp; 📞 +91 7903525312
    </span>
</div>
""", unsafe_allow_html=True)