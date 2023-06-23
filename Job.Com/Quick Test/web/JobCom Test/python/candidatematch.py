import tkinter as tk

# Sample data - candidates and jobs with skills
candidates = [
    {"name": "Candidate 1", "skills": ["Python", "Java", "SQL"]},
    {"name": "Candidate 2", "skills": ["Python", "JavaScript", "HTML"]},
    {"name": "Candidate 3", "skills": ["Java", "C++", "Python"]},
]

jobs = [
    {"title": "Job 1", "skills_required": ["Python", "SQL", "JavaScript"]},
    {"title": "Job 2", "skills_required": ["Java", "C++", "HTML"]},
    {"title": "Job 3", "skills_required": ["Python", "JavaScript", "CSS"]},
]


def match_candidates():
    selected_job = job_listbox.get(tk.ACTIVE)
    matched_candidates = []

    # Find candidates who have matching skills
    for candidate in candidates:
        if set(candidate["skills"]).issuperset(selected_job["skills_required"]):
            matched_candidates.append(candidate["name"])

    # Display the matched candidates in the result label
    result_label.config(text=", ".join(matched_candidates))


# Create the main window
window = tk.Tk()
window.title("Candidate Matching")

# Create the job listbox
job_listbox = tk.Listbox(window, width=50)
job_listbox.pack()

# Populate the job listbox with job titles
for job in jobs:
    job_listbox.insert(tk.END, job["title"])

# Create the button to match candidates
match_button = tk.Button(window, text="Match Candidates", command=match_candidates)
match_button.pack()

# Create the label to display the matched candidates
result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI event loop
window.mainloop()
