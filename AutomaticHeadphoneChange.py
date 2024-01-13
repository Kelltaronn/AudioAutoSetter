# Repo:
# https://github.com/frgnca/AudioDeviceCmdlets
import subprocess
import re

script = "(Get-AudioDevice -List | Where-Object { $_.Type -eq 'Playback' -and $_.Name -eq 'Speakers (High Definition Audio Device)' }).Default"

def run_powershell_script(script):
    try:
        # Start PowerShell process
        process = subprocess.Popen(["powershell.exe", "-Command", "-"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Send the script to PowerShell
        process.stdin.write(script)
        process.stdin.close()

        # Get the output
        output, error = process.communicate()

        # Print the output and error, if any
        # print("Output:", output)
        # print("Error:", error)

    except Exception as e:
        print("An error occurred:", e)

    return output

def make_it_switch(speaker_state):
    if speaker_state == "True\n":
        switch_script = "Set-AudioDevice -ID '{0.0.0.00000000}.{8ea3557e-6a5f-4899-8eb4-860e0a50aa35}'"
    elif speaker_state == "False\n":
        switch_script = "Set-AudioDevice -ID '{0.0.0.00000000}.{0945f80b-3dab-4fcf-94be-cd2461b3e3fb}'"
    

    process = subprocess.Popen(["powershell.exe", "-Command", "-"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Send the script to PowerShell
    process.stdin.write(switch_script)
    process.stdin.close()

    output, error = process.communicate()
    # print("Output:", output)
    # print("Error:", error)



make_it_switch(run_powershell_script(script))



