import os
import shutil


def title_template(file):
    # create the title template
    file.write(
f"""# Coding Exercises
#### Click the toggle button to show the picture of the output.

---
"""
    )


def exercise_template(file, date):
    # create the exercise template
    exercise_len = int(input("Exercise length: "))
    os.mkdir("Exercise")
    os.chdir("Exercise")
    for j in range(1, exercise_len + 1):
        exercise_name = input(f"Exercise {j} title: ")
        file.write(
f"""
## Exercise {j} - {exercise_name}
- Instructions:<br>

- [{exercise_name} Code](exercise{j}.py)

<details>
<summary>Output:</summary>

![Day {date} Exercise {j}](../assets/img/{date}_exercise_{j}.png)
</details>

---
"""
        )
        os.system(f"touch exercise{j}.py")
        
    os.chdir("..")


def project_template(file, date):
    # create the project template
    file_name = input("Project file name: ")
    project_name = input("Project name: ")
    file.write(
f"""
# Project: {project_name}
- Instructions:<br>

- [{project_name} Code]({file_name})

- Output:<br>
![{project_name}](../assets/img/{date}_project.png)
"""
    )

    os.system(f"touch {file_name}.py")


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
        print("\n\n---------------------README.md Contents---------------------\n")
        title_template(file)

        if input("Put exercise template? (y/n): ") == 'y':
            exercise_template(file, date)

        if input("Put project template? (y/n): ") == 'y':
            project_template(file, date)

    os.chdir("..")


if __name__ == "__main__":
    folder_automate()
