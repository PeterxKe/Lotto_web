import streamlit as st
import random
import time

st.sidebar.title("Menü")
wahl = st.sidebar.selectbox("Option wählen", ["Lotto spielen", "Über diese APP"])

if wahl == "Über diese APP":
    st.header("Mitwirkende")
    st.markdown("[• Peter Kemmeter (peterxke) – Entwickler](https://github.com/PeterxKe)")
    st.write("• Copilot – KI‑Support")

    st.divider()

    st.header("Über diese App")
    st.write("Version 1.0.0")
    st.write("Erstellt 01.06.2026")
    st.write("Hochgeladen 04.06.2026")

    st.divider()

    st.header("Weitere APPs")
    st.markdown("[• x² Calculator](https://x2-calculator.streamlit.app/)")

else:

    st.title("🎰 Lotto 6 aus 49")
    
    # Profit speichern
    if "profit" not in st.session_state:
        st.session_state.profit = 0
    
    # Loading Animation
    with st.spinner("Loading..."):
        time.sleep(1)
    
    st.write("## Einsatz: 5€ (fest)")
    
    # Eingabe der 6 Zahlen
    st.write("### Deine Zahlen eingeben")
    deine_zahlen = []
    for i in range(6):
        zahl = st.number_input(f"Zahl {i+1} (1–49)", min_value=1, max_value=49, key=f"zahl{i}")
        deine_zahlen.append(zahl)
    
    # Button zum Starten
    if st.button("Lotto spielen"):
        # Lottozahlen ziehen
        lotto_zahlen = []
        while len(lotto_zahlen) < 6:
            z = random.randint(1, 49)
            if z not in lotto_zahlen:
                lotto_zahlen.append(z)
        lotto_zahlen.sort()
    
        # Treffer zählen
        treffer = sum(1 for z in deine_zahlen if z in lotto_zahlen)
    
        st.write("## Ergebnis")
        st.write("Deine Zahlen:", deine_zahlen)
        st.write("Lottozahlen:", lotto_zahlen)
        st.write("Treffer:", treffer)
    
        # Gewinnklassen
        if treffer == 6:
            st.success("💰 JACKPOT!!! 6 Richtige!")
        elif treffer == 5:
            st.success("🔥 5 Richtige! Mega stark!")
        elif treffer == 4:
            st.success("🎉 4 Richtige! Sehr gut!")
        elif treffer == 3:
            st.info("😎 3 Richtige! Kleiner Gewinn!")
        elif treffer == 2:
            st.warning("🙂 2 Richtige – fast!")
        else:
            st.error("😢 Leider kein Gewinn...")
    
        # Gewinn berechnen
        gewinn = 0
        if treffer == 6:
            gewinn = 1000000
        elif treffer == 5:
            gewinn = 5000
        elif treffer == 4:
            gewinn = 200
        elif treffer == 3:
            gewinn = 20
    
        st.write("### Gewinn:", gewinn, "€")
    
        # Profit aktualisieren
        st.session_state.profit += gewinn - 5
        st.write("### Gesamt‑Profit:", st.session_state.profit, "€")
