# Frame-Work-py

# CORD-19 Metadata Explorer

A simple data exploration and visualization project using the CORD-19 `metadata.csv` dataset.  
Built with **Python**, **Pandas**, **Matplotlib**, **Seaborn**, **WordCloud**, and **Streamlit**.

---

## 📂 Project Structure
```

Frame-Work-py/
│-- app.py               # Streamlit application
│-- metadata.csv         # Original dataset (ignored in Git)
│-- metadata_cleaned.csv # Cleaned dataset (ignored in Git)
│-- .gitignore           # Ignore rules
│-- requirements.txt     # Dependencies

````

---

## ⚡ Features
- Load and clean the CORD-19 metadata.
- Explore missing values and data structure.
- Visualizations:
  - Publications by year
  - Top journals
  - Word cloud of paper titles
  - Distribution by source
- Interactive **Streamlit web app**.

---

## 🛠 Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/waziri-cod/cord19-explorer.git
   cd cord19-explorer
````

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   source .venv/bin/activate # Mac/Linux
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

Run the Streamlit app:

```bash
python -m streamlit run app.py
```

Then open your browser at `http://localhost:8501`.

---

## 📊 Example Visualizations

* Publications by year
* Word cloud of titles
* Top journals
* Data source distribution

---

## 📜 License

This project is open-source and available under the MIT License.

```

---

👉 Do you want me to also generate a **`requirements.txt`** file with your exact dependencies (so you don’t have to install each manually)?
```
