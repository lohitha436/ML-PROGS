# FIND-S Algorithm Implementation

# Given training dataset
training_data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

# Number of attributes (excluding target)
num_attributes = len(training_data[0]) - 1

# Step 1: Initialize hypothesis with the most specific hypothesis
hypothesis = ['0'] * num_attributes

print("Initial Hypothesis:")
print(hypothesis)

# Step 2: Apply FIND-S algorithm
for example in training_data:
    if example[-1] == 'Yes':   # Consider only positive examples
        for i in range(num_attributes):
            if hypothesis[i] == '0':
                hypothesis[i] = example[i]
            elif hypothesis[i] != example[i]:
                hypothesis[i] = '?'
   
    print("\nTraining Example:", example)
    print("Updated Hypothesis:", hypothesis)

# Step 3: Final hypothesis
print("\nFinal Most Specific Hypothesis:")
print(hypothesis)

