# from browser_agent import BrowserAgent
# from job_matcher import JobMatcher
# from form_filler import FormFiller
# from approval import approve
# import json

# def main():
#     browser = BrowserAgent()
#     matcher = JobMatcher("resume.json")

#     browser.open_site("https://jobs.lever.co")

#     browser.search_jobs("Backend Developer")

#     jobs = browser.extract_jobs()

#     with open("resume.json") as f:
#         resume = json.load(f)

#     for job in jobs:
#         browser.open_job(job["link"])

#         job_text = browser.page.inner_text("body")
#         score = matcher.match(job_text)

#         if score < 0.6:
#             print("❌ Skipping low relevance")
#             continue

#         if approve(job, score):
#             filler = FormFiller(browser.page, resume)
#             filler.fill()
#             print("🛑 Form filled. Please review manually.")
#             input("Press ENTER to submit manually...")
#         else:
#             print("⏭ Skipped")

#     browser.close()

# if __name__ == "__main__":
#     main()




from browser_agent import BrowserAgent
from job_matcher import extract_jobs, match_jobs
from approval import get_approval
from form_filler import fill_application
import json
import time
import os

# --- Step 0: Load your resume skills ---
resume_file = os.path.join(os.path.dirname(__file__), "resume.json")
with open(resume_file, "r") as f:
    resume = json.load(f)
skills = resume.get("skills", [])
print(f"Loaded skills from resume: {skills}")

# --- Step 1: Start browser ---
browser = BrowserAgent()

# --- Step 2: Open Naukri job search page ---
search_url = "https://www.naukri.com/jobs?q=Node.js+Developer&l="
browser.open_site(search_url)

# Give page some time to fully load
print("Loading jobs...")
time.sleep(5)

# --- Step 3: Extract jobs from page ---
jobs = extract_jobs(browser.page)
print(f"Found {len(jobs)} jobs on page.")

# --- Step 4: Match jobs with your skills ---
matched_jobs = match_jobs(jobs, skills)
print(f"{len(matched_jobs)} jobs matched your skills.")

# --- Step 5: Approval & apply loop ---
for job in matched_jobs:
    if get_approval(job):
        print(f"Applying to: {job['title']} - {job['company']}")
        fill_application(browser.page, job['link'])
        time.sleep(2)  # small delay to avoid being too fast
    else:
        print(f"Skipped: {job['title']} - {job['company']}")

# --- Step 6: Keep browser open for inspection ---
print("All done. Browser will stay open. Press Ctrl+C to exit and close browser.")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Closing browser...")
    browser.close()
