from guizero import App, Text, TextBox, PushButton, Window
from logic import store_user_info, analyzeInput, categorize, personalizedSupport, show_convo, communityConnect

user_database = {
    1: {"username": "john", "issue": "stress"},
    2: {"username": "alice", "issue": "purpose"},
    3: {"username": "bob", "issue": "relationships"},
    4: {"username": "mary", "issue": "faith"},
    5: {"username": "david", "issue": "stress"},
    6: {"username": "lisa", "issue": "purpose"},
    7: {"username": "mark", "issue": "relationships"},
}

current_user = {}

def login(app):
    """
    Opens a login window to allow existing users to log in.

    Parameters
    ----------
    app : App the main guizero object
        

    Operations:
    -------------
    - Prompts the user to input their username.
    - Validates the username against the existing user database.
    - If the username is valid, updates the current user session and redirects them to the issue submission window.
    - Displays error messages for invalid usernames or unexpected errors.
    """
    
    login_window = Window(app, title="Login", width=400, height=300)
    Text(login_window, text="Username:")
    username_box = TextBox(login_window, width=30)

    def handle_login():
        username = username_box.value.strip().lower()
        user = None
        for current_username in user_database.values():
            if current_username["username"] == username:
                user = current_username
                break
        if user:
            current_user.update(user)
            login_window.hide()
            Text(app, text=f"Welcome back, {username.capitalize()}!", color="green")
            submit_issue(app)
        else:
            Text(login_window, text="Username not found. Please sign up.", color="red")
            PushButton(login_window, text="Back", command=login_window.hide)

    PushButton(login_window, text="Login", command=handle_login)
    PushButton(login_window, text="Back", command=login_window.hide)


def signup(app):
    """
    Opens a sign-up window to allow new users to register.

    Parameters
    ----------
    app : App (the main guizero object)

    Operations:
    -------------
    - Prompts the user to create a username.
    - Validates the entered username.
    - If valid, stores the user in the user database with a unique ID.
    - Updates the current user session and redirects them to the issue submission window.
    - Displays error messages for invalid usernames or unexpected errors.
    """
    
    signup_window = Window(app, title="Sign Up", width=400, height=300)
    Text(signup_window, text="Choose a Username:")
    username_box = TextBox(signup_window, width=30)

    def handle_signup():
        username = username_box.value.strip().lower()
        if username:
            user_id = len(user_database) + 1
            user_database[user_id] = {"username": username, "issue": None}
            current_user.update({"id": user_id, "username": username})
            signup_window.hide()
            Text(app, text=f"Thank you for signing up, {username.capitalize()}!", color="green")
            submit_issue(app)
        else:
            Text(signup_window, text="Please enter a valid username.", color="red")
            PushButton(login_window, text="Back", command=login_window.hide)

    PushButton(signup_window, text="Sign Up", command=handle_signup)
    PushButton(signup_window, text="Back", command=signup_window.hide)


def submit_issue(app):
    """
    Opens a window for the user to describe their issue and receive categorized support,
    and suggests connecting to a community.

    Parameters
    ----------
    app : App (the main guizero object)

    Operations
    -------------
    - Prompts the user to describe how they're feeling.
    - Analyzes the user's input, extracts keywords, and categorizes their concern.
    - Displays the identified category and offers personalized support suggestions.
    - Suggests joining a relevant community and displays available options.
    - Handles invalid or empty inputs and displays appropriate error messages.
    """
    issue_window = Window(app, title="Describe Your Issue", width=500, height=400)
    Text(issue_window, text="Describe how you're feeling below:")
    issue_box = TextBox(issue_window, multiline=True, width=40, height=5)

    def handle_submit_issue():
        issue_text = issue_box.value.strip()
        if issue_text:
            analyzed_text = analyzeInput(issue_text)
            initial_category, _ = categorize(analyzed_text)
            current_user["issue"] = initial_category
            Text(issue_window, text=f"Your concern is categorized under: {initial_category.capitalize()}.", color="green")
            
            # Personalized support suggestions
            suggestions = personalizedSupport(initial_category)
            for suggestion in suggestions:
                Text(issue_window, text=f"- {suggestion}")
            
            # Community suggestions
            community_suggestions = show_community(initial_category)
            Text(issue_window, text="\nCommunity Connection Options:", color="purple", size=16)
            
            if community_suggestions:
                for group in community_suggestions:
                    Text(issue_window, text=f"- {group}")
                
                # Use the current user's id as the group_id
                group_id = current_user['id']
                
                # Add the button to join the community
                PushButton(issue_window, text="Join Community", command=lambda: show_convo_window(app, group_id=group_id))
            else:
                Text(issue_window, text="No community groups available at the moment. Please try again later.", color="red")

        else:
            Text(issue_window, text="Please enter a valid description of your issue.", color="red")

    # Submit and Exit buttons
    PushButton(issue_window, text="Submit", command=handle_submit_issue)
    PushButton(issue_window, text="Exit", command=issue_window.destroy)

    
def show_community(user_issue):
    """
    Provides a list of available community groups that address the given issue.

    Parameters
    -----------
    user_issue(str): describes the user's concern for the community

    Returns
    ---------
    list: A list of strings describing available community groups for the issue.
              If no groups are available, a message indicating this is returned.
    """
    available_groups = []  # Create a list to store available groups
    community_groups = communityConnect()  # Get all community groups
    for group in community_groups:
        if group['available'] and group['issues'] == user_issue:
            available_groups.append(f"Community for {user_issue} issue is available. Join now! Group ID: {group['id']}")
    
    if available_groups:
        return available_groups
    else:
        return ["No available community for this issue. Please try again later."]

def show_convo_window(app, group_id):
    """Displays the conversation for the selected community group."""
    convo_window = Window(app, title=f"Community Group {group_id} Conversation", width=500, height=400)
    convo = show_convo(group_id)
    
    Text(convo_window, text=f"Conversation in Group {group_id}:", size=14, color="green")
    for message in convo["conversation"]:
        Text(convo_window, text=f"{message['user']}: {message['message']}")

    Text(convo_window, text="Your message:", size=12, color="blue")
    message_box = TextBox(convo_window, width=40, height=3, multiline=True)

    def submit_message():
        """Handles the submission of a user's message to the conversation."""
        user_message = message_box.value.strip()
        if user_message:
            convo["conversation"].append({"user": current_user["username"], "message": user_message})
            Text(convo_window, text=f"Me: {user_message}", color="green")
            message_box.clear()

            Text(convo_window, text="It's nice to connect with you!", color="purple", size=12)
        else:
            Text(convo_window, text="Please enter a message.", color="red", size=12)

    PushButton(convo_window, text="Send Message", command=submit_message)
    PushButton(convo_window, text="Exit", command=convo_window.destroy)
    
    
def main():
    """
    Initializes and displays the main application window.

    Functionality
    -------------
    - Sets up the main interface with options for users to log in or sign up.
    - Opens corresponding windows based on the user's choice.
    - Entry point for the application.
    """
    app = App(title="Your Safe Haven", width=500, height=400)
    Text(app, text="Welcome to Your Safe Haven!", size=24,font= "Times Roman")
    Text(app, text= "Get Started!!", size= 24, font = "Times Roman")
    PushButton(app, text="Login", command=lambda: login(app))
    PushButton(app, text="Sign Up", command=lambda: signup(app))
    PushButton(app, text="Exit", command=app.destroy)
    app.display()

if __name__ == "__main__":
    main()

