# 🎬 **TMDB Top-Rated Movies Scraper**

This Python project fetches data from **The Movie Database (TMDB)** API and extracts the top-rated movies across **471 pages**, replaces `genre_ids` with actual **genre names**, and stores the results in a clean CSV format for further analysis.

---

## 📌 **Features**

- Scrapes all **top-rated movies** from TMDB (up to 471 pages).
- Uses the official **TMDB API**.
- Converts `genre_ids` to **human-readable genre names**.
- Filters out unwanted fields for a clean dataset.
- Exports results as a **CSV file**.

---

<div style="text-align: center;">
    <img src="Banner_img.png" alt="Project Banner" style="width: 100%; max-width: 350px; height:400px; border-radius: 10px;"/>
</div>

## 🧰 **Tech Stack**

- Python 3.7+
- `aiohttp`
- `pandas`
- `tqdm` (optional, for progress bar)

---

## 📥 **Installation**

1. ### **Clone the repo**
   ```bash
   git clone https://github.com/Yousfshah/Top_Rated_Movies_Data.git
   ```
   
   ```bash
   cd top_rated_movies_data
   ```

2. ### **Install dependencies**
   - Make sure you have uv installed.
  ```bash
   uv init
  ```
  ```bash
   uv install pandas tqdm aiohttp
  ```
3. ### 🚀 **How to Run**
```bash
python main.py
```
- The script will fetch all pages and save a file named tmdb_top_rated_filtered.csv in the current directory.

### 🔐 **API Key**
- This project uses a public demo API key:
```bash
  8265bd1679663a7ea12ac168da84d2e8
```
- For production use, <a href="https://www.themoviedb.org/settings/api" target="_blank">Register For Your Own TMDB API Key</a>



### 🙌 **Acknowledgements**
- Data from TMDB
- Genre mappings from TMDB official documentation

###  **Connect with me on**
<div style="max-width: 42rem; margin: 2.5rem auto; padding: 2rem; text-align: center; background: linear-gradient(135deg, #8d8d8dff, #9c9b9bff); box-shadow: 0 0.5rem 1.25rem rgba(0, 0, 0, 0.15); font-family: 'Lato', Arial, sans-serif; border: 5px solid black; border-radius: 0.75rem;">

  <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 1.25rem;">

<a href="https://www.linkedin.com/in/yousuf-shah-7ba9492b4/" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0a66c2?style=for-the-badge&logo=linkedin&logoColor=white"
        alt="LinkedIn"
        style="height: 3.3rem; padding: 0.3rem; background: #000; transition: transform 0.3s;"
        onmouseover="this.style.transform='scale(1.07)'" 
        onmouseout="this.style.transform='scale(1)'">
</a>

<a href="https://yousfshah.github.io/Portfolio_Website/" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/Portfolio-Visit-ffb300?style=for-the-badge&logo=firefox&logoColor=white"
        alt="Portfolio"
        style="height: 3.3rem; padding: 0.3rem; background: #000; transition: transform 0.3s;"
        onmouseover="this.style.transform='scale(1.07)'" 
        onmouseout="this.style.transform='scale(1)'">
</a>

<a href="https://github.com/Yousfshah" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/GitHub-Explore-6f42c1?style=for-the-badge&logo=github&logoColor=white"
        alt="GitHub"
        style="height: 3.3rem; padding: 0.3rem; background: #000; transition: transform 0.3s;"
        onmouseover="this.style.transform='scale(1.07)'" 
        onmouseout="this.style.transform='scale(1)'">
</a>

<a href="https://www.kaggle.com/yousufshah" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/Kaggle-Profile-0097b2?style=for-the-badge&logo=kaggle&logoColor=white"
        alt="Kaggle"
        style="height: 3.3rem; padding: 0.3rem; background: #000; transition: transform 0.3s;"
        onmouseover="this.style.transform='scale(1.07)'" 
        onmouseout="this.style.transform='scale(1)'">
</a>

<a href="https://yousfshah.github.io/Blogging/" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/Blog-Articles-f44336?style=for-the-badge&logo=blogger&logoColor=white"
        alt="Blog"
        style="height: 3.3rem; padding: 0.3rem; background: #000; transition: transform 0.3s;"
        onmouseover="this.style.transform='scale(1.07)'" 
        onmouseout="this.style.transform='scale(1)'">
</a>

<a href="https://x.com/YousufAnalyst" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/Twitter-Follow-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white"
        alt="Twitter"
        style="height: 3.3rem; padding: 0.3rem; background: linear-gradient(to right, #000, #000); transition: transform 0.3s;"
        onmouseover="this.style.transform='scale(1.07)'" 
        onmouseout="this.style.transform='scale(1)'">
</a>

  </div>
</div>



