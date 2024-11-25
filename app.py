import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd
from kn_base import get_knowledge
import datetime
from datetime import datetime
import os
import dropbox
from dotenv import load_dotenv
import gdown
import pytz


# Set the timezone (for example, IST)
india_timezone = pytz.timezone('Asia/Kolkata')

# Get the current time in UTC and convert it to IST
current_time_utc = datetime.now(pytz.utc)
current_time_local = current_time_utc.astimezone(india_timezone)

# Extract date and timestamp separately
formatted_date = current_time_local.strftime('%Y-%m-%d')  # YYYY-MM-DD format
formatted_time = current_time_local.strftime('%H:%M:%S')  # HH:MM:SS format

# Load environment variables from .env file
load_dotenv()

# Access token from environment variable
access_token = os.getenv('DROPBOX_ACCESS_TOKEN')

if not access_token:
    raise ValueError("Dropbox Access Token not found. Check your environment variables.")

# intialization
dbx = dropbox.Dropbox(access_token)

# Function to upload a file to Dropbox
def upload_to_dropbox(file_path, dropbox_path):
    try:
        with open(file_path, "rb") as f:
            file_data = f.read()
            dbx.files_upload(file_data, dropbox_path, mode=dropbox.files.WriteMode.overwrite)
        st.success("Your message has been saved.")
    except dropbox.exceptions.AuthError as e:
        st.error(f"Error: {e}")

# for feedback--
def save_to_csv_and_dropbox(rating , feedback, user_name, user_email):
    data = {
        "Name": user_name,
        "Email": user_email,
        "Rating" : rating,
        "Feedback": feedback,
        "Date" : formatted_date,
        "Timestamp": formatted_time
    }

    # Save feedback to a local CSV file
    file_path = "feedback.csv"
    if not os.path.exists(file_path):
        # Write the header row if the file is new
        df = pd.DataFrame([data])
        df.to_csv(file_path, mode='w', header=True, index=False)
    else:
        # Append the message data to the existing CSV file
        df = pd.DataFrame([data])
        df.to_csv(file_path, mode='a', header=False, index=False)
    # Upload the CSV to Dropbox
    dropbox_path = '/feedback/feedback.csv'  # Dropbox folder path where the file will be saved
    upload_to_dropbox(file_path, dropbox_path)
    return "Thank you for your Feedback!"


# for contact messaging

def save_to_csv_and_dropbox_msg(message, user_name, user_email):
    data = {
        "Name": user_name,
        "Email": user_email,
        "Message": message,
        "Date" : formatted_date,
        "Timestamp": formatted_time
    }

    # Save feedback to a local CSV file
    file_path = "message.csv"
    if not os.path.exists(file_path):
        # Write the header row if the file is new
        df = pd.DataFrame([data])
        df.to_csv(file_path, mode='w', header=True, index=False)
    else:
        # Append the message data to the existing CSV file
        df = pd.DataFrame([data])
        df.to_csv(file_path, mode='a', header=False, index=False)
    # Upload the CSV to Dropbox
    dropbox_path = '/message/message.csv'  # Dropbox folder path where the file will be saved
    upload_to_dropbox(file_path, dropbox_path)
    return "Thank you for your message!"


# gettign download from google drive the model
# File ID from your Google Drive link
file_id = "1NLv7xgvuNp7VNnXSPDT3C55S52mQ625M"
url = f"https://drive.google.com/uc?id={file_id}"

# Output file path
output = "Final_model.keras"
# Check if file already exists
if not os.path.exists(output):
    gdown.download(url, output, quiet=False)
else:
    print(f"{output} already exists. Skipping download.")

# Function for Prediction

def model_prediction(test_image):
    model = tf.keras.models.load_model(output)
    
    # Preprocess the uploaded image
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(256, 256))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.expand_dims(input_arr, axis=0) / 255.0  # Normalize the image
    
    # Get predictions
    predictions = model.predict(input_arr)
    max_prob = np.max(predictions)  # Confidence of the top prediction
    predicted_index = np.argmax(predictions)  # Index of the predicted class
    
    return predicted_index, max_prob,input_arr[0]

# Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home","Disease Recognition","Knowledge Base", "About", "Contact"])

# Main Page
if app_mode == "Home":
    st.header("PLANT DISEASE RECOGNITION SYSTEM")
    image_path = "image/home_page.jpeg"
    st.image(image_path, use_container_width=True)
    st.markdown("""
    Welcome to the Plant Disease Recognition System! 🌿🔍

    Our mission is to help in identifying plant diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!

    ### How It Works
    1. **Upload Image:** Go to the **Disease Recognition** page and upload an image of a plant with suspected diseases.
    2. **Analysis:** Our system will process the image using advanced algorithms to identify potential diseases.
    3. **Results:** View the results and get recommendations from **knowledge base** section for further action.

    ### Why Choose Us?
    - **Accuracy:** Our system utilizes state-of-the-art deep learning techniques for accurate disease detection.
    - **User-Friendly:** Simple and intuitive interface for seamless user experience.
    - **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.

    ### Get Started
    Click on the **Disease Recognition** page in the sidebar to upload an image and experience the power of our Plant Disease Recognition System!

    ### About Us
    Learn more about the project, our team, and our goals on the **About** page.
    """)

# About Project
elif app_mode == "About":
    st.header("About")
    st.markdown("""
                #### About Dataset
                This dataset is recreated using offline augmentation from the original dataset. The original dataset can be found on kaggle.
                This dataset consists of about 18K RGB images of healthy and diseased crop leaves which is categorized into 15 different classes. The total dataset is divided into an 70/20/10 ratio of training validation and test sets, preserving the directory structure.
                #### Content
                1. train (14440 images)
                2. test (2076 images)
                3. validation (4122 images)
                """)
    

# Contact Page
elif app_mode == "Contact":
    st.header("Contact Us")
    st.markdown("""
    For any queries or feedback, please reach out to us:
    - **Email**: lightofcandle5879@gmail.com
    """)
    
    # Get the message input from the user
    message = st.text_area("Leave a Message")
    
    # Optionally, get user details (if needed)
    user_name = st.text_input("Your Name (optional)")
    user_email = st.text_input("Your Email (optional)")
    
    # Submit button for the message form
    msg_btn = st.button("Submit Feedback")
        # Submit button
    if msg_btn:
        if message:
            # Capture and save feedback
            message = save_to_csv_and_dropbox_msg(message, user_name, user_email)
            
            # Show success message
            st.success(message)
            
            # Show the submission date and time
            st.write(f"Message submitted on {formatted_date} at {formatted_time}")
        else:
            st.error("Please provide your message or any query before submitting.")


# Prediction Page
elif app_mode == "Disease Recognition":
    st.header("Disease Recognition")
    test_image = st.file_uploader("Choose an Image:", type=["jpg", "jpeg", "png"])
    
    if test_image is not None:
        # Display the image
        st.image(test_image, use_container_width=True)
        
        # Predict button
        if st.button("Predict"):
            st.snow()
            st.write("Analyzing...")

            # Get prediction and confidence
            result_index, max_prob, preprocessed_image = model_prediction(test_image)
            
            # Define class names (update with actual class names from your model)
            class_name = [
                'Pepper__bell___Bacterial_spot', 'Pepper__bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Tomato_Bacterial_spot', 'Tomato_Early_blight', 'Tomato_Late_blight', 'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot', 'Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato__Target_Spot', 'Tomato__Tomato_YellowLeaf__Curl_Virus', 'Tomato__Tomato_mosaic_virus', 'Tomato_healthy'
                # Add all your actual class names here
            ]

            # Confidence threshold for "Unknown"
            # Confidence threshold for valid predictions
            threshold = 0.4

            # Check confidence and index validity
            if max_prob >= threshold and 0 <= result_index < len(class_name):
                # Valid prediction with high confidence
                disease_name = class_name[result_index]
                st.success(f"Prediction: {disease_name} ({max_prob * 100:.2f}% confidence)")
            else:
                # Low confidence or invalid index -> Unknown
                st.warning("The model is uncertain about this image.")
                st.success(f"Prediction: Unknown (low confidence)")



# Feedback Form
    st.subheader("Feedback")
    with st.form("feedback_form"):
        # Get feedback input from the user
        rating = st.slider("Rating (1 to 5)", min_value=1, max_value=5)
        feedback = st.text_area("Your feedback")

        # Optionally, get user details (if needed)
        user_name = st.text_input("Your Name (optional)")
        user_email = st.text_input("Your Email (optional)")
        # Submit button (using form_submit_button)
        submit_button = st.form_submit_button("Submit Feedback")
        # Submit button
        if submit_button:
            if feedback:
                # Capture and save feedback
                feedback = save_to_csv_and_dropbox(rating, feedback, user_name, user_email)
                
                # Show success message
                st.success(feedback)
                
                # Show the submission date and time
                st.write(f"Feedback submitted on {formatted_date} at {formatted_time}")
            else:
                st.error("Please provide your feedback before submitting.")


# Knowledge Base Page
elif app_mode == "Knowledge Base":
    st.header("Plant Knowledge Base")
    
    # Dropdown for selecting leaf type
    plant = st.selectbox("Select a Plant", ["Pepper", "Potato", "Tomato"])
    if plant == "Tomato":
            # General Information about Tomato
            st.subheader("General Information about Tomato")
            st.markdown("""
                **Description:** Tomatoes are one of the most widely cultivated crops, valued for their juicy, flavorful fruits that are rich in vitamins A, C, and antioxidants.
                
                **Growing Conditions:**
                - **Soil:** Well-draining, loamy soil with pH 6.0–6.8.
                - **Temperature:** Optimal range is 21°C to 27°C.
                - **Watering:** Maintain consistent moisture levels but avoid waterlogging.
                - **Light:** Requires 6–8 hours of full sunlight daily.
            """) 
    elif plant == "Pepper":
            # General Information about Pepper (Bell Pepper)
            st.subheader("General Information about Bell Pepper")
            st.markdown("""
                **Description:** Bell peppers are sweet peppers commonly grown for their colorful fruits, which are rich in vitamins and antioxidants.
                
                **Growing Conditions:**
                - **Soil:** Well-draining, rich in organic matter.
                - **Temperature:** Warm, between 21°C to 29°C.
                - **Watering:** Keep the soil evenly moist but avoid waterlogging.
                - **Light:** Requires full sunlight for 6–8 hours daily.
            """)
        
    elif plant == "Potato":
        # General Information about Potato
        st.subheader("General Information about Potato")
        st.markdown("""
            **Description:** Potato plants are tuber-producing crops that are a staple food worldwide, rich in carbohydrates and essential vitamins.
            
            **Growing Conditions:**
            - **Soil:** Loose, well-draining, and rich in organic matter.
            - **Temperature:** Cool climates, between 15°C to 20°C for optimal tuber development.
            - **Watering:** Keep soil moist, especially during tuber formation, but avoid overwatering.
            - **Light:** Requires full sunlight for at least 6 hours daily.
        """)
        
    # Get the possible leaf conditions based on the plant selected
    leaf_options = {
        "Pepper": ["Pepper__bell___Bacterial_spot", "Pepper__bell___healthy"],
        "Potato": ["Potato___Early_blight", "Potato___Late_blight", "Potato___healthy"],
        "Tomato": ["Tomato_Bacterial_spot", "Tomato_Early_blight", "Tomato_Late_blight", 
                    "Tomato_Leaf_Mold", "Tomato_Septoria_leaf_spot", "Tomato_Spider_mites_Two_spotted_spider_mite", 
                    "Tomato_Target_Spot", "Tomato_Tomato_YellowLeaf_Curl_Virus", "Tomato_Tomato_mosaic_virus", "Tomato_healthy"]
    }

     # Dictionary of images for each leaf condition
    leaf_images = {
        "Pepper__bell___Bacterial_spot": "image/Pepper_Bell_Bacterial_Spot.JPG",
        "Pepper__bell___healthy": "image/Pepper_Bell_Healthy.JPG",
        "Potato___Early_blight": "image/Potato___Early_blight.JPG",
        "Potato___Late_blight": "image/Potato___Late_blight.JPG",
        "Potato___healthy": "image/Potato___healthy.JPG",
        "Tomato_Bacterial_spot": "image/Tomato_Bacterial_spot.JPG",
        "Tomato_Early_blight": "image/Tomato_Early_blight.JPG",
        "Tomato_Late_blight": "image/Tomato_Late_blight.JPG",
        "Tomato_Leaf_Mold": "image/Tomato_Leaf_Mold.JPG",
        "Tomato_Septoria_leaf_spot": "image/Tomato_Septoria_leaf_spot.JPG",
        "Tomato_Spider_mites_Two_spotted_spider_mite": "image/Tomato_Spider_mites_Two_spotted_spider_mite.JPG",
        "Tomato_Target_Spot": "image\Tomato__Target_Spot.JPG",
        "Tomato_Tomato_YellowLeaf_Curl_Virus": "image/Tomato__Tomato_YellowLeaf__Curl_Virus.JPG",
        "Tomato_Tomato_mosaic_virus": "image/Tomato__Tomato_mosaic_virus.JPG",
        "Tomato_healthy": "image/Tomato_healthy.JPG"
    }
    
        
    # Dropdown for selecting leaf condition
    leaf_type = st.selectbox("Select a Leaf Condition", leaf_options.get(plant, []))
    
    if leaf_type:

        # Display image for the selected leaf condition
        if leaf_type in leaf_images:
            st.image(leaf_images[leaf_type], caption=leaf_type.replace('_', ' ').title(), use_container_width=True)
        
        # Fetch and display knowledge for the selected leaf type
        knowledge = get_knowledge(leaf_type)
        
        if knowledge != "Information not available":
            st.subheader(f"Information about {leaf_type.replace('_', ' ').title()}")
            st.markdown(f"**Description:** {knowledge.get('Description', 'N/A')}")
            
            if 'Symptoms' in knowledge:
                st.markdown(f"**Symptoms:**")
                for symptom in knowledge['Symptoms']:
                    st.markdown(f"- {symptom}")
            
            if 'Causes' in knowledge:
                st.markdown(f"**Causes:**")
                for care in knowledge['Causes']:
                    st.markdown(f"- {care}")

            if 'Care' in knowledge:
                st.markdown(f"**Care:**")
                for cause in knowledge['Care']:
                    st.markdown(f"- {cause}")

            if 'Prevention' in knowledge:
                st.markdown(f"**Prevention:**")
                for prevention in knowledge['Prevention']:
                    st.markdown(f"- {prevention}")
            
            if 'Cure' in knowledge:
                st.markdown(f"**Cure:**")
                for cure in knowledge['Cure']:
                    st.markdown(f"- {cure}")
            
            # Check and display additional details like Characteristics, Pest Management, and Harvesting
            if 'Characteristics' in knowledge:
                st.markdown(f"**Characteristics:**")
                for characteristic in knowledge['Characteristics']:
                    st.markdown(f"- {characteristic}")
            
            if 'Pest_Management' in knowledge:
                st.markdown(f"**Pest Management:**")
                for pest in knowledge['Pest_Management']:
                    st.markdown(f"- {pest}")
            
            if 'Harvesting' in knowledge:
                st.markdown(f"**Harvesting:**")
                for harvesting in knowledge['Harvesting']:
                    st.markdown(f"- {harvesting}")
        else:
            st.warning(knowledge)

