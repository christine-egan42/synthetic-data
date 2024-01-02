**Create Synthetic Data with Python and Faker**


The scarcity of high-quality, diverse datasets can be a significant roadblock. Synthetic data, which is data that is artificially generated to mimic real-world scenarios, can be a solution to this challenge. 

**The Importance of Synthetic Data:**
- In various industries, the availability of relevant and comprehensive datasets is often limited by privacy concerns, data access restrictions, or simply the absence of historical information.
- Synthetic data serves as a bridge, enabling organizations to simulate realistic scenarios, test algorithms, and develop models without compromising sensitive information.

**Why You Might Need Synthetic Data:**
1. **Privacy and Compliance:** In sectors where privacy regulations are stringent (such as healthcare and finance), using real data for testing and development may risk violating privacy laws. Synthetic data allows organizations to adhere to compliance requirements without sacrificing the quality of their testing environments.

2. **Data Diversity:** Real-world datasets may lack diversity, hindering the robustness of models. Synthetic data offers the flexibility to create diverse datasets that encompass a wide range of scenarios, ensuring that models are trained to handle a variety of situations.

3. **Limited Historical Data:** For emerging technologies or novel applications, historical data may be scarce. Synthetic data allows organizations to create training datasets, even in the absence of a rich historical record, accelerating the development of innovative solutions.

**Creating Synthetic Data with Faker:**
The `Faker` library in Python simplifies the process of generating synthetic data with its vast array of functions that produce realistic names, addresses, emails, and more. 

Here's a simplified example of creating synthetic customer data:

```python
from faker import Faker
import pandas as pd

fake = Faker()

def generate_synthetic_data(num_records):
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

# Generate synthetic data for 1000 customers
synthetic_customer_data = generate_synthetic_data(1000)

# Convert data to DataFrame
synthetic_df = pd.DataFrame(synthetic_customer_data)
```

In this repository, there are three scripts to create synthetic data with Python and Faker, for three different use cases.

- **Customer Data**: Creates a table of synthetic customer data that includes Names, Addresses, Emails, Phone Numbers, and Date of Birth. It's similar to the example above.

- **Entity Resolution Data**: Generates two different lists of entities, with some overlap. Good for simulating entity resolution scenarios.

  
- **Complaint Data**: Creates a data set that includes caller data, like Name and Phone Number. The other fields generate random data related to hotline complaints. Can be edited or expanded to fit any kind of survey or self-reporting scenario. There is additional functionality to build out graphs to simulate EDA.

![graph-1](https://github.com/christine-egan42/synthetic-data/assets/116017015/ac292a54-6b3f-49d9-970b-11c4a4cb583d)

![graph-2](https://github.com/christine-egan42/synthetic-data/assets/116017015/9a4a42f5-82bc-4979-b6a5-03a8b1079290)

![graph-3](https://github.com/christine-egan42/synthetic-data/assets/116017015/499554bf-cbec-4afc-89f4-0da3c2411fba)
