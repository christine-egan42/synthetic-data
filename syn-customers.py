from faker import Faker
import pandas as pd

fake = Faker()

def generate_synthetic_data(num_records):
    """
    Generate synthetic customer data.

    Parameters:
    - num_records (int): Number of records to generate.

    Returns:
    - list of dict: List containing dictionaries with synthetic customer data.
    """
    data = []
    for _ in range(num_records):
        record = {
            'Name': fake.name(),
            'Address': fake.address(),
            'Email': fake.email(),
            'Phone': fake.phone_number(),
            'DOB': fake.date_of_birth(),
        }
        data.append(record)
    return data

if __name__ == "__main__":
    # Generate synthetic data for 1000 customers
    synthetic_customer_data = generate_synthetic_data(1000)

    # Convert data to DataFrame
    synthetic_df = pd.DataFrame(synthetic_customer_data)

    # Additional script-specific code can be added here if needed
    print(synthetic_df.head())