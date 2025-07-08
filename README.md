## Scrub: Data Redaction for Safe LLM Usage
This repository provides tools and guidelines for analysts to redact personal information (PI) and trade secret data before sharing with public-facing Large Language Models (LLMs). It includes a sample dataset (samples_tradesecrets.csv) and system prompts to guide the redaction process.

## Purpose
The goal is to ensure sensitive data, such as personal information (e.g., names, addresses, SSNs) and trade secrets (e.g., proprietary formulas, client lists), is securely redacted before being processed by public LLMs, mitigating risks of data exposure.
Repository Structure
```
scrub/
├── samples_tradesecrets.csv
├── README.md
└── [other files to be added]
```


samples_tradesecrets.csv: A sample dataset containing mock data with personal information and trade secrets for testing redaction processes.
README.md: This file, providing instructions and system prompts for redaction.

## Prerequisites

* Python 3.x: For processing the CSV file and implementing redaction scripts.
* Text Editor or IDE: To write and test system prompts (e.g., VS Code, PyCharm).
* Access to an LLM: For testing prompts (e.g., Grok, ChatGPT, or other public-facing LLMs).
* Optional: Libraries like pandas for CSV handling or re for regex-based redaction.

Install required Python libraries:
`pip install pandas`

## How to Use
Step 1: Understand the Sample Dataset
The samples_tradesecrets.csv file contains mock data with sensitive information. Example structure:


```
Name,SSN,Address,TradeSecret
John Doe,123-45-6789,"123 Main St, Anytown",FormulaX: 10% Compound
Jane Smith,987-65-4321,"456 Oak Ave, Othercity",ClientList_2025

```


Personal Information (PI): Columns like Name, SSN, and Address.
Trade Secrets: Columns like TradeSecret (e.g., proprietary formulas, client lists).

Step 2: Use System Prompts for Redaction
Below are system prompts designed to guide an LLM to redact sensitive data. These prompts can be used with any public-facing LLM to process text or CSV data.

System Prompt for Redacting Personal Information:
```
You are a data redaction assistant. Your task is to identify and redact personal information (PI) such as names, Social Security Numbers (SSNs), addresses, phone numbers, and email addresses from the provided text or dataset. Replace sensitive data with placeholders (e.g., [REDACTED_NAME], [REDACTED_SSN], [REDACTED_ADDRESS]). Do not modify non-sensitive data. Return the redacted text or dataset in the same format as the input. If processing a CSV, maintain the structure and only redact specified fields.
```
```
Example Input:
Name: John Doe, SSN: 123-45-6789, Address: 123 Main St, Anytown
Example Output:
Name: [REDACTED_NAME], SSN: [REDACTED_SSN], Address: [REDACTED_ADDRESS]

```
System Prompt for Redacting Trade Secrets:
```
You are a data redaction assistant specializing in trade secrets. Your task is to identify and redact trade secret data, such as proprietary formulas, client lists, or confidential business information, from the provided text or dataset. Replace trade secrets with [REDACTED_TRADE_SECRET]. Do not modify non-sensitive data. Return the redacted text or dataset in the same format as the input. If processing a CSV, maintain the structure and only redact specified fields.
```
```
Example Input:
Formula: 10% Compound, Client: Acme Corp
Example Output:
Formula: [REDACTED_TRADE_SECRET], Client: [REDACTED_TRADE_SECRET]

```
Step 3: Process the CSV File

Load the CSV:Use Python with pandas to read samples_tradesecrets.csv:
```python
import pandas as pd
df = pd.read_csv('samples_tradesecrets.csv')
```

Apply Redaction:
Manual Redaction:
```
Use regex or string replacement to redact sensitive fields. Example:importCivil 1
df['Name'] = df['Name'].str.replace(r'.+', '[REDACTED_NAME]')
df['SSN'] = df['SSN'].str.replace(r'.+', '[REDACTED_SSN]')
df['Address'] = df['Address'].str.replace(r'.+', '[REDACTED_ADDRESS]')
df['TradeSecret'] = df['TradeSecret'].str.replace(r'.+', '[REDACTED_TRADE_SECRET]')
```

LLM-Based Redaction: 
```
Send each row or cell content to an LLM with the above prompts to get redacted output. 
Example (pseudo-code):for index, row in df.iterrows():
    df.at[index, 'Name'] = send_to_llm(row['Name'], pi_redaction_prompt)
    df.at[index, 'TradeSecret'] = send_to_llm(row['TradeSecret'], trade_secret_prompt)
```
Save Redacted Data:Save the redacted dataset to a new CSV:
df.to_csv('redacted_samples_tradesecrets.csv', index=False)



Step 4: Test with an LLM

Copy a row or cell from samples_tradesecrets.csv.
Use the system prompts above with a public-facing LLM (e.g., Grok on grok.com or the X app).
Verify that sensitive data is replaced with placeholders (e.g., [REDACTED_NAME], [REDACTED_TRADE_SECRET]).
Ensure the LLM does not store or expose the original data.

Step 5: Verify and Share

Check the redacted CSV to ensure all sensitive data is replaced.
The redacted data is now safe to share with a public-facing LLM for further analysis.

## Best Practices

Test Thoroughly: Always test the redaction process on sample data to ensure no sensitive information leaks.
Automate Redaction: Use scripts to process large datasets efficiently (see example above).
Secure Environment: Run redaction scripts locally or in a secure environment to avoid accidental data exposure.
Log Redactions: Keep a log of what was redacted for auditing purposes (optional).

Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request.

Please include tests and update documentation as needed.
License
This project is licensed under the MIT License. See the LICENSE file for details.
