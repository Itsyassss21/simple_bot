import random
# @itzyassss21
def My_bot(prompt):
    greetings = ["Hello",  "Good morning",  "Hey","Hi","Can you help me with a programming problem?", "I need information about your products.", "I'm feeling a bit lost, can you offer some guidance?","I have a question about your services." , " Can you tell me a joke? "]
    responses = [ "Hi there! How can I assist you today?", "Good morning! What can I help you with?",  "Hey! What brings you here today?", 'Hello there!', "Of course! I'd be happy to help with your programming issue. Please provide me with the details.","Sure thing! I can provide you with details about our products. What specifically are you looking for?","I'm here to help! Let's talk about what's on your mind and see how I can support you.", "Ask away! I'm here to answer any questions you have about our services.", "Sure, here's a joke for you: Why don't skeletons fight each other? They don't have the guts!"]
    responses_no_answer = ['Sorry, I am unable to answer that question.', 'I am not sure how to help with that.', 'I cannot answer that.', 'I am unable to help with that topic.']
    stop_phrases = ['bye', 'goodbye', 'see you']

    # Split prompt into list of words
    words = prompt.lower().split()
    # Check if prompt contains a greeting
    if any(word in words for word in greetings):
        return random.choice(responses)

    # Check if prompt contains a stop phrase
    if any(word in words for word in stop_phrases):
        return random.choice(stop_phrases)

    # Check if prompt requires an answer
    if '?' in prompt:
        return random.choice(responses_no_answer)

    # Default response if none of the above conditions are met
    return random.choice(responses)

user_input = ""
while user_input.lower() != "bye":
    user_input = input("You: ")
    bot_response = My_bot(user_input)
    print("Bot:", bot_response)
