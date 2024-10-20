# imagedownloader

Streamlit Image Downloader and Email Sender 

A simple web app that lets users search, download, zip, and email images based on a search query. Built using Python, Streamlit, SerpAPI, and smtplib.

This Streamlit-based app allows users to search and download images from Google, compress them into a ZIP file, and send the images via email. Users can easily interact with the app through an intuitive interface that requires minimal input.



Requirements
To run this app locally, you will need:

Python 3.x

Required Python libraries:

Streamlit
SerpAPI (pip install serpapi)
Requests
smtplib (built-in)
zipfile (built-in)

The interface is designed for simplicity and ease of use. The sidebar contains the following input fields:

Search Query: Enter the object or term to search for images.
Number of Images: Specify the number of images to download (default is 5, maximum is 50).
Recipient Email: Input the email address where the zip file of images will be sent.
Once the inputs are provided, the user clicks the "Download and Send Images" button, triggering the download and email functions.

![Screenshot 2024-10-21 034811](https://github.com/user-attachments/assets/c6e4574c-3a2d-4d1f-9f79-8b12cff4bb18)

Key Interface Elements:
Custom Styling: The app uses custom CSS to enhance its appearance.
Progress Bar: A progress bar is shown to indicate the status of image downloading and sending.


![Screenshot 2024-10-21 034856](https://github.com/user-attachments/assets/bbfefcd6-2003-4248-a7eb-4125a5ea7086)
![Screenshot 2024-10-21 034933](https://github.com/user-attachments/assets/b3c6ee23-4f42-4e5d-bc64-a4b144ae7f2f)

WORKING OF THE CODE:

Image Search and Download:

The app uses SerpAPI to search for images based on the user’s input.
Images are then downloaded to a folder named "images."
The app ensures the folder is cleared after each search, preventing old images from being included in subsequent downloads.

Zipping the Images:

After downloading the images, they are compressed into a single ZIP file using the Python zipfile module.

Email Sending:

Using the smtplib library, the app sends the ZIP file as an attachment to the recipient’s email. The sender’s email and app password are hardcoded for simplicity.


![Screenshot 2024-10-21 035020](https://github.com/user-attachments/assets/63aa5a76-51ae-4174-ad09-816c0a27f08b)


