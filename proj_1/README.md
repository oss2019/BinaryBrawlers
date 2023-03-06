__On Windows__ Open powershell in administrator mode and type
```pwsh
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Force
exit
````

Open new Powershell/Terminal. Check your python version using
```sh
python --version
```

if python version comes 2.7.x then use *python3* in place of *python* in the following commands

```sh
python -m pip install virtualenv
```

Go to the dicrctory where you will like to start the project

```
mkdir proj_1
cd proj_1
python -m virtualenv ./env
env\Scripts\activate.ps1
pip install beautifulsoup4 requests
```
