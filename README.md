# **Streamlit Image Downloader and Email Sender**

A **simple web app** that allows users to **search, download, zip, and email images** based on a search query. Built using **Python**, **Streamlit**, **SerpAPI**, and **smtplib**.

---

## **Overview**

This **Streamlit-based app** enables users to:  
- **Search** and **download images** from Google.  
- **Compress** the images into a **ZIP file**.  
- **Send** the images via **email**.  

The app features an **intuitive interface** that is designed for simplicity and minimal input.

---

## **Requirements**

To run this app locally, ensure you have the following:

### **Prerequisites**
- **Python 3.x**  

### **Required Python Libraries**
- **Streamlit**  
- **SerpAPI** (`pip install serpapi`)  
- **Requests**  
- **smtplib** *(built-in)*  
- **zipfile** *(built-in)*  

---

## **How It Works**

The interface is user-friendly and includes the following **sidebar input fields**:  

- **Search Query**: Enter the object or term to search for images.  
- **Number of Images**: Specify the number of images to download *(default: 5, maximum: 50)*.  
- **Recipient Email**: Input the email address where the ZIP file of images will be sent.  

### **Steps to Use the App**
1. Input the required fields in the sidebar.  
2. Click the **"Download and Send Images"** button.  
3. The app will:  
   - Search and download images.  
   - Compress the images into a ZIP file.  
   - Send the ZIP file to the specified email address.  


![Screenshot 2024-10-21 034811](https://github.com/user-attachments/assets/c6e4574c-3a2d-4d1f-9f79-8b12cff4bb18)

---

## **Features**
- **Simple Interface**: Easy to use with minimal input.  
- **Fast Downloads**: Fetches images quickly based on the search query.  
- **Automatic Compression**: Zips all downloaded images.  
- **Email Integration**: Seamlessly sends the images to your desired recipient.  

---

## **Technologies Used**
- **Streamlit**: Web app framework for building the interface.  
- **SerpAPI**: Fetches images from Google search.  
- **smtplib**: Handles email sending functionality.  
- **Python Standard Libraries**: `requests`, `zipfile`.  

---

## Key Interface Elements:
- Custom Styling: The app uses custom CSS to enhance its appearance.
- Progress Bar: A progress bar is shown to indicate the status of image downloading and sending.


![Screenshot 2024-10-21 034856](https://github.com/user-attachments/assets/bbfefcd6-2003-4248-a7eb-4125a5ea7086)
![Screenshot 2024-10-21 034933](https://github.com/user-attachments/assets/b3c6ee23-4f42-4e5d-bc64-a4b144ae7f2f)

---

## **Working of the Code**

### **1. Image Search and Download**
- The app uses **SerpAPI** to search for images based on the user’s input.  
- The images are **downloaded** to a folder named **"images"**.  
- To ensure a clean workflow, the app **clears the folder** after each search, preventing old images from being included in subsequent downloads.  

---

### **2. Zipping the Images**
- After downloading the images, they are **compressed** into a single ZIP file using the Python **`zipfile`** module.  
- This ensures that all downloaded images are packaged neatly for easy sharing.  

---

### **3. Email Sending**
- Using the **smtplib** library, the app **sends the ZIP file** as an attachment to the recipient’s email.  
- The sender’s email and app password are **hardcoded** for simplicity in this implementation.  

---

This streamlined workflow ensures the app functions efficiently, providing a seamless experience for searching, downloading, and sharing images. 🚀

![Screenshot 2024-10-21 035020](https://github.com/user-attachments/assets/63aa5a76-51ae-4174-ad09-816c0a27f08b)


