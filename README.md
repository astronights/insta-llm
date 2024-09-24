# Instagram Marketing with LLM

This repository uses Large Language Modelling to generate content for Instagram marketing to boost engagement.

**NOTE**: 
- This app supports only Instagram business accounts.
- The webpages rendered as part of this are optimized for mobile view, targeted towards business owners driving a significatn chunk of their operations via mobile.

## Running the Code

### **Prerequisites**

Before you begin, ensure you have the following installed:

- **Python 3.12** (for the backend)
- **Git** (for version control)

### **Installation** 

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/astronights/llm-amazing-race-ai.git
   cd llm-amazing-race-ai
   ```

2. **Install the Requirements:**

    ```bash
    # Create an environment if you need to
    python -m venv insta_llm
    insta_llm\Scripts\activate
    pip install -r requirements.txt
    ```

3. **Start the Flask Server:**

   ```bash
   flask --app api/index run -p 5328
   ```