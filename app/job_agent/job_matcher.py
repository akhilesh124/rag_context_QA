from sentence_transformers import SentenceTransformer, util
import json

model = SentenceTransformer("all-MiniLM-L6-v2")

class JobMatcher:
    def __init__(self, resume_path):
        with open(resume_path) as f:
            self.resume = json.load(f)
        self.resume_text = " ".join(self.resume["skills"])

    def match(self, job_text):
        emb1 = model.encode(self.resume_text, convert_to_tensor=True)
        emb2 = model.encode(job_text, convert_to_tensor=True)
        score = util.cos_sim(emb1, emb2).item()
        return round(score, 2)
