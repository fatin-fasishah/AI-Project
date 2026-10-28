from datetime import datetime
import pytz

while True:
    # 1. Ask for user input
    user = input("Hi! Tanya la apa-apa? (or type 'bye' to quit): ")
    
    # 2. Check if the user wants to leave
    if user.lower() == "exit":
        print("Goodbye!")
        break
        
    # 3. Check for keywords in the user's message
    if any(keyword in user.lower() for keyword in ["weather", "cuaca"]):
        print("The weather today is sunny!")
        
    elif "time" in user.lower():
        local_tz = pytz.timezone("Asia/Kuala_Lumpur")
        current_time = datetime.now(local_tz)
        # Using flush=True forces Python to print immediately to the terminal
        print("The time is", current_time, flush=True)

    elif any(keyword in user.lower() for keyword in ["makan", "mamam", "lunch", "dinner"]):
        print("Ayam gepuk set A!")
        
    else:
        print("Sorry, I don't understand.")