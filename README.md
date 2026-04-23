# 📧 Email Automation Bot (Python)

## 🚀 Overview

This project is a Python-based email automation tool that sends bulk emails using a CSV file.

It uses Gmail SMTP to send emails automatically, supports HTML email formatting, file attachments, and maintains logs for tracking.

---

## ⚙️ How It Works

1. Reads email addresses from a CSV file
2. Loops through each user
3. Sends a personalized email (Text + HTML)
4. Attaches files (PDF, images, etc.)
5. Logs success and errors with timestamps
6. Waits a few seconds between emails to avoid spam detection

---

## 📂 Project Files

- `main.py` → Main script that runs the email bot
- `config.py` → Stores email credentials
- `emails.csv` → List of recipients
- `logs.txt` → Stores email sending history

---

## 🧠 main.py Explanation

The `main.py` file:

- Opens the CSV file using `csv.DictReader`
- Extracts `email` and `name`
- Sends emails using SMTP
- Supports both plain text and HTML email formats
- Attaches files to emails
- Logs success and error messages with timestamps
- Uses delay (`time.sleep(5)`) to avoid spam blocking

---

## 📌 Example CSV Format

```csv
email,name
test@gmail.com,Ali
test2@gmail.com,Ahmed
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🔐 Setup

1. Enable 2-Step Verification (2FA) on Gmail
2. Generate App Password
3. Add credentials in `config.py`

---

## 🛠️ Technologies Used

- Python
- smtplib
- csv
- email.mime
- datetime

---

## ✨ Features

- ✅ Bulk email sending
- ✅ Personalized emails (name-based)
- ✅ HTML email support (styled emails)
- ✅ File attachments support
- ✅ Logging system with timestamps
- ✅ Delay system to prevent spam blocking

---

## 📄 Logs Example

```text
[20-04-2026 04:30:10 PM][Done] Email sent to test@gmail.com
[20-04-2026 04:30:15 PM][Error] Failed for client@gmail.com: Authentication error
```

---

## 🎨 HTML Email Support

Emails are sent in both:

- Plain text (fallback)
- HTML format (styled with header, content, footer)

---

## 📎 Attachment Support

You can attach files such as:

- PDF (resume, reports)
- Images
- Documents

---

## 🚀 Future Improvements

- Send different attachments per user
- Advanced HTML templates (marketing emails)
- CLI arguments for input/output
- GUI version (Tkinter)
- Email scheduling

---
