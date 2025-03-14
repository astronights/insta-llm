# Instagram Marketing with Large Language Models (LLM)

This repository leverages the power of Large Language Models (LLM) to generate and enhance content for Instagram marketing, aimed at boosting engagement and improving the visibility of business accounts on the platform. It provides tools to automate bio updates, caption generation for posts, and media uploads.

## Table of Contents
- [Overview](#overview)
- [App Features](#app-features)
- [Large Language Modelling](#large-language-modelling)
- [More Scripts](#more-scripts)
- [Running the Code](#running-the-code)
  - [Prerequisites](#prerequisites)
  - [API Keys](#api-keys)
  - [Installation](#installation)
  - [Starting the Server](#starting-the-server)

---

## Overview

This project is specifically designed to cater to **Instagram business accounts**. It integrates LLMs with the Instagram API to optimize social media presence for business owners, with an emphasis on driving operations through mobile devices. 

The app includes features that assist business accounts—particularly in the fashion industry—by generating relevant content, including captions and hashtags, to enhance post engagement. While the fashion-specific UI components (e.g., garment sizes) are client-side and customizable, the core functionality can be adapted to any industry.

### **Note**:
- This app **only supports Instagram business accounts**.
- The UI components are **optimized for mobile view**, making it suitable for business owners managing their Instagram accounts via mobile devices.
- Some UI elements are **designed with fashion businesses in mind** but can be customized to suit other industries.

---

## App Features

This app utilizes **Generative AI** techniques to automate content generation for Instagram posts and profiles. Here's a breakdown of the core features:

### 1. **Update Instagram Bio**
   Automatically generate or update the bio of an Instagram business account using LLM-generated content tailored to your niche or market.

### 2. **Caption Existing Posts**
   Provide intelligent and engaging captions for your existing posts, making them more relatable and shareable. The model can also generate hashtags to boost the visibility of the posts.

### 3. **Caption and Upload New Posts**
   Create new content by uploading images and getting auto-generated captions, hashtags, and descriptions. The app allows direct posting to Instagram business accounts.

---

## Large Language Modelling

The backbone of the project is powered by **Google's `Gemini 2.0 Flash` LLM**. This model is employed for its robust free tier and impressive capabilities in handling both text and media content generation.

### **1. Fine-Tuned Prompts**
   The LLM has been fine-tuned with specific prompts for various use cases, such as bio updates, caption generation, and hashtag creation, to align with social media marketing best practices.

### **2. Media Understanding**
   The LLM is fed not only text inputs but also image and media data, allowing it to generate more contextual and visually relevant content.

### **3. Social Media Optimization**
   The generated outputs are crafted to appeal to Instagram's algorithms, with content tailored to increase post engagement and profile reach. Custom hashtags are generated based on the media and target audience.

### **4. Output Formatting**
   The model outputs data in structured **JSON** format, making it easy to integrate directly into the UI components of the app for a seamless user experience.

---

## More Scripts

The project also contains scripts to help you update your old posts in bulk. These can be triggered manually with Python. In order to run these scripts, you would require the credentials, access token and the Gemini API Key.

```bash
.
├── scripts
│   ├── crawler.py      # Crawl all historical posts by the user.
│   ├── genai.py        # Generate captions with the LLM.
│   ├── postprocess.py  # Perform any post processing steps required.
│   └── automation.csv  # Automate the update of captions.
```

**NOTE**: The automation script requires Selenium, the version of which is mentioned in the requirements.

---

## Running the Code

Follow these steps to get the application up and running on your local machine.

### **Prerequisites**

Before running the app, make sure the following dependencies are installed:

- **Python 3.12**: Backend is written in Python.
- **Git**: For cloning the repository and version control.

### **API Keys**

To interact with Instagram, you'll need to set up a developer account and generate API keys:

1. Go to the [Meta Developer Portal](https://developers.facebook.com/) and create a new app.
2. Enable the **Instagram Graph API** for your app.
3. Generate the required **API keys** for authentication (Client ID, Client Secret, Access Tokens).

### **Installation**

1. **Clone the Repository**:

Begin by cloning the repository to your local machine:

   ```bash
   git clone https://github.com/astronights/instagram-marketing-llm.git
   cd instagram-marketing-llm
   ```

2. **Create a Python Virtual Environment**

It's recommended to create a virtual environment to keep your dependencies isolated:

   ```bash
   python -m venv insta_llm
   insta_llm\Scripts\activate  # For Windows
   source insta_llm/bin/activate  # For macOS/Linux
   ```

3. **Install Dependencies**

Install the required Python packages by running:

   ```bash
   pip install -r requirements.txt
   ```

## Starting the Server

1. **Run the Flask App**

Once all dependencies are installed, you can start the Flask server:

   ```bash
   flask --app api/index run -p 5328
   ```

This will start the Flask app on port `5328`, which you can access by navigating to `http://localhost:5328` in your browser.


## Contributing

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcomed.