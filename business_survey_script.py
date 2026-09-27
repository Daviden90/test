# Business-Survey
# Python script to run a construction company survey and email the results

import os
import re
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to display survey header
def display_header():
    print("\n############################################")
    print("#   Construction Company Success Survey   #")
    print("############################################")
    print("\nPlease enter the name of your company below:")
    company_name = input("Company Name: ").strip()
    print(f"\nThank you, {company_name}! Please answer the {len(survey_questions)} questions below.")
    print("\nFor each question, where applicable, provide a score from 1 (Very Poor) to 10 (Excellent).")
    return company_name

# List of tailored survey questions
survey_questions = [
    "What is the mission statement of your company?",
    "What is the vision statement of your company?",
    "How does your company ensure alignment with core values?",
    "Do you have a documented training program for employees?",
    "How do you onboard new team members?",
    "How often do you conduct performance reviews? (1-10 scale)",
    "What is your process for ensuring client satisfaction?",
    "Do you track key performance indicators (KPIs) regularly? (1-10 scale)",
    "What is your process for documenting systems and procedures?",
    "How often do you refresh and review your processes?",
    "What is your marketing strategy to attract new clients?",
    "How do you handle client feedback or complaints? (1-10 scale)",
    "What strategies do you use for team development?",
    "Do you have a budget for professional development and training? (1-10 scale)",
    "What systems do you use to manage project timelines?",
    "How do you handle unexpected delays in projects?",
    "What financial tools do you use for budget tracking?",
    "How do you allocate resources across multiple projects? (1-10 scale)",
    "What is your approach to sustainability in construction projects?",
    "Do you have a disaster recovery or risk mitigation plan?",
    "What percentage of your projects involve subcontractors?",
    "How do you ensure quality control in your construction projects? (1-10 scale)",
    "What technology tools do you use to improve efficiency?",
    "How do you identify and nurture potential leaders within your team? (1-10 scale)",
    "Do you have performance-based incentives for your team?",
    "What is your company’s annual revenue growth goal?",
    "How do you track and report on financial performance?",
    "What is your process for identifying and addressing weaknesses in the business?",
    "How do you monitor market trends and incorporate them into strategy?",
    "What is your approach to client retention? (1-10 scale)",
    "Do you have a structured sales process?",
    "What role does social media play in your marketing efforts?",
    "What challenges do you face with supply chain disruptions?",
    "What is your strategy for capturing and analyzing market opportunities?",
    "How do you measure the effectiveness of your marketing campaigns? (1-10 scale)",
    "What steps do you take to maintain financial alignment with your team goals?",
    "What steps have you taken to ensure operational effectiveness?",
    "What are your methods for peer-to-peer benchmarking?",
    "How does your company contribute to the local community?",
    "What innovations have you recently implemented in your business?",
    "What is your long-term vision for the growth of your business?"
]

# Function to display survey questions
def display_survey():
    responses = []
    for i, question in enumerate(survey_questions, start=1):
        print(f"{i}. {question}")
        response = input("Your Answer: ")
        responses.append(f"{i}. {question}\nAnswer: {response}\n")
    return responses

# Function to save survey results to a local text file so answers are never lost
def save_responses(company_name, responses):
    safe_name = re.sub(r"[^A-Za-z0-9_-]+", "_", company_name).strip("_") or "company"
    filename = f"survey_{safe_name}_{datetime.now():%Y%m%d_%H%M%S}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Company: {company_name}\n\n")
        f.write("\n".join(responses))
    print(f"\nSurvey results saved to {filename}")
    return filename

# Function to send survey results via email
def send_email(company_name, responses, recipient_email):
    # Credentials come from environment variables so they are never stored in the code
    sender_email = os.environ.get("SURVEY_SENDER_EMAIL")
    sender_password = os.environ.get("SURVEY_SENDER_PASSWORD")
    smtp_host = os.environ.get("SURVEY_SMTP_HOST", "smtp.gmail.com")
    smtp_port = int(os.environ.get("SURVEY_SMTP_PORT", "587"))

    if not sender_email or not sender_password:
        print("Email not sent: set SURVEY_SENDER_EMAIL and SURVEY_SENDER_PASSWORD first.")
        return False

    # Email content
    subject = f"Completed Construction Company Survey - {company_name}"
    body = f"Company: {company_name}\n\n" + "\n".join(responses)

    # Create email message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Send email
    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Survey results sent successfully!")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

if __name__ == "__main__":
    # Display the survey header and questions
    company = display_header()
    answers = display_survey()

    # Save a local copy first, then collect recipient email and send survey results
    save_responses(company, answers)
    print("\nPlease enter the recipient's email to send the survey results:")
    recipient = input("Recipient Email: ").strip()
    if recipient:
        send_email(company, answers, recipient)
    else:
        print("No recipient entered; email skipped.")
