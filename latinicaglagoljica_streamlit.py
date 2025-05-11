import streamlit as st

# Mape slova
glagoljica_u_latinicu = {
    'Ⰰ': 'A', 'ⰰ': 'a', 'Ⰱ': 'B', 'ⰱ': 'b', 'Ⰲ': 'V', 'ⰲ': 'v', 'Ⰳ': 'G', 'ⰳ': 'g',
    'Ⰴ': 'D', 'ⰴ': 'd', 'Ⰵ': 'E', 'ⰵ': 'e', 'Ⰶ': 'Ž', 'ⰶ': 'ž', 'Ⰷ': 'Z', 'ⰷ': 'z',
    'Ⰻ': 'I', 'ⰻ': 'i', 'Ⰼ': 'J', 'ⰼ': 'j', 'Ⰽ': 'K', 'ⰽ': 'k', 'Ⰾ': 'L', 'ⰾ': 'l',
    'Ⰿ': 'M', 'ⰿ': 'm', 'Ⱀ': 'N', 'ⱀ': 'n', 'Ⱁ': 'O', 'ⱁ': 'o', 'Ⱂ': 'P', 'ⱂ': 'p',
    'Ⱃ': 'R', 'ⱃ': 'r', 'Ⱄ': 'S', 'ⱄ': 's', 'Ⱅ': 'T', 'ⱅ': 't', 'Ⱆ': 'U', 'ⱆ': 'u',
    'Ⱇ': 'F', 'ⱇ': 'f', 'Ⱈ': 'H', 'ⱈ': 'h', 'Ⱌ': 'C', 'ⱌ': 'c', 'Ⱍ': 'Č', 'ⱍ': 'č',
    'Ⱎ': 'Š', 'ⱎ': 'š', 'Ⱋ': 'Ć', 'ⱋ': 'ć', '.': '.', ',': ',', '?': '?', '!': '!',
    ';': ';', '=': '='
}

latinica_u_glagoljicu = {
    'A': 'Ⰰ', 'a': 'ⰰ', 'B': 'Ⰱ', 'b': 'ⰱ', 'V': 'Ⰲ', 'v': 'ⰲ', 'G': 'Ⰳ', 'g': 'ⰳ',
    'D': 'Ⰴ', 'd': 'ⰴ', 'E': 'Ⰵ', 'e': 'ⰵ', 'Ž': 'Ⰶ', 'ž': 'ⰶ', 'Z': 'Ⰷ', 'z': 'ⰷ',
    'I': 'Ⰻ', 'i': 'ⰻ', 'J': 'Ⰼ', 'j': 'ⰼ', 'K': 'Ⰽ', 'k': 'ⰽ', 'L': 'Ⰾ', 'l': 'ⰾ',
    'M': 'Ⰿ', 'm': 'ⰿ', 'N': 'Ⱀ', 'n': 'ⱀ', 'O': 'Ⱁ', 'o': 'ⱁ', 'P': 'Ⱂ', 'p': 'ⱂ',
    'R': 'Ⱃ', 'r': 'ⱃ', 'S': 'Ⱄ', 's': 'ⱄ', 'T': 'Ⱅ', 't': 'ⱅ', 'U': 'Ⱆ', 'u': 'ⱆ',
    'F': 'Ⱇ', 'f': 'ⱇ', 'H': 'Ⱈ', 'h': 'ⱈ', 'C': 'Ⱌ', 'c': 'ⱌ', 'Č': 'Ⱍ', 'č': 'ⱍ',
    'Š': 'Ⱎ', 'š': 'ⱎ', 'Ć': 'Ⱋ', 'ć': 'ⱋ', 'Đ': 'Ⰼ', 'đ': 'ⰼ',
    ' ': ' ', '.': '.', ',': ',', '?': '?', '!': '!', ';': ';', '=': '='
}

# Streamlit UI
st.set_page_config(page_title="Prevoditelj Glagoljica ↔ Latinica", layout="centered")
st.title("🔤 Prevoditelj: Latinica ↔ Glagoljica")

# Izbor pravca
smjer = st.radio("Odaberite smjer prevođenja:", ["Latinica → Glagoljica", "Glagoljica → Latinica"])

# Unos teksta
tekst = st.text_area("Unesite tekst za prevođenje:")

# Dugme za prevođenje
if st.button("Prevedi"):
    if not tekst.strip():
        st.warning("Molimo unesite tekst.")
    else:
        rezultat = ""
        if "Latinica" in smjer:
            for znak in tekst:
                rezultat += latinica_u_glagoljicu.get(znak, znak)
        else:
            for znak in tekst:
                rezultat += glagoljica_u_latinicu.get(znak, znak)

        st.subheader("Prevedeni tekst:")
        st.code(rezultat)
