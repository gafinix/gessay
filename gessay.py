import openai

# Set up OpenAI API key (You need to have an OpenAI account and use your own API key)
openai.api_key = "YOUR_API_KEY"

def generate_outline(topic):
    # Function to generate an outline based on the essay topic using GPT model
    prompt = f"Create an outline for an essay on the topic: {topic}. Include introduction, body paragraphs, and conclusion."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )
    outline = response.choices[0].text.strip()
    return outline

def generate_section(section_title, topic):
    # Function to generate a specific section of the essay (introduction, body, conclusion)
    prompt = f"Write a {section_title} for an essay on the topic: {topic}. Be detailed and informative."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=250,
        n=1,
        stop=None,
        temperature=0.7
    )
    section_text = response.choices[0].text.strip()
    return section_text

def write_essay():
    print("Welcome to the Essay Writing Assistant!")

    # Get essay topic from user
    topic = input("Enter the topic for your essay: ")

    # Generate an outline based on the topic
    print("\nGenerating essay outline...")
    outline = generate_outline(topic)
    print(f"\nEssay Outline:\n{outline}\n")
    
    # Ask user for the structure they want to write (Introduction, Body, Conclusion)
    sections = ["Introduction", "Body", "Conclusion"]
    essay_parts = {}

    for section in sections:
        print(f"\nWriting {section}...")
        section_text = generate_section(section, topic)
        essay_parts[section] = section_text
        print(f"\n{section}:\n{section_text}\n")

    # Combine all parts to form the full essay
    essay = "\n".join([essay_parts[section] for section in sections])
    
    # Display the final essay
    print("\nFinal Essay:")
    print(essay)

    # Option to save the essay to a text file
    save = input("\nWould you like to save your essay to a file? (yes/no): ")
    if save.lower() == "yes":
        filename = input("Enter the filename (without extension): ")
        with open(f"{filename}.txt", "w") as file:
            file.write(essay)
        print(f"Essay saved as {filename}.txt")

if __name__ == "__main__":
    write_essay()
