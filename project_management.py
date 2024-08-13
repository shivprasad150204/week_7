from project import Project
import datetime

def main():
    projects = load_projects("projects.txt")
    display_menu()
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'l':
            filename = input("Filename to load from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename to save to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        display_menu()
        choice = input(">>> ").lower()
    print("Thank you for using the project management software.")

def load_projects(filename):
    """Load projects from a file."""
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # Skip the header
        for line in file:
            parts = line.strip().split('\t')
            name, start_date, priority, cost_estimate, completion = parts
            project = Project(name, start_date, int(priority), float(cost_estimate), int(completion))
            projects.append(project)
    return projects

def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion}\n")

def display_projects(projects):
    """Display all projects, separated by completion status."""
    incomplete = [project for project in projects if project.completion < 100]
    complete = [project for project in projects if project.completion == 100]
    print("Incomplete projects:")
    for project in sorted(incomplete, key=lambda x: x.priority):
        print(project)
    print("Completed projects:")
    for project in complete:
        print(project)

def filter_projects_by_date(projects):
    """Filter projects by a start date."""
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered = [project for project in projects if datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date() > date]
    for project in filtered:
        print(project)

def add_new_project(projects):
    """Add a new project to the list."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost_estimate, completion)
    projects.append(project)

def update_project(projects):
    """Update an existing project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    project = projects[project_choice]
    new_completion = input("New Percentage: ")
    if new_completion:
        project.completion = int(new_completion)
    new_priority = input("New Priority: ")
    if new_priority:
        project.priority = int(new_priority)

def display_menu():
    """Display the menu options."""
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")

if __name__ == "__main__":
    main()
