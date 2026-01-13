import google.generativeai as genai
genai.configure(api_key="AIzaSyCxdJmsv3z4SSZxeNRqg-xwnkWC3K35utQ")
for m in genai.list_models():
    print(m.name)