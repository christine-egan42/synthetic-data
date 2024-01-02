import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from faker import Faker
import random
import warnings
warnings.filterwarnings("ignore")

fake = Faker()

def generate_synthetic_complaints(num_complaints):
    """
    Generate synthetic complaints data for visualization.

    Parameters:
    - num_complaints (int): Number of synthetic complaints to generate.

    Returns:
    - list: List of dictionaries containing synthetic complaints data.
    """
    complaints = []
    for _ in range(num_complaints):
        complaint = {
            'ComplaintID': fake.uuid4(),
            'ComplainantType': random.choice(['Individual', 'Bank', 'Accountant', 'Whistleblower']),
            'ComplainantName': fake.name(),
            'ComplainantEmail': fake.email(),
            'ComplainantPhone': fake.phone_number(),
            'ComplaintDate': fake.date_this_decade(),
            'ComplaintTime': fake.time(),
            'SuspectedFraudType': random.choice(['Embezzlement', 'Cooking the Books', 'False Reporting', 'Tax Evasion']),
            'EvidenceFile': fake.file_name(extension='pdf'),
            'Status': random.choice(['Pending', 'Under Investigation', 'Closed']),
        }
        complaints.append(complaint)
    return complaints

def visualize_customer_data(customer_data):
    """
    Visualize synthetic customer data.

    Parameters:
    - customer_data (list): List of dictionaries containing synthetic customer data.

    Returns:
    - None
    """
    # Convert data to DataFrame
    customer_df = pd.DataFrame(customer_data)

    # Pie chart for Complainant Types
    plt.figure(figsize=(10, 6))
    customer_df['ComplainantType'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
    plt.title('Distribution of Complainant Types')
    plt.ylabel('')  # Remove y-axis label
    plt.show()

    # Bar chart for Suspected Fraud Types
    plt.figure(figsize=(12, 6))
    sns.countplot(x='SuspectedFraudType', data=customer_df, palette='mako')
    plt.title('Distribution of Suspected Fraud Types')
    plt.xlabel('Suspected Fraud Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.show()

    # Horizontal bar chart for Complaint Status
    plt.figure(figsize=(8, 6))
    sns.countplot(y='Status', data=customer_df, hue='Status', palette='rocket', legend=False)
    plt.title('Distribution of Complaint Status')
    plt.xlabel('Count')
    plt.ylabel('Complaint Status')
    plt.show()

if __name__ == "__main__":
    num_complaints_example = 500
    synthetic_customer_data = generate_synthetic_complaints(num_complaints_example)
    visualize_customer_data(synthetic_customer_data)