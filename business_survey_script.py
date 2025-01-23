
# Business-Survey
# Python script to generate 40 construction company survey questions with email functionality

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to display survey header
def display_header():
    print("\n############################################")
    print("#   Construction Company Success Survey   #")
    print("############################################")
    print("\nPlease enter the name of your company below:")
    company_name = input("Company Name: ")
    print(f"\nThank you, {company_name}! Please answer the questions below.")
    print("\nFor each question, where applicable, provide a score from 1 (Very Poor) to 10 (Excellent).")

# List of 40 tailored questions
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

# Function to send survey results via email
def send_email(responses, recipient_email):
    sender_email = "your_email@example.com"  # Replace with your email
    sender_password = "your_password"  # Replace with your email password

    # Email content
    subject = "Completed Construction Company Survey"
    body = "\n".join(responses)

    # Create email message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Send email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Survey results sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    # Display the survey header and questions
    display_header()
    answers = display_survey()

    # Collect recipient email and send survey results
    print("\nPlease enter the recipient's email to send the survey results:")
    recipient = input("Recipient Email: ")
    send_email(answers, recipient)
