import streamlit as st
import subprocess
import os
import time

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return True, result.stdout.strip()
        else:
            return False, result.stderr.strip()
    except Exception as e:
        return False, str(e)

def list_sessions(session_port):
    # Combine commands to execute in one go
    command = f"tmux send-keys -t handler-{session_port} 'spool sessions.txt' Enter && tmux send-keys -t handler-{session_port} 'sessions -l' Enter && tmux send-keys -t handler-{session_port} 'spool off' Enter"
    # Execute the combined commands
    success, _ = execute_command(command)
    if success:
        # Wait for sessions.txt to be created
        timeout = 10  # Timeout in seconds
        start_time = time.time()
        while not os.path.exists("sessions.txt"):
            if time.time() - start_time > timeout:
                return "Timed out waiting for sessions.txt to be created."
            time.sleep(0.5)  # Check every 0.5 seconds

        # Read the contents of sessions.txt
        with open("sessions.txt", 'r') as file:
            output = file.readlines()[3:-3]
            output = ''.join(output)
        # Remove the sessions.txt file
        execute_command("rm sessions.txt")
        return output
    else:
        return "Failed to list sessions. Please check the session port and try again."

def main():
    st.title("List Active Sessions")
    session_port = st.text_input("Enter session port:", "8080")

    if st.button("List Sessions"):
        output = list_sessions(session_port)
        st.code(output)

if __name__ == "__main__":
    main()
