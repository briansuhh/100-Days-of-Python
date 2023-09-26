import os
import shutil


def exercise_template():
    # create the exercise template
    exercise_len = int(input("Exercise length: "))
    os.mkdir("Exercise")
    os.chdir("Exercise")
    for j in range(1, exercise_len + 1):
        os.system(f"touch exercise{j}.py")
        
    os.chdir("..")


def project_template(file, date):
    # create the project template
    project_name = input("Project name: ")
    instructions = input("Instructions: ")
    file.write(
f"""
# Project: {project_name}
- Instructions:<br>
{instructions}

- [{project_name} Code](main.py)

- Output:<br>
![{project_name}](../assets/img/{date}_project.png)
"""
    )

    os.system(f"touch main.py")


def folder_automate():
    date = int(input("Day: "))
    directory_name = f"Day {date}"

    # delete the exiting directory and all its contents
    if os.path.exists(directory_name):   
        shutil.rmtree(directory_name)
        
    os.mkdir(directory_name) 
    os.chdir(directory_name)

    # create a markdown file    
    with open("README.md", "w") as file:
        if input("Exercise? (y/n): ") == "y":
            exercise_template()

        project_template(file, date)

    os.chdir("..")


if __name__ == "__main__":
    folder_automate()
