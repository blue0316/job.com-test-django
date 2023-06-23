from tkinter import *
from tkinter.scrolledtext import ScrolledText
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample candidate data
candidates = [
    {
        "name": "Candidate 1",
        "skills": "python, machine learning, data analysis"
    },
    {
        "name": "Candidate 2",
        "skills": "java, software development, problem-solving"
    },
    {
        "name": "Candidate 3",
        "skills": "python, data science, statistics"
    }
]

# Sample job data
jobs = [
    {
        "title": "Data Scientist",
        "skills_required": "python, machine learning, data analysis, statistics"
    },
    {
        "title": "Software Engineer",
        "skills_required": "java, software development, problem-solving, teamwork"
    },
    {
        "title": "Data Analyst",
        "skills_required": "python, data analysis, statistics, SQL"
    }
]

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform candidate skills into feature vectors
candidate_skills = [candidate["skills"] for candidate in candidates]
candidate_vectors = vectorizer.fit_transform(candidate_skills)

# Create the GUI
def match_candidates():
    selected_job_index = job_listbox.curselection()
    if not selected_job_index:
        return
    
    selected_job = jobs[selected_job_index[0]]
    job_vector = vectorizer.transform([selected_job["skills_required"]])
    
    # Compute cosine similarity between job and candidate vectors
    similarities = cosine_similarity(job_vector, candidate_vectors).flatten()
    
    # Sort candidates based on similarity scores
    matched_candidates = sorted(zip(candidates, similarities), key=lambda x: x[1], reverse=True)
    
    # Display matched candidates in the checklist
    for checkbox in checkboxes:
        checkbox.destroy()
    checkboxes.clear()
    
    for i, (candidate, similarity) in enumerate(matched_candidates):
        var = IntVar()
        checkbox = Checkbutton(result_frame, text=f"{candidate['name']} (Similarity: {similarity:.2f})", variable=var)
        checkbox.pack(anchor=W)
        checkboxes.append(checkbox)
        checkbox_vars.append(var)

def accept_candidates():
    selected_candidates = [candidate for candidate, var in zip(candidates, checkbox_vars) if var.get() == 1]
    if selected_candidates:
        print("Accepted Candidates:")
        for candidate in selected_candidates:
            print(candidate["name"])
        print()

def deny_candidates():
    denied_candidates = [candidate for candidate, var in zip(candidates, checkbox_vars) if var.get() == 0]
    if denied_candidates:
        print("Denied Candidates:")
        for candidate in denied_candidates:
            print(candidate["name"])
        print()

def open_create_job_page():
    create_job_window = Toplevel(window)
    create_job_window.title("Create Job")
    create_job_window.geometry("300x200")
    
    # Create the job creation form
    job_title_label = Label(create_job_window, text="Job Title:")
    job_title_label.pack()
    job_title_entry = Entry(create_job_window)
    job_title_entry.pack()

    job_skills_label = Label(create_job_window, text="Skills Required:")
    job_skills_label.pack()
    job_skills_entry = Entry(create_job_window)
    job_skills_entry.pack()

    def create_job():
        title = job_title_entry.get()
        skills_required = job_skills_entry.get()

        if title and skills_required:
            new_job = {"title": title, "skills_required": skills_required}
            jobs.append(new_job)
            job_listbox.insert(END, title)
            create_job_window.destroy()
    
    create_job_button = Button(create_job_window, text="Create Job", command=create_job)
    create_job_button.pack()

def open_create_candidate_page():
    create_candidate_window = Toplevel(window)
    create_candidate_window.title("Create Candidate")
    create_candidate_window.geometry("300x200")
    
    # Create the candidate creation form
    candidate_name_label = Label(create_candidate_window, text="Candidate Name:")
    candidate_name_label.pack()
    candidate_name_entry = Entry(create_candidate_window)
    candidate_name_entry.pack()

    candidate_skills_label = Label(create_candidate_window, text="Skills:")
    candidate_skills_label.pack()
    candidate_skills_entry = Entry(create_candidate_window)
    candidate_skills_entry.pack()

    def create_candidate():
        name = candidate_name_entry.get()
        skills = candidate_skills_entry.get()

        if name and skills:
            new_candidate = {"name": name, "skills": skills}
            candidates.append(new_candidate)
            create_candidate_window.destroy()
    
    create_candidate_button = Button(create_candidate_window, text="Create Candidate", command=create_candidate)
    create_candidate_button.pack()

# Create the GUI window
window = Tk()
window.title("Candidate Matching")
window.geometry("400x400")

# Create a list box to display jobs
job_listbox = Listbox(window, selectmode=SINGLE)
for job in jobs:
    job_listbox.insert(END, job["title"])
job_listbox.pack(pady=10)

# Create a button to match candidates
match_button = Button(window, text="Match Candidates", command=match_candidates)
match_button.pack(pady=10)

# Create a frame for displaying matched candidates
result_frame = Frame(window)
result_frame.pack(pady=10)

# Create a checklist for accepting candidates
checkboxes = []
checkbox_vars = []

# Create an "Accept" button
accept_button = Button(window, text="Accept", command=accept_candidates)
accept_button.pack(side=LEFT, padx=5)

# Create a "Deny" button
deny_button = Button(window, text="Deny", command=deny_candidates)
deny_button.pack(side=LEFT, padx=5)

# Create a menu
menu = Menu(window)
window.config(menu=menu)

# Create a "File" submenu
file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)

# Add options to the "File" submenu
file_menu.add_command(label="Create Job", command=open_create_job_page)
file_menu.add_command(label="Create Candidate", command=open_create_candidate_page)

# Start the GUI event loop
window.mainloop()
