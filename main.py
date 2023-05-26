import openai
import os

# Step 0: Remember to set your API key through an environment variable with the syntax below.
# openai.api_key = os.getenv("api_key")



def get_completion(course_name, student_name, adjectives, areas_for_improvement):
    openai.api_key = os.getenv("api_key")
    prompt = """Write a two paragraph grade narrative in the second person for a """+course_name+"""course for a high school student  that incorporates the adjectives and test scores provided, and provides suggestions for growth as shown.

Name:  Steven
Adjectives:  clever, diligent, tardy
Suggestions: come to class on time, work on debugging, asking more questions
Response:  Steven, you have made excellent progress in class this year.  You did some clever coding, and were diligent with completing assignments.  You have displayed a good ability for debugging and solving problems. However, you should work on asking more questions in class and taking on more challenging projects. You have also been tardy to several classes, which is something you should strive to improve on in the future. Keep up the hard work and keep pushing yourself to do better!
    
Name: """+student_name+"""
Adjectives: """+adjectives+"""
Suggestions: """+areas_for_improvement+"""
Response: """
    # openai.api_key = os.getenv("api_key")
    # Also check out the EDIT endpoint
    # https://beta.openai.com/docs/api-reference/edits
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=400,
        top_p=1,
        # positive values decrease likelihood to repeat same line
        # value range -2, 2
        frequency_penalty=.5,
        # positive values decrease likelihood to repeat same topic
        # value range -2, 2
        presence_penalty=0
    )
    print(response)
    return response.choices[0].text


def get_prompt_response(prompt, temp=0.7, max_tokens=300):
    openai.api_key = os.getenv("api_key")
    # Also check out the EDIT endpoint
    # https://beta.openai.com/docs/api-reference/edits
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=float(temp),
        max_tokens=int(max_tokens),
        top_p=1,
        # positive values decrease likelihood to repeat same line
        # value range -2, 2
        frequency_penalty=.5,
        # positive values decrease likelihood to repeat same topic
        # value range -2, 2
        presence_penalty=0
    )
    print(response)
    return response.choices[0].text


if __name__ == '__main__':
    test_response = get_completion("Write lyrics for a rock ballad about Perry the Platypus and his adventure through the volcano of doom.")
    print(test_response)