import pandas as pd
from faker import Faker
import random

fake = Faker()

def generate_entity_data(num_records):
    """
    Generate synthetic entity data.

    Parameters:
    - num_records (int): Number of records to generate.

    Returns:
    - list of dict: List containing dictionaries with synthetic entity data.
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

def create_synthetic_data(num_records_per_entity, match_percentage=0.8):
    """
    Create synthetic data for two entities with a specified match percentage.

    Parameters:
    - num_records_per_entity (int): Number of records per entity.
    - match_percentage (float): Percentage of records that should match between the entities.

    Returns:
    - tuple of DataFrames: Two DataFrames representing synthetic data for two entities.
    """
    entity1_data = generate_entity_data(num_records_per_entity)
    entity2_data = generate_entity_data(num_records_per_entity)

    num_matches = int(num_records_per_entity * match_percentage)
    for i in range(num_matches):
        match_index_entity1 = random.randint(0, num_records_per_entity - 1)
        match_index_entity2 = random.randint(0, num_records_per_entity - 1)
        entity2_data[match_index_entity2] = entity1_data[match_index_entity1]

    entity1_df = pd.DataFrame(entity1_data)
    entity2_df = pd.DataFrame(entity2_data)

    entity1_df['EntityID'] = ['Entity1_' + str(i) for i in range(1, num_records_per_entity + 1)]
    entity2_df['EntityID'] = ['Entity2_' + str(i) for i in range(1, num_records_per_entity + 1)]

    return entity1_df, entity2_df

if __name__ == "__main__":
    num_records_per_entity_example = 100
    match_percentage_example = 0.8
    entity1_df_example, entity2_df_example = create_synthetic_data(num_records_per_entity_example,
                                                               match_percentage_example)

    # Additional script-specific code can be added here if needed
    print(entity1_df_example.head())
    print(entity2_df_example.head())