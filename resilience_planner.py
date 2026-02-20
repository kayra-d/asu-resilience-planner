import streamlit as st
import pandas as pd
import plotly.express as px
import datetime

# Sayfa Ayarları
st.set_page_config(page_title="Resilience Growth Modeler", layout="wide")

# Sidebar: Kullanıcı Tanımlama
st.sidebar.header("🎯 Set Your Goals")
user_name = st.sidebar.text_input("Student Name", "Guest User")
start_score = st.sidebar.slider("Starting Performance (%)", 0, 100, 50)
target_score = st.sidebar.slider("Target Performance (%)", 0, 100, 90)

st.sidebar.markdown("---")
st.sidebar.info(f"""
**The Kayra Method:**
This tool is inspired by Kayra's academic turnaround from 53% to 90%. 
It uses data to bridge the gap between potential and performance.
""")

# Ana Başlık
st.title(f"🧠 {user_name}'s Resilience Growth Modeler")
st.subheader("Transform your academic discipline with data-driven tracking.")

# Veri Giriş Bölümü
col1, col2 = st.columns(2)

with col1:
    st.write("### 📝 Daily Log")
    study_hours = st.number_input("Hours Studied Today", 0.0, 16.0, 4.0)
    focus_level = st.select_slider("Focus Intensity", options=["Very Low", "Low", "Medium", "High", "Peak"])
    distractions = st.multiselect("Main Distractions", ["Social Media", "Gaming", "Noise", "Procrastination", "Stress"])

with col2:
    st.write("### 📊 Performance Logic")
    # Basit bir puanlama algoritması
    focus_map = {"Very Low": 1, "Low": 2, "Medium": 3, "High": 4, "Peak": 5}
    score = (study_hours * focus_map[focus_level]) - (len(distractions) * 1.5)
    
    # Skor normalizasyonu
    final_day_score = min(max(start_score + score, 0), 100)
    
    st.metric("Estimated Daily Performance Index", f"{final_day_score:.1f}%")
    if final_day_score >= target_score:
        st.success("🔥 High Performance! You are meeting your target pace.")
    else:
        st.warning("📉 Keep going! Focus more to reach your target curve.")

# Grafik Bölümü
st.markdown("---")
st.write("### 📈 Your Growth Roadmap")

# Örnek veri seti (Kullanıcının başlangıç ve hedefine göre dinamik)
months = ["Month 1", "Month 2", "Month 3", "Month 4", "Month 5"]
# Başlangıçtan hedefe lineer bir artış simülasyonu
performance_curve = [start_score, 
                     start_score + (target_score-start_score)*0.3, 
                     start_score + (target_score-start_score)*0.6, 
                     start_score + (target_score-start_score)*0.8, 
                     target_score]

df = pd.DataFrame({"Timeline": months, "Performance Index (%)": performance_curve})
fig = px.line(df, x="Timeline", y="Performance Index (%)", 
              title=f"Path to {target_score}% Discipline",
              markers=True, range_y=[0, 100])

st.plotly_chart(fig, use_container_width=True)