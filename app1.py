import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Mahindra University School of Management",
    page_icon="🎓",
    layout="wide"
)

# Hero Section
st.title("🎓 Mahindra University")
st.subheader("School of Management")

st.markdown("""
### Shaping Future Leaders

Welcome to the School of Management at Mahindra University.

Our programs are designed to develop innovative, ethical, and globally minded leaders
equipped to navigate the challenges of a rapidly evolving business landscape.
""")

# Call-to-Action Buttons
col1, col2, col3 = st.columns(3)

with col1:
    st.button("Explore Programs")

with col2:
    st.button("Admissions")

with col3:
    st.button("Contact Us")

st.divider()

# Highlights Section
st.header("Why Choose Us?")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Faculty", "50+")
    st.write("Experienced academicians and industry experts.")

with col2:
    st.metric("Industry Partners", "100+")
    st.write("Strong corporate collaborations and internships.")

with col3:
    st.metric("Placement Support", "95%+")
    st.write("Career development and placement assistance.")

st.divider()

# Programs
st.header("Programs Offered")

st.markdown("""
- MBA
- BBA
- Executive Education Programs
- Industry Certification Courses
- Research & Innovation Initiatives
""")

st.divider()

# Footer
st.markdown("""
---
**Mahindra University School of Management**  
Empowering students to become leaders, innovators, and entrepreneurs.

📍 Hyderabad, India  
🌐 www.mahindrauniversity.edu.in

Run it with:

```bash
pip install streamlit
streamlit run app.py
```

# This creates a clean university-style landing page with a hero section, program highlights, metrics, and call-to-action buttons.
