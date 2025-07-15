import requests
import public_ip as ip
import platform 
if __name__ == "__main__":
    webhook_url = ''  # paste your webhook URL here

    output = "✅ Script finished successfully!"
    public_ip = ip.get()
    machine = "OS Name: " + platform.system() + '\n' + "OS Version: " + platform.platform()


    data = {
    "content": f"{output}\n{public_ip}\n{machine}"  
    }

    response = requests.post(webhook_url, json=data)

    if response.status_code == 204:
        print("Message sent to Discord!")
    else:
        print(f"Failed to send message: {response.status_code}")

