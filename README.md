# Hublinker 

Hublinker is a command line tool (CLI) for easy navigation and management of repositories on GitHub directly from the terminal. Ideal for developers who work intensively with GitHub and want a fast and user-friendly interface to perform common operations. 

## Installation 
clone or fork the project and go to root directory

Downloading dependencies 

```bash 
pip install - r requirements.txt
```

installing project (method recommended by the dependency) 

```bash 
pip install .
```

or 

```bash 
python3 setup.py install
```

if you want to run without installation use in the root folder of the project

```bash
python3 -m hublinker 

```

## Documentation 
- limit 
lists the consumption and usage limit of the gitHub api 

```bash 
hublinker 
```

- repos 
group of commands related to repositories 
```bash 
hublinker repos
```

1) public 

it will list a user's public repositories and allow cloning 

```bash 
hublinker repos public --user <user> 
```

2) private 

it will list your private repositories through the configured token and will allow you to clone 

```bash 
hublinker repos 
```

- config configuration options 

```bash 
hublinker config
```

1) set-token
config adds the token for authentication in the api (can be generating in settings -> developer settings -> personal access token -> tokens) 

```bash 
hublinker config set-token 
```

2) set-clone-path 

config adds the path where new repositories will be cloned 

```bash 
hublinker config set-clone-path 
```

3) set-rows-page 
config changes the row limit when querying repositories 
```bash 
hublinker config set-rows-page 
```

## Contributing 
Contributions are welcome! 
To contribute: 
- Make a fork of the project for features
- Create a new branch (`git checkout -b feature/MyFeature`) 
- Commit your changes (`git commit -m 'Add MinhaFeature'`) 
- Push to branch (`git push origin feature/MyFeature`) 

open a Pull Request for hotfix 
- Create a new branch (`git checkout -b hotfix/MeuHotFix_numeroIssue`) 
- Commit your changes (`git commit -m 'Add MeuHotFix_numeroIssue'`) 
- Push to branch (`git push origin hotfix/MeuHotFix_numeroIssue`) 

open a Pull Request for bugFix (add issue number only if you have it if you don't add a short description) 
- Create a new branch (`git checkout -b bugFix/BugFix_numeroIssue`) 
- Commit your changes (`git commit -m 'Add BugFix_numeroIssue'`) 
- Push to branch (`git push origin bugFix/BugFix_numeroIssue`) 

## License [MIT](https://choosealicense.com/licenses/mit/)
