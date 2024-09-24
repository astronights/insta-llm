# Instagram Marketing with LLM

This repository uses Large Language Modelling to generate content for Instagram marketing to boost engagement.

This repository is still Work in Progress. Changes are being made regularly to arrive at a working solution.

**NOTE**: 
- This app supports only Instagram business accounts.
- The webpages rendered as part of this are optimized for mobile view, targeted towards business owners driving a significatn chunk of their operations via mobile.

## Running the Code

### **Prerequisites**

Before you begin, ensure you have the following installed:

- **Python 3.12** (for the backend)
- **Git** (for version control)

### API Keys

Generate your API ID and Keys from the Meta Developer Portal for access.

### **Installation** 

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/astronights/instagram-marketing-llm.git
   cd instagram-marketing-llm
   ```

2. **Install the Requirements:**

    ```bash
    # Create an environment
    python -m venv insta_llm
    insta_llm\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Start the Flask Server:**

   ```bash
   flask --app api/index run -p 5328
   ```