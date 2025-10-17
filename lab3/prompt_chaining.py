import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from util import call_ollama

def analyze_text_chain(text):
    """Chain prompts to analyze text progressively."""
    
    # Step 1: Summarize
    summary_prompt = f"Summarize this in one sentence:\n\n{text}"
    summary = call_ollama(summary_prompt, temperature=0.3, num_predict=100)
    print("Step 1 - Summary:")
    print(summary)
    
    # Step 2: Extract key points from summary
    keypoints_prompt = f"List 3 key points from: {summary}"
    keypoints = call_ollama(keypoints_prompt, temperature=0.3)
    print("\nStep 2 - Key Points:")
    print(keypoints)
    
    # Step 3: Generate questions
    questions_prompt = f"Generate 2 questions someone might ask about:\n{keypoints}"
    questions = call_ollama(questions_prompt, temperature=0.5)
    print("\nStep 3 - Questions:")
    print(questions)
    
    return {
        'summary': summary,
        'keypoints': keypoints,
        'questions': questions
    }

# Test text
article = """
Artificial Intelligence (AI) is transforming healthcare in profound ways, with one of the most impactful changes emerging through digital diagnosis. Digital diagnosis refers to the use of AI algorithms and machine learning models to analyze patient data and provide clinical assessments, predictions, or alerts, often in real-time. This innovation is revolutionizing how medical conditions are detected, monitored, and treated by significantly enhancing speed, accuracy, and accessibility. Traditionally, diagnosis relied heavily on a physician's experience, time-consuming tests, and subjective interpretations, which could lead to delays, misdiagnoses, or inefficiencies in patient care. AI-driven digital diagnostic tools, however, can rapidly process massive datasets—such as electronic health records (EHRs), medical images, genetic data, and even patient speech or behavior patterns—to identify patterns and anomalies that might be invisible to the human eye. For instance, in radiology, AI systems can analyze X-rays, MRIs, and CT scans to detect diseases like cancer, pneumonia, or brain hemorrhages with a level of precision that rivals or even surpasses that of seasoned radiologists. Similarly, in pathology, AI tools can scan digital slides to detect malignant cells or predict cancer subtypes based on histological features, speeding up diagnosis and facilitating more targeted treatment. Furthermore, AI is also making strides in non-invasive diagnostics through wearable technology and mobile apps that continuously monitor patients' vital signs, glucose levels, heart rhythms, and more. These systems not only detect early warning signs but also alert both patients and providers, enabling preventative care and reducing hospital readmissions. In primary care, chatbots and virtual assistants powered by natural language processing are assisting in symptom checking, triaging patients, and even supporting mental health through cognitive behavioral therapy interfaces. This digital front-line diagnostic approach improves healthcare access, especially in underserved or remote regions where medical professionals may be scarce. Importantly, AI also personalizes diagnosis by incorporating genetic data, lifestyle factors, and treatment histories into risk prediction models, paving the way for precision medicine. For example, AI models can predict the likelihood of developing chronic diseases like diabetes or cardiovascular conditions long before symptoms appear, allowing for early interventions. However, this transformation also raises critical concerns, including data privacy, algorithmic bias, regulatory approval, and the need for transparency in AI decision-making processes. To ensure trust and safety, AI systems must be trained on diverse, high-quality data and must be validated rigorously against clinical standards. Despite these challenges, the benefits of AI in digital diagnosis are undeniable. It empowers clinicians with decision support tools, reduces diagnostic errors, streamlines workflows, and ultimately leads to better patient outcomes. As AI continues to evolve, its integration into healthcare promises a future where diagnosis is faster, smarter, and more equitable, fundamentally changing how we understand and manage health. By bridging technology with clinical expertise, digital diagnosis is not just an upgrade to traditional methods—it represents a paradigm shift in modern medicine, bringing us closer to a more responsive, predictive, and personalized healthcare system.
"""

print("Chained Analysis:\n" + "="*60 + "\n")
result = analyze_text_chain(article)