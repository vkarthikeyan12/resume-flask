# 📄 Resume Flask App  

A simple **Flask web app** to showcase my resume online. The site serves:  
- A **resume web page** built with HTML, CSS, and Bootstrap.  
- A **downloadable PDF** version of my resume.  
- Optional **profile photo** displayed on the left side.  

Deployed on **Render** with optional support for a **custom domain**.  

---

## 🚀 Features
- 📑 Resume displayed in a clean, responsive layout  
- 🖼 Profile photo (served from `static/profile.jpg`)  
- 📥 PDF download button (`/download` route)  
- 🎨 Custom styling with Bootstrap + CSS  
- 🌍 Deployable on **Render**, **Railway**, or **PythonAnywhere**  
- 🔒 HTTPS enabled automatically (via Render / Let’s Encrypt)  

---

## 📂 Project Structure
```
resume-flask-app/
│── app.py                # Flask application
│── requirements.txt      # Dependencies
│── Procfile              # For deployment (Gunicorn command)
│── resume.pdf            # Resume file for download
│
├── static/               # Static assets (CSS, images)
│   ├── style.css
│   └── profile.jpg
│
└── templates/            # HTML templates
    └── resume.html
```

---

## ⚙️ Installation (Local)

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/resume-flask-app.git
   cd resume-flask-app
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Mac/Linux
   venv\Scripts\activate         # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run Flask app:
   ```bash
   python app.py
   ```

5. Open in browser:
   ```
   http://127.0.0.1:5000
   ```

---

## 🌐 Deployment (Render)

1. Push project to GitHub.  
2. On [Render](https://render.com):
   - Create a **Web Service** (not Static Site).  
   - Connect repo.  
   - Build Command:
     ```
     pip install -r requirements.txt
     ```
   - Start Command:
     ```
     gunicorn app:app
     ```
3. Render deploys automatically → You get a live link:
   ```
   https://your-app-name.onrender.com
   ```

---

## 🔗 Custom Domain (Optional)
1. Buy a domain (Namecheap, Google Domains, GoDaddy).  
2. In Render → **Settings → Custom Domains** → Add your domain.  
3. Update DNS records at your registrar (CNAME or A records provided by Render).  
4. Wait for propagation → Your app will be live at:
   ```
   https://yourdomain.com
   ```

---

## 📸 Example Screenshot
(Add a screenshot of your site here, e.g. `/static/screenshot.png`)

---

## 🛠 Tech Stack
- **Python 3**  
- **Flask**  
- **Gunicorn** (production server)  
- **Bootstrap 5** (styling)  

---

## 📬 Contact
**Karthikeyan Venkatesan**  
- 📧 [kar120997@gmail.com](mailto:kar120997@gmail.com)  
- 🔗 [LinkedIn](https://www.linkedin.com/in/karthikeya-n-venkatesan/)  
- 💻 [GitHub](https://github.com/vkarthikeyan12)  
