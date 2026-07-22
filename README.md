# Movie Multi-Model Recommendation System


A Flask-based Movie Recommendation System using multiple Machine Learning recommendation techniques including popularity-based and content-based filtering.

The application provides a modern dark and white themed dashboard where users can discover Movies oks based on popularity, Movies similarity, or user preferences.

---

#  Features

- 📈 Popularity-Based Recommendation
-  Content-Based Recommendation
- 👥 Collaborative Filtering Recommendation
- 🌙 Modern Dark and White UI
- 📱 Responsive Design
- ⚡ Fast Recommendation using Pickle Models
- 🎨 Attractive Movie Cards with Cover Images

---

# 🛠️ Technologies Used

## Frontend

- HTML5
- CSS3
- JavaScript
- Bootstrap 5

## Backend

- Python
- Flask

## Machine Learning

- Pandas
- NumPy
- Scikit-learn
- Cosine Similarity
- Pickle

---

# 📂 Project Structure

```
Movie-Multi-Model-Recommendation-System/
│
├── app.py
├── requirements.txt
├── extra.py
├── README.md
│
├── models/
│   ├── Movies.pkl
│   ├── poster.pkl
│   ├── final_movies.pkl
│   └── similarity_scores.pkl
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── images/
│
└── templates/
    ├── index.html
    ├── base.html
    └── recommender.html
    
    
```

---
# Dashbord

- Dark mode
<img width="1340" height="622" alt="Screenshot 2026-07-10 153831" src="https://github.com/user-attachments/assets/190dd035-1b92-45ea-a387-d08fd7121a05" />

- Light Mode

<img width="1344" height="625" alt="Screenshot 2026-07-10 153900" src="https://github.com/user-attachments/assets/8c105f64-3e1e-4fd4-8e13-dcf6727529b8" />


# 01 Popularity Recommendation
  
https://github.com/user-attachments/assets/50b9febe-089d-4ce4-bfeb-a188cb90ec27

# 02 Content Based Recommendation

<img width="967" height="618" alt="Screenshot 2026-07-10 154339" src="https://github.com/user-attachments/assets/1a05af1a-a31d-4fcd-b0d1-5a78ffdb64f4" />

<img width="1340" height="620" alt="Screenshot 2026-07-10 154858" src="https://github.com/user-attachments/assets/67b50161-d987-451b-8d6a-fd61f6f7c9bd" />

---- 

---
# 📦 Required Python Libraries

Install all required packages using:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install flask
pip install pandas
pip install numpy
```

---

# 📁 Model Files

Create a folder named **models** and place the following files inside it.

| File Name | Description |
|------------|-------------|
| Movies.pkl | Movies information dataset |
| popular.pkl | Popular Movies dataset |
| final_movies.pkl | final_movies stores |
| similarity_scores.pkl | Cosine Similarity Matrix |

Folder structure:

```
models/
   ├── Movies.pkl
   ├── poster.pkl
   ├── final_movies.pkl
   └── similarity_scores.pkl
```

---

# ▶️ How to Run the Project

### Step 1

Clone the repository.

```bash
git clone <repository-link>
```

### Step 2

Go to the project folder.

### Step 3

Create a virtual environment (Optional).

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

### Step 4

Install dependencies.

```bash
pip install -r requirements.txt
```

### Step 5

Place all pickle model files inside the **models** folder.

### Step 6

Run the Flask application.

```bash
python app.py
```

### Step 7

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# Recommendation Techniques

## 1. Popularity-Based Recommendation

This method recommends Moives that are popular among all users.

It uses:

- Popular Movies
- Recommendation Movies

These Movies are recommended to every user regardless of their reading history.

---

## 2. Content-Based Recommendation

This method recommends Movies that are similar to the selected Movie.

It compares:

- Movies Title
- Poster img
- Vote average
- popularity
 
Cosine Similarity is used to find similar Movies.

---

## 3. Collaborative Filtering Recommendation

This method recommends Movies based on user behavior.

It works by finding users with similar looking preferences and recommending Movies they have liked.

It uses:

- Cosine Similarity Matrix

---

# 🖥️ Application Workflow

```
User

   ↓

Choose Recommendation Method

   ↓

Enter Movie Name (if required)

   ↓

Flask Backend

   ↓

Load Pickle Models

   ↓

Generate Recommendations

   ↓

Display Recommended Movies
```

---

# 🎨 User Interface

The application includes:

- Dark Theme Dashboard
- White Theme Dashboard
- Gold Accent Design
- Responsive Layout
- Interactive Movie Cards
- Movie Cover Images
- Smooth Animations
- Clean Navigation

---

# 📸 Screens

- Home Page
- Popular Movies
- Content-Based Recommendation
- Collaborative Recommendation
- Recommendation Results

---

# 📊 Machine Learning Models

The project uses pre-trained models stored as Pickle files.

These include:

- Popular Movies DataFrame
- Movies DataFrame
- Similarity Matrix

No model training is required while running the application.

---

# 🚀 Future Improvements

- Reading History
- Movies Search
- Genre-Based Recommendation
- Hybrid Recommendation System
- Rating Prediction
- Favorite Movies
- Database Integration
- Admin Dashboard
- Deploy on Cloud

---

# 👨‍💻 Author

**Gautam Purohit**

B.Sc. (CA & IT)

Machine Learning & Python Developer

----

GitHub : https://github.com//gautam-purohit2006/

Linkedin : https://www.linkedin.com/in/gautam-purohit-618383315/

----

# 📄 License

This project is created for learning and educational purposes.

Feel free to use and modify it for your own projects.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
