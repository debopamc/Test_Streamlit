import streamlit as st

st.title("Hello, World!")
st.write("Welcome to Mahindra University!")
`Run it with:

```bash
pip install streamlit
streamlit run app.py
```

This will open a web page displaying:

* **Hello, World!**
* **Welcome to Mahindra University!**

A slightly nicer version:

```python
import streamlit as st

st.set_page_config(page_title="Mahindra University", page_icon="🎓")

st.title("🎓 Hello, World!")
st.subheader("Mahindra University")
st.write("Welcome to your first Streamlit application!")

name = st.text_input("Enter your name")

if name:
    st.success(f"Hello, {name}! Welcome to Mahindra University.")
