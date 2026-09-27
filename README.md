# Business Survey

Terminal survey for construction companies. It asks the questions in `business_survey_script.py`, saves the answers to a local text file, and can email them.

## Run it

1. Set the email login (optional, only needed to send email):
   ```bash
   export SURVEY_SENDER_EMAIL="you@example.com"
   export SURVEY_SENDER_PASSWORD="your-app-password"   # for Gmail, use an App Password
   # Optional, defaults to Gmail:
   export SURVEY_SMTP_HOST="smtp.gmail.com"
   export SURVEY_SMTP_PORT="587"
   ```
2. Run the survey:
   ```bash
   python3 business_survey_script.py
   ```
3. Answers are always saved to `survey_<company>_<date>_<time>.txt` in the current folder. The file is written before the email step, so a failed email doesn't lose the answers.

Never put the password in the code or commit it to the repo.
