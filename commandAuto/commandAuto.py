import argparse
import requests
import subprocess;

def get_ollama_response(prompt):
    # URL and port where Ollama is running
    url = "http://localhost:11434/api/generate"  # replace with actual port
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "prompt": prompt,
        "model": "codellama",
        "format":"json",
        "stream": False

    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json().get("response", "No response")
    else:
        return "Error connecting to Ollama"

for i in range(0,1):
    path="C:/Users/91875/VScode/reactNative/testapp/app"
    query=input("Enter query ");
    prompt="write bash commands that "+query+". at location "+path;
    res=get_ollama_response(prompt);
    print(res);
