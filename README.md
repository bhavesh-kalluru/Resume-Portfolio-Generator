# 🚀 AI Resume → Interactive Portfolio Generator

Turn your resume into a beautifully animated online portfolio — in seconds.  
Built with Python, Flask, and custom NLP, this app extracts every detail from your resume (PDF/DOCX) and renders it in a professional, responsive web layout.

---

## 🧠 Why I Built This

As an AI/GenAI engineer passionate about building tools that *automate tedious tasks*, I created this project to showcase how NLP + UI design can empower job seekers.  
Instead of manually building personal websites, you can now upload your resume and *instantly* generate a portfolio that reflects your skills, experience, and projects.

---

## 🎨 Key Features

- ✅ **Upload your resume** (.pdf or .docx) → auto-converts to portfolio
- 🎯 **Full NLP Parsing**: Extracts name, email, phone, skills, experience, education, projects, LinkedIn & GitHub
- 🌗 **Dark/Light Mode** toggle (saved in localStorage)
- 🔄 **Rotating Templates**: Three unique, animated HTML templates
- 🔒 **Only resumes allowed** (No cover letters or other docs)
- ⚡ **Instant deployment-ready** Flask web app

---

## 🛠 Tech Stack

| Backend  | Frontend | NLP Parsing | Extras |
|----------|----------|-------------|--------|
| Python   | HTML5/CSS3 | Custom Regex / spaCy-ready | Responsive design |
| Flask    | Jinja2 Templates | OpenAI (optional) | Animations |
|          | JavaScript |              | Dark Mode |

---

## 📁 Project Structure

/app.py
/utils/parser.py
/templates/
├── template1.html
├── template2.html
└── template3.html
/static/
└── css/style.css
/uploads/ # Temp resume storage

## 🧪 How to Use

1. Clone the repo  
   `git clone https://github.com/your-username/resume-portfolio-generator.git`
2. Install dependencies  
   `pip install -r requirements.txt`
3. Run the app  
   `python app.py`
4. Visit `http://localhost:5000`, upload your resume, and boom 💥 — portfolio generated!

---

## 🔮 Future Ideas

- PDF export of portfolio
- User login + saved portfolio history
- Integration with LinkedIn or Notion
- Support for custom portfolio themes

---

## 🙋‍♂️ About Me

Hi, I’m **Bhavesh**, an AI/GenAI engineer and Python developer building real-world tools powered by AI.  
This is one of my flagship portfolio projects showcasing:
- Practical NLP application
- Clean frontend design
- Full-stack implementation
- UX-focused development

Let’s connect on LinkedIn: https://www.linkedin.com/in/bhaveshkalluru/  
GitHub: https://github.com/bhavesh-kalluru

---

## 🌟 If you found this useful:
Give it a ⭐ on GitHub, or fork it to build your own version!
