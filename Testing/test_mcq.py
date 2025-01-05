from mcq_generation import generate_mcq

sample_text = "Artificial Intelligence and its impact on modern healthcare."

mcqs = generate_mcq(sample_text, None)

# Print the generated MCQs
print("Generated MCQs:")
print(mcqs)
