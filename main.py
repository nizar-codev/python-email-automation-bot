import smtplib
import csv
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL, APP_PASSWORD, SMTP_SERVER, SMTP_PORT
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

def send_email(receiver_email, name):
    try:
        # Create message
        msg = MIMEMultipart("mixed")
        msg["From"] = EMAIL
        msg["To"] = receiver_email
        msg["Subject"] = "Email With Attachment"

        
        # Alternative part (text + html)
        alt_part = MIMEMultipart("alternative")

        # Plain version (fallback)
        text_body = f"Hello {name}, Please find the attached file."

        html_body = f"""
<html>
  <body style="margin:0; padding:0; background-color:#f4f4f4;">

    <div style="max-width:600px; margin:auto; background:white; padding:20px;">

      <!-- Header -->
      <div style="background-color:#4CAF50; color:white; padding:15px; text-align:center;">
        <h2 style="margin:0;">📧 Email Automation Bot</h2>
      </div>

      <!-- Content -->
      <div style="padding:20px;">
        <h3>Hello {name},</h3>
        
        <p>Please find the attached file.</p>

        <p style="color:blue;">
          This email was sent using a Python automation script.
        </p>
      </div>

      <!-- Footer -->
      <div style="background-color:#eeeeee; padding:10px; text-align:center; font-size:12px;">
        <p style="margin:0;">© 2026 Nizar | All rights reserved</p>
      </div>

    </div>

  </body>
</html>
"""


        alt_part.attach(MIMEText(text_body, "plain"))
        alt_part.attach(MIMEText(html_body, "html"))

       # Attach alternative part to main msg
        msg.attach(alt_part)

        #Attachment
        filename = "resume.pdf"
        with open(filename,"rb") as attachment:
            part = MIMEBase("application","octet-stream")
            part.set_payload(attachment.read())
         
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={filename}",
        )
        
        msg.attach(part)

        # Send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL, APP_PASSWORD)

        server.send_message(msg)
        server.quit()

        time_now = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

        #print(f"[Done] Email sent to {receiver_email}")

         # ✅ LOG SUCCESS
        with open("logs.txt", "a") as log:
            log.write(f"[{time_now}][Done] Email sent to {receiver_email}\n")

        print(f"[Done] Email sent to {receiver_email}")

    except Exception as e:
        # ❌ LOG ERROR
        time_now = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
        with open("logs.txt", "a") as log:
            log.write(f"[Error] Failed for {receiver_email}: {e}\n")
        print(f"[{time_now}][Error] Failed to send to {receiver_email}: {e}")


def main():
    # ✅ CLEAR LOG FILE FIRST
    open("logs.txt", "w").close()

    with open("emails.csv", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            email = row["email"]
            name = row["name"]

            send_email(email, name)

            # Delay to avoid spam block
            time.sleep(5)


if __name__ == "__main__":
    main()