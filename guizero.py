from textblob import TextBlob

keywordCategories = {
    "stress": ["overwhelmed", "burnout", "anxious", "exhausted"],
    "purpose": ["confused", "unmotivated", "directionless"],
    "relationships": ["lonely", "disconnected", "isolated", "friendship"],
    "faith": ["hopeless", "spiritual", "faith", "purposeful"]
}

userInfo = {} 


def analyzeInput(text):
    """analyzes the input using TextBlob to understand the emotional tone of the input
       Parameters
       ----------
       text: str
    
       Returns
       ---------
       analyzed_text: list of keywords
    """
    blob = TextBlob(text)
    for word in blob.words:
        keywords = word.lower()
    return keywords


def detectingKeywords(categ_text):
    """Identifying specific phrases or keywords related to "stress", "purpose" and more
       Parameters
       -----------
       categ_text: str
        
       Returns
       -------
       categoryDict : dictionary that maps the categories to the given keywords
    """
    categoryDict = {}
    categoryList = []
    for word in categ_text:
        for keywords in keywordCategories.items():
            if word in keywords:
                categoryDict(categoryList).append(word)
    return categoryDict


def categorize(analyzed_text):
    """maps the processed text to a category using a keyword matching
       Parameters
       -----------
       analyzed_text: str
    
       Returns
       --------
       category: string representing the category
    
       Calls
       ------
       def detectingKeywords
     """

    # Initialize variables to track the initial category of the user
    initialCategory = None
    max_length = 0

    try:
        user_category = detectingKeywords(analyzed_text)
        if not user_category:
            raise ValueError("No matching categories found.")
        
        # Loop through each category and its word list in the dictionary
        for category, words in user_category.items():
            # Check if the current category has more words than the current max
            if len(words) > max_length:
                initialCategory = category  
                max_length = len(words)      
        return initialCategory, user_category

    except ValueError as error:
        return str(error), {}



def personalizedSupport(user_categ):
    """Offer personalized support depending on the user's identified issues
       Parameters
       -----------
       user_categ: str
    
       Returns
       --------
       support_response: a list of ideas for the specific issue
    """
    support_responses = {
        "stress": ["Take deep breaths", "Consider mindfulness exercises", "Seek counseling resources."],
        "purpose": ["Explore your interests", "Consider journaling your goals", "Talk with a career mentor."],
        "relationships": ["Reach out to a trusted friend", "Join a community group", "Consider professional advice."],
        "faith": ["Explore spiritual practices", "Engage with a faith community", "Seek meaning through prayer or meditation."]
    }
    return support_responses.get(user_categ, ["We are here for you. Explore our community support options."])


def communityConnect():
    """Connects user with a safe network of peers
       Parameters
       -----------
       user_id: int
    
       Returns
       --------
       profiles: list describing their ids and issues and if available to connect
    """

    return [
        {"id": 1, "issues": "stress", "available": True},
        {"id": 2, "issues": "purpose", "available": True},
        {"id": 3, "issues": "relationships", "available": False},
    ]


def process_user_input():
    """
       Process user input from the input box and uses the analyzeInput function
       Parameters
       -----------
       None
       Return
       -------
       Raises an error when there's an invalid input and clears the support list section
       
    """
    
    try:
        user_text = input_box.value
        analyzed_text = analyzeInput(user_text)
        initial_category, _ = categorize(analyzed_text)

        category_label.value = f"Your concern is categorized under: {initial_category.capitalize()}."
        support_messages = personalizedSupport(initial_category)

        support_list.clear()
        for message in support_messages:
            support_list.append(message)
    except ValueError as error:
        category_label.value = str(error)
        support_list.clear()

def show_community():
    """
       Shows a window of communities for connection with ids, issues and availability
       Parameters
       ----------
       None
       If the availability light is on, then they can communicate
    """
    pass