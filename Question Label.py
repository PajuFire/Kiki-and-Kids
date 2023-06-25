keywords = {
    "linear_equations": ["slope", "y-intercept", "linear", "equation", "line", "parallel", "perpendicular"],
    "systems_of_equations": ["system of equations", "simultaneous equations", "substitution", "elimination"],
    "ratios_and_proportions": ["ratio", "proportion", "directly proportional", "inversely proportional"],
    "percentages": ["percent", "%", "percentage", "increase", "decrease"],
    "exponential_growth_decay": ["exponential", "growth", "decay", "compounded", "doubles", "halves"],
    "quadratic_equations": ["quadratic", "parabola", "vertex", "roots", "solutions", "discriminant"],
    "polynomials": ["polynomial", "degree", "term", "coefficient", "factor", "expand"],
    "geometry": ["angle", "triangle", "rectangle", "circle", "area", "perimeter", "volume", "Pythagorean"],
    "trigonometry": ["sine", "cosine", "tangent", "sin", "cos", "tan", "trigonometry", "angle", "right triangle"],
    "statistics": ["mean", "median", "mode", "range", "standard deviation", "probability", "data", "average"],
    "functions": ["function", "domain", "range", "inverse", "composition", "graph"],
    "complex_numbers": ["complex number", "imaginary", "real part", "imaginary part"],
}

# Initialize an empty dictionary to store the results
results = {}

# Open and read the text file
with open('your_file.txt', 'r') as file:
    for line in file:
        # If the line is a question number, remember it
        if line.strip().isdigit():
            question_number = int(line.strip())
            results[question_number] = {"question": question_number, "topics": {}}
        # Otherwise, check if the line contains any of the keywords
        elif question_number is not None:
            for topic, topic_keywords in keywords.items():
                for keyword in topic_keywords:
                    if keyword in line:
                        # If it does, increment the count for the topic in the results for the current question
                        if topic not in results[question_number]["topics"]:
                            results[question_number]["topics"][topic] = 0
                        results[question_number]["topics"][topic] += 1

# For each question, find the topic with the most matches and label the question with that topic
for question, info in results.items():
    max_topic = max(info["topics"], key=info["topics"].get)
    print(f"Question {info['question']} is about the topic '{max_topic}'.")

# Print the results
for question, info in results.items():
    print(f"Question {info['question']} is about the topic '{info['topic']}'.")