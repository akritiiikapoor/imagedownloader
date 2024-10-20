import streamlit as st
from serpapi import GoogleSearch
import requests
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import zipfile
import shutil 

def download_images(query, num_images, api_key):
    if os.path.exists('images'):
        shutil.rmtree('images')  
    os.mkdir('images')  
    
    params = {
        "q": query,
        "tbm": "isch",
        "num": num_images,
        "api_key": api_key
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    images = results['images_results']
    
    image_urls = []
    progress_bar = st.progress(0)
    
    for index, image in enumerate(images):
        if index >= num_images:
            break
        image_url = image['original']
        image_urls.append(image_url)
        image_response = requests.get(image_url)
        with open(f"images/{query}_image_{index + 1}.jpg", 'wb') as f:
            f.write(image_response.content)
        
        progress_bar.progress((index + 1) / num_images)
    
    return image_urls

def zip_images(zip_filename):
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for foldername, subfolders, filenames in os.walk('images'):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                zipf.write(file_path, os.path.basename(file_path))
    
    return zip_filename

def send_email(sender_email, sender_password, receiver_email, subject, body, zip_file_path):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    with open(zip_file_path, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(zip_file_path)}')
        msg.attach(part)
    
    server.send_message(msg)
    server.quit()

st.markdown("""
    <style>
        body {
            background-color: #f0f2f5;
        }
        .title {
            font-family: 'Helvetica', sans-serif;
            color: #4B0082;
            font-size: 2.5em;
            text-align: center;
        }
        .header {
            font-family: 'Helvetica', sans-serif;
            color: #333;
            font-size: 1.5em;
            text-align: left;
        }
        .stTextInput>div>input {
            border: 2px solid #4B0082;
            border-radius: 5px;
            padding: 10px;
        }
        .stNumberInput>div>input {
            border: 2px solid #4B0082;
            border-radius: 5px;
            padding: 10px;
        }
        .stButton>button {
            background-color: #4B0082;
            color: white;
            padding: 10px;
            border-radius: 5px;
        }
        .stButton>button:hover {
            background-color: #6A0DAD;
        }
    </style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="title">Image Downloader and Email Sender</h1>', unsafe_allow_html=True)
    
    
    st.sidebar.header("User Input")
    query = st.sidebar.text_input("Enter the object to search for images")
    num_images = st.sidebar.number_input("Enter the number of images to download", min_value=1, max_value=50, value=5)
    receiver_email = st.sidebar.text_input("Enter the receiver's email")
    
    
    api_key = "7d22a195e68327a830b9a5d149d737a3a32bfc6cf055a34003d157c80de806fe"  
    
    sender_email = "akritiikapoor@gmail.com"
    sender_password = "rraskabkxvnomumb"  
    
    
    if st.sidebar.button("Download and Send Images"):
        
        st.write(f"Downloading {num_images} images of '{query}'...")
        downloaded_images = download_images(query, num_images, api_key)
        
        
        zip_filename = "images.zip"
        zip_images(zip_filename)
        
        
        st.write(f"Sending images to {receiver_email}...")
        send_email(
            sender_email=sender_email,
            sender_password=sender_password,
            receiver_email=receiver_email,
            subject=f"{num_images} Images of {query}",
            body=f"Here are the {num_images} images of {query} you requested.",
            zip_file_path=zip_filename
        )
        
        st.success(f"Images sent to {receiver_email}!")

if __name__ == '__main__':
    main()
