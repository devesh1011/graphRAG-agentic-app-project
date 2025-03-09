import pandas as pd
import numpy as np
import random
import string
from datetime import datetime, timedelta

# Set random seeds for reproducibility
random.seed(42)
np.random.seed(42)

# Function to generate a unique hash-like transaction ID
def generate_transaction_id(existing_ids):
    while True:
        suffix = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
        txn_id = f"TXN-{suffix}"
        if txn_id not in existing_ids:
            return txn_id

# Step 1: Generate 1000 unique 9-digit account numbers
account_numbers = random.sample(range(1000000, 999999999), 1000)
account_numbers = [f"{num:09d}" for num in account_numbers]

# Assign ages and determine elderly status based on age threshold
ages = []
is_elderly = []
elderly_threshold = 60  # Define elderly as age >= 65
for i, acc in enumerate(account_numbers):
    if i < 200:  # Elderly users (first 200 accounts)
        age = random.randint(65, 90)
    elif i < 900:  # Non-elderly legitimate users (next 700 accounts)
        age = random.randint(18, 64)  # Still includes 60-64, but we'll adjust is_elderly later
    else:  # Fraud ring members (last 100 accounts)
        age = random.randint(20, 50)
    ages.append(age)
    is_elderly.append(1 if age >= elderly_threshold else 0)  # Set based on age

# Create users DataFrame and add gender
users = pd.DataFrame({"account": account_numbers, "age": ages, "is_elderly": is_elderly})
users["gender"] = np.random.choice(["Male", "Female"], size=1000, p=[0.49, 0.51])

# Create lookup dictionaries
account_to_age = users.set_index("account")["age"].to_dict()
account_to_is_elderly = users.set_index("account")["is_elderly"].to_dict()
account_to_gender = users.set_index("account")["gender"].to_dict()

# Step 2: Generate target lists for fraud rings
elderly_accounts = [acc for acc, elderly in account_to_is_elderly.items() if elderly == 1]
fraud_accounts = account_numbers[900:]  # Last 100 are fraud ring members
target_lists = {}
for ring in range(1, 11):  # 10 fraud rings
    target_lists[ring] = random.sample(elderly_accounts, min(20, len(elderly_accounts)))

# Step 3: Define fraud types and methods for rings
fraud_types = ["Tech Support Scam", "Investment Fraud", "Romance Scam", "Government Impersonation", "Other"]
methods = ["Phone", "Email", "Social Media", "In-Person", "Other"]
ring_to_fraud_type = {ring: fraud_types[(ring - 1) % 5] for ring in range(1, 11)}
ring_to_method = {ring: methods[(ring - 1) % 5] for ring in range(1, 11)}

# Step 4: Generate transactions
transactions = []
existing_ids = set()
start_date = datetime(2023, 1, 1)

# Step 4.1: Generate 2300 fraudulent transactions
fraud_count = 0
while fraud_count < 2300:
    ring_number = random.randint(1, 10)
    sender = random.choice(target_lists[ring_number])
    receiver_start_idx = 900 + (ring_number - 1) * 10
    receiver = account_numbers[receiver_start_idx + random.randint(0, 9)]

    amount = round(np.random.lognormal(mean=5, sigma=1), 2)
    date = (start_date + timedelta(days=random.randint(0, 364))).strftime("%Y-%m-%d")

    transaction_id = generate_transaction_id(existing_ids)
    existing_ids.add(transaction_id)

    sender_age = account_to_age[sender]
    sender_is_elderly = account_to_is_elderly[sender]
    receiver_age = account_to_age[receiver]
    receiver_is_elderly = account_to_is_elderly[receiver]
    sender_gender = account_to_gender[sender]
    receiver_gender = account_to_gender[receiver]
    type_of_fraud = ring_to_fraud_type[ring_number]
    method_of_contact = ring_to_method[ring_number]
    loss = amount
    time_of_day = np.random.choice(["Morning", "Afternoon", "Evening", "Night"], p=[0.25, 0.3, 0.3, 0.15])
    resolution_status = np.random.choice(["Unreported", "Reported", "Under Investigation", "Resolved"], p=[0.5, 0.3, 0.15, 0.05])

    transactions.append([
        transaction_id, sender, sender_age, sender_is_elderly, receiver, receiver_age, receiver_is_elderly,
        amount, date, 1, sender_gender, receiver_gender, type_of_fraud, method_of_contact, loss, time_of_day, resolution_status
    ])
    fraud_count += 1

# Step 4.2: Generate 7700 legitimate transactions
legit_count = 0
while legit_count < 7700:
    sender = random.choice(account_numbers)
    receiver = random.choice([acc for acc in account_numbers if acc != sender])
    if account_to_is_elderly[sender] == 1 and receiver in fraud_accounts:
        ring_number = (account_numbers.index(receiver) - 900) // 10 + 1
        if sender in target_lists[ring_number]:
            continue

    amount = round(np.random.lognormal(mean=5, sigma=1), 2)
    date = (start_date + timedelta(days=random.randint(0, 364))).strftime("%Y-%m-%d")

    transaction_id = generate_transaction_id(existing_ids)
    existing_ids.add(transaction_id)

    sender_age = account_to_age[sender]
    sender_is_elderly = account_to_is_elderly[sender]
    receiver_age = account_to_age[receiver]
    receiver_is_elderly = account_to_is_elderly[receiver]
    sender_gender = account_to_gender[sender]
    receiver_gender = account_to_gender[receiver]
    type_of_fraud = "Legitimate"
    method_of_contact = "Direct"
    loss = 0
    time_of_day = np.random.choice(["Morning", "Afternoon", "Evening", "Night"], p=[0.25, 0.3, 0.3, 0.15])
    resolution_status = "N/A"

    transactions.append([
        transaction_id, sender, sender_age, sender_is_elderly, receiver, receiver_age, receiver_is_elderly,
        amount, date, 0, sender_gender, receiver_gender, type_of_fraud, method_of_contact, loss, time_of_day, resolution_status
    ])
    legit_count += 1

# Step 5: Shuffle transactions
random.shuffle(transactions)

# Step 6: Create DataFrame
columns = [
    "Transaction_ID", "Sender_account", "Sender_age", "Sender_is_elderly", "Receiver_account", "Receiver_age", "Receiver_is_elderly",
    "Amount", "Date", "Is_fraud", "Sender_gender", "Receiver_gender", "Type_of_fraud", "Method_of_contact", "Loss", "Time_of_day", "Resolution_status"
]
df_transactions = pd.DataFrame(transactions, columns=columns)

# Step 7: Save to CSV
df_transactions.to_csv("fraud_23pct_synthetic_dataset_fixed.csv", index=False)

print("Dataset with 23% fraud rate generated and saved as 'synthetic_dataset_fixed.csv'.")
print(f"Fraudulent transactions: {df_transactions['Is_fraud'].sum()} ({df_transactions['Is_fraud'].mean()*100:.1f}%)")