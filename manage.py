import Project

def main():
    try:
        Project.load_env()
        Project.project.run(debug= True)
    except Exception as error:
        print(error)


if __name__ == '__main__':
    main()
    
