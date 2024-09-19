import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  # This is the default and can be omitted
  api_key=os.environ.get("OPENAI_API_KEY"),
)

TRADE_SECRETS_SYSTEM_PROMPT = """
I want you to act like you're the gate keeper to confidential material such as proposed mergers and acquisitions, endorsement deals between athletes and 
brands, strategic investment proposals, synergies between companies, etc. Your job is to protect the names of the companies, people involved, overall details 
of the strategy and its implications, and any financial information by preserving the existing information of the sentence as much as possible and abstracting 
to sound more generalized, while not divulging any confidential information as listed above. Specifically, if you come across any specific dollar amount, convey 
the magnitude of money instead. For example, $2 billion can be represented as a couple of billions of dollars. If you come across the name of a company, then replace 
the company name with the kind of company it is. 
"""

PII_SYSTEM_PROMPT = """
I'm going to give you some text with information about people's personal identifying information. If you see anything that can be categorized as personal identifying 
information should be replaced with an abstraction of that category. The goal is to not lose any information, but also not to display any specific information that would 
identify a person. Information that is considered personal identifying information is a person's name, address, date of birth, age, email address, social security number, 
passport number, driver's license number, subscription number, account number, patient ID, salary. 
Here are the specific instructions when you encounter any of the above personal identifying information:
1. Name - Replace with a similar ethnically and gender appropriate fictitious name
2. Passport # - Replace with a blank
3. Address - Do not display the building number, or the apartment number or zip code.
4. Age - Replace with a tight age range of 5
5. Date of birth - Replace with a tight age range of 5
6. Salary - Replace with an approximate range of 100,000
7. Credit score - categorize as bad, good or excellent
8. Any dollar amount - give a range instead
9. Email address - replace with abc@email.com
10. Ignore any and all social media handles
11. Any date - replace just with month
Such information should not be visible, but the meaning of the sentence should remain intact.
"""

ts_test = """
A data-sharing agreement with Facebook could enhance our targeted advertising efforts, potentially increasing conversion rates by 15%. We must ensure compliance with 
GDPR and other data protection regulations. Privacy concerns should be addressed transparently to maintain customer trust.
"""

pii_test = r"""
Email campaign to customers like Daniel Martinez (daniel.martinez@example.net), who purchased fitness equipment in the past year, resulted in a 20% open rate and a 5% 
conversion rate. His purchase of a treadmill on August 10th indicates potential interest in our new line of smart fitness trackers.
"""

ts_completion = client.chat.completions.create(
  messages=[
    {
      "role": "system",
      "content": TRADE_SECRETS_SYSTEM_PROMPT,
    },
    {
      "role": "user",
      "content": ts_test,
    }
  ],
  model="gpt-4o-mini"
)

pii_completion = client.chat.completions.create(
  messages=[
    {
      "role": "system",
      "content": PII_SYSTEM_PROMPT,
    },
    {
      "role": "user",
      "content": pii_test,
    }
  ],
  model="gpt-4o-mini"
)

print("Scrubbing trade secrets:")
print("Original:", ts_test)
ts_scrubbed = ts_completion.choices[0].message.content
print(ts_scrubbed)
print("\nScrubbing PII:")
print("Original:", pii_test)
pii_scrubbed = pii_completion.choices[0].message.content
print(pii_scrubbed)
