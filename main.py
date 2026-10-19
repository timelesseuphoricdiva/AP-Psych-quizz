import random


questions = [

    {

        "question": "Which means 'disruption of the circadian rhythm'",
        "options": ["A. Shift Work", "B. Insomnia", "C. Reflex Arc"],
        "answer": "A",
        "explanation": "Shift work is a disruption of the Circadian Rhythm"

    },

    {
        "question": "Which process describes when a neuron becomes less negative, leading to firing? ",
        "options": ["A. Reuptake", "B. Depolarization", "C. All-or-nothing principle"],
        "answer": "B",
        "explanation": "Depolarization is when a neuron's charge becomes less negative, leading to firing"

             },

    {
        "question": "Which process describes when the excitatory signals outweigh the inhibitory signals by a certain amount, and the neuron fires? ",
        "options": ["A. Threshold", "B. Multiple Sclerosis", "C. Dopamine"],
        "answer": "A",
        "explanation": "Threshold means 'when the excitatory signals outweigh the inhibitory signals by a certain amount, the neuron fires'"

    },

    {
        "question": "What is multiple sclerosis? ",
        "options": ["A. A neurotransmitter involved in sleep", "B. an autoimmune disorder where acetylcholine receptors are attacked", "C. When the myelin sheath is damaged"],
        "answer": "C",
        "explanation": "In multiple sclerosis, the myelin sheath is damaged, slowing down or blocking signals"


    },

    {
        "question": "Which Neurotransmitter arouses alertness and energy? ",
        "options": ["A. Norepinephrine",
                    "B. Glutamate",
                    "C. GABA"],
        "answer": "A",
        "explanation": "Norepinephrine arouses alertness and energy"

    },

    {
        "question": "Which hormone regulates hunger and fat storage ",
        "options": ["A. Oxytocin",
                    "B. Ghrelin",
                    "C. Leptin"],
        "answer": "C",
        "explanation": "Leptin regulates hunger and fat storage (Ghrelin makes you hungry)"

    },

    {
        "question": "Which lobes are located on the sides of the brain? ",
        "options": ["A. Frontal Lobes",
                    "B. Temporal Lobes",
                    "C. Occipital Lobes"],
        "answer": "B",
        "explanation": "Temporal lobes are located on the sides of the brain; these lobes process auditory information and handle language comprehension"

    },

    {
        "question": "What is the pituitary gland responsible for? ",
        "options": ["A. Releasing hormones that regulate growth ",
                    "B. Major drives, such as thirst and hunger",
                    "C. Balance and Voluntary movements"],
        "answer": "A",
        "explanation": "The Pituitary gland is the brain's master gland; it releases hormones that regulate growth and other essential processes"




    },

    {
        "question": "What type of drugs cause distortions in perception and/or cognition",
        "options": ["A. Opioids ",
                    "B. Depressants",
                    "C. Hallucinogens"],
        "answer": "C",
        "explanation": "Hallucinogens cause distortions in perception and/or cognition"

    },

    {
        "question": "What does the Reticular Activating System control? ",
        "options": ["A. sleep/wake cycles, alertness, and voluntary movements ",
                    "B. hearing, fight-or-flight reaction, and eating ",
                    "C. releasing hormones, involuntary movements, and breathing"],
        "answer": "A",
        "explanation": "The Reticular Activating System controls sleep/wake cycles, alertness, and voluntary movements; without it, you wouldn't be able to stay awake"



    },

    {
        "question": "What is the Somatosensory Cortex responsible for ",
        "options": ["A. making sense of visual stimuli ",
                    "B. distinguishing between different smells",
                    "C. feeling textures and temperatures"],
        "answer": "C",
        "explanation": "The Somatosensory Cortex is in the parietal lobes; helps you feel textures and temperatures"


    },

    {
        "question": "Which lobes handle linguistic processing ",
        "options": ["A. Parietal Lobes",
                    "B. Temporal Lobes",
                    "C. Occipital Lobes"],
        "answer": "B",
        "explanation": "Linguistic Processing is handled by the Temporal Lobes"

    },

    {
        "question": "What does the motor cortex do? ",
        "options": ["A. Control muscle movement",
                    "B. Control breathing",
                    "C. Control brain function"],
        "answer": "A",
        "explanation": "The motor cortex is located at the back of the frontal lobes and controls muscle movement"

    },

]


print("=" * 35)
print("       AP Psych Study")
print("   A mini ap psych quiz")
print("=" * 35)


random.shuffle(questions)
score = 0

for number, question in enumerate(questions, start=1):
    print(f"\nQuestion {number}: {question['question']}")

    for option in question["options"]:
        print(option)

    answer = input("Your answer (A/B/C): ").strip().upper()

    if answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Not quite! The answer was {question['answer']}.")

    print(question["explanation"])


print(f"Final score: {score}/{len(questions)}")
print("Thanks for playing!")

