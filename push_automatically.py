import os

from dotenv import load_dotenv


class GitProject:
    def __init__(self, project_directory, name_github, token_github):
        self.project_directory = project_directory
        self.repository_name = os.path.basename(self.project_directory)
        self.name_github = name_github
        self.token_github = token_github

    def add(self):
        os.chdir(self.project_directory)
        os.system("git add .")

    def status(self):
        os.system("git status")

    def commit(self, commit_description):
        os.system(f'git commit -m "{commit_description}"')
        print('\n')

    def push(self):
        os.system(f'git push -u https://{self.name_github}:{self.token_github}@github.com/{self.name_github}/{self.repository_name}.git main')

    def print_completed(self):
        print('\n')
        print("Project successfully pushed to the remote repository.")


def main():
    load_dotenv()
    name_github = os.getenv("GITHUB_USERNAME")
    token_github = os.getenv("GITHUB_TOKEN")

    if name_github is None or token_github is None:
        print("GitHub credentials not found in the .env file.")
        return
    
    current_path = os.path.dirname(__file__)

    # Create a GitProject instance
    my_project = GitProject(current_path, name_github, token_github)
    my_project.add()
    my_project.status()
    commit_description = input("Enter commit description: ")
    my_project.commit(commit_description)
    my_project.push()

    my_project.print_completed()


if __name__ == "__main__":
    main()