import random

def My_bot(prompt):
    greetings = ['hi', 'hello', 'hey']
    responses = ['How can I help you today?', 'I am here to help!', 'Nice to meet you!', 'Hello there!']
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
