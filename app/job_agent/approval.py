def approve(job, score):
    print("\n===========================")
    print("JOB TITLE:", job["title"])
    print("MATCH SCORE:", score)
    choice = input("Apply? (y/n): ")
    return choice.lower() == "y"
