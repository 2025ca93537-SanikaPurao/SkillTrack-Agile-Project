# SkillTrack-Agile-Project
Students often have projects, certificates, internships, and achievements scattered across multiple platforms. SkillTrack will provide a centralized portfolio platform where students can showcase their skills and projects professionally.


## Agile Project - Sprint 1 MVP

SkillTrack is a web-based portfolio management platform that enables students to create and manage their professional profile, technical skills, and academic/personal projects in one place.

---

#  Problem Statement

Students usually maintain their skills, projects, GitHub links, and professional information across multiple platforms, making it difficult to present a unified professional profile.

SkillTrack solves this by providing a centralized portfolio management system.

---

# Sprint 1 Goal

Develop a Minimum Viable Product (MVP) that allows users to:

- Register
- Login
- Manage Profile
- Manage Skills
- Manage Projects
- View Dashboard

---

# Features

## Authentication

- User Registration
- User Login
- Secure Password Hashing
- Session Management
- Logout

---

## Dashboard Module

- Welcome User
- Profile Status
- Total Skills
- Total Projects
- Recent Projects

---

## Profile Module

- Full Name
- Phone
- College
- Degree
- Graduation Year
- LinkedIn
- GitHub
- About Me

---

## Skills Module

- Add Skills
- Delete Skills
- View Skills

---

## Projects Module

- Add Project
- Delete Project
- View Projects
- GitHub Link
- Demo Link

---

# Technology Stack Used

| Layer | Technology |
|---------|------------|
| Frontend | HTML5 |
| Styling | Bootstrap 5 |
| Backend | Python Flask |
| ORM | SQLAlchemy |
| Database | MySQL (XAMPP) |
| Authentication | Flask Login |
| Security | Werkzeug Password Hashing |

---

# Project Architecture

Browser

↓

Flask

↓

Routes (Blueprints)

↓

Models (SQLAlchemy)

↓

MySQL

↓

HTML Templates

---

# Project Structure

SkillTrack

app.py

config.py

models/

routes/

templates/

static/

README.md

---

# Database Tables

Users

Profiles

Skills

Projects


# Installation

Clone Repository

git clone <repository-url>

Install Packages

pip install -r requirements.txt

Run Application

python app.py


# Future Enhancements ( Sprint 2)

Feedback module
Ratings module
Analytics Dashboard
Resume Builder
AI Skill Recommendation
Certificate Upload
Resume Download
Job Recommendation
Admin Portal
Email Notifications
Dark Mode
Mobile Application

---

#  Sprint Status

Sprint 1

Status: Completed 

