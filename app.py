from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

# In-memory to-do list (will reset when the app restarts)
todo_list = []

@app.route('/')
def home():
    return "Welcome to your To-Do List App!"

@app.route('/sms', methods=['POST'])
def sms_reply():
    incoming_msg = request.form.get('Body')
    response = MessagingResponse()

    if incoming_msg.lower().startswith("add:"):
        # Add a task
        task = incoming_msg[4:].strip()
        if task:
            todo_list.append(task)
            response.message(f"Task added: {task}")
        else:
            response.message("Please specify a task to add. Format: Add: [Task Name]")
    
    elif incoming_msg.lower() == "list":
        # List all tasks
        if todo_list:
            tasks = "\n".join([f"{i+1}. {task}" for i, task in enumerate(todo_list)])
            response.message(f"Your To-Do List:\n{tasks}")
        else:
            response.message("Your to-do list is empty. Add a task using 'Add: [Task Name]'.")
    
    elif incoming_msg.lower().startswith("done:"):
        # Remove a task
        task_to_remove = incoming_msg[5:].strip()
        if task_to_remove in todo_list:
            todo_list.remove(task_to_remove)
            response.message(f"Task removed: {task_to_remove}")
        else:
            response.message("Task not found in your to-do list.")
    
    else:
        # Default response
        response.message("To use this app:\n- Add a task: Add: [Task Name]\n- View tasks: List\n- Mark task as done: Done: [Task Name]")

    print("Current To-Do List:", todo_list)  # Log the current tasks in the terminal
    return str(response)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
