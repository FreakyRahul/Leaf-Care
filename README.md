# LeafCare - Leaf Disease Prediction

**LeafCare** is a web application that uses a Convolutional Neural Network (CNN) model to predict the health of plant leaves across 15 different categories. It classifies leaves into healthy or diseased types, enabling plant care enthusiasts, farmers, and researchers to quickly diagnose and take preventive measures.

## Features

- Predict leaf health based on uploaded images.
- Classifies leaves into 15 categories using a trained CNN model.
- Feedback and messages are stored on Dropbox.
- Easy-to-use interface created using **Streamlit**.
- Fast and reliable access to the trained model using **gdown**.
- Organized website with the following sections:
  - **Home**: Introduction to LeafCare.
  - **About**: Information about the app's purpose and features.
  - **Knowledge Base**: Provides educational resources on plant diseases and their remedies.
  - **Disease Detection**: Core functionality for uploading images and getting predictions.
  - **Contact**: Users can submit feedback or inquiries directly from the app.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Tech Stack](#tech-stack)
3. [Setup Instructions](#setup-instructions)
4. [How to Use](#how-to-use)
5. [Deployment](#deployment)
6. [Environment Variables & Security](#environment-variables--security)
7. [Acknowledgments](#acknowledgments)

---

## Project Overview

The **LeafCare** project is designed to help identify leaf diseases using deep learning techniques. Here's an overview of how the system works:

1. **Model Training**: A CNN model was trained to classify leaf images into 15 categories, including healthy and various disease types.
2. **Streamlit Interface**: A user interface was created using **Streamlit**, which allows users to upload leaf images and get predictions.
3. **Dropbox Integration**: Feedback and user messages are saved to **Dropbox** for later analysis.
4. **Google Drive for Model Storage**: Since the model size was large, it was stored on **Google Drive** and accessed via **gdown** during app calls.
5. **Deployment**: The app was deployed on **Streamlit Cloud**, allowing users to access it from anywhere.

---

## Tech Stack

- **Python** (3.12)
- **TensorFlow** (2.18.0) for model training
- **Streamlit** (1.40.1) for creating the user interface
- **Dropbox** (12.0.2) for storing feedback
- **gdown** for accessing large models stored on Google Drive
- **NumPy** (1.26.4) and **Pandas** (2.1.3) for data handling
- **python-dotenv** for managing environment variables securely

---

## Setup Instructions

To run this project locally, follow the steps below:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Leaf-Care.git
cd Leaf-Care
```

### 2. Install dependencies

Ensure you have Python 3.12 installed, and then create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
```

Then install the required libraries:

```bash
pip install -r requirements.txt
```

### 3. Setup Dropbox and Environment Variables

- Create a Dropbox account and generate an **Access Token**.
- Store the Dropbox token as an environment variable in a `.env` file. Create a `.env` file in the project root and add the following:

```bash
DROPBOX_ACCESS_TOKEN=your_dropbox_access_token
```

Make sure that the `.env` file is added to `.gitignore` for security reasons.

---

## How to Use

1. **Train the Model**: You can train the CNN model using your own dataset by running the `model_training.ipynb` script. This will save the model as a `.keras` file.
   
2. **App Interface**: To run the Streamlit app locally, execute:

```bash
streamlit run app.py
```

This will open a local server where you can upload a leaf image and get predictions about its health.

3. **Upload Model to Google Drive**: Since the model is large, upload it to your Google Drive, and use the `gdown` module to download it when the app is running.

---

## Deployment

To deploy the app on **Streamlit Cloud**:

1. Create an account on [Streamlit](https://streamlit.io).
2. Link your GitHub repository to Streamlit.
3. Set up **secrets** for the Dropbox access token in the Streamlit Cloud interface for secure usage.
4. Push your repository to GitHub, and Streamlit will handle the deployment automatically.
   
Once deployed, your app will be accessible via a public URL:  
`https://leafcare.streamlit.app`

---

## Environment Variables & Security

To ensure your Dropbox access token remains secure:

- Use **environment variables** to store sensitive data like API tokens. 
- Make sure your `.env` file is added to **`.gitignore`** to prevent it from being committed to GitHub.

Here’s an example of your `.gitignore` file:

```bash
.env
__pycache__/
*.pyc
```

---

## Acknowledgments

- **TensorFlow**: Used for creating and training the Convolutional Neural Network (CNN).
- **Streamlit**: For creating the interactive user interface.
- **Dropbox**: Used for storing feedback and messages.
- **Google Drive**: For storing the large model files and accessing them using **gdown**.

---

Happy coding! If you find any bugs or issues, feel free to open an issue in the repository!
