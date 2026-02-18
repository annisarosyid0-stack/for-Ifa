import streamlit as st
import time

st.set_page_config(page_title="For Agip ✨", page_icon="✨", layout="centered")

# Custom CSS aesthetic
st.markdown("""
    <style>
    body {
        background-color: #f8f6f1;
    }
    .big-text {
        font-size: 40px;
        text-align: center;
        font-weight: 600;
        color: #5e503f;
    }
    .sub-text {
        font-size: 20px;
        text-align: center;
        color: #8a817c;
    }
    .doa-box {
        background-color: #ede0d4;
        padding: 25px;
        border-radius: 15px;
        font-size: 18px;
        color: #3a5a40;
        text-align: center;
        line-height: 1.8;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-text">Barakallahu fii umrik, Agip ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Semoga Allah selalu melimpahkan keberkahan dalam setiap langkahmu.</p>', unsafe_allow_html=True)

st.write("")
st.write("")

if st.button("🎁 Buka Hadiah"):
    with st.spinner("Menyiapkan doa terbaik untukmu..."):
        time.sleep(2)

    st.success("✨ Doa Spesial Untuk Agip ✨")

    st.markdown("""
        <div class="doa-box">
        Semoga di usia yang baru ini,<br><br>
        Allah menambahkan imanmu,<br>
        melapangkan rezekimu,<br>
        memudahkan setiap urusanmu,<br>
        dan menjadikan kamu pribadi yang lebih kuat dan tenang.<br><br>
        Terima kasih sudah jadi teman yang baik 🤍<br><br>
        Semoga semua hal baik datang ke kamu, satu per satu.
        </div>
    """, unsafe_allow_html=True)

    st.balloons()
