import pip

with open("requirements.txt") as f:
    for line in f:
        # call pip's main function with each requirement
        pip.main(['install','-U', line])