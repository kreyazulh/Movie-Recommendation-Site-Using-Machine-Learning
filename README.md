# Movie-Recommendation-Site-Using-Machine-Learning
A simple movie recommendation site which suggests you movies like your searched query.
This project is based on machine learning basics which includes *text vectorization*, *stemming* and *connecting APIs*.
## How to run?
- Clone the git repository using-
``` git lfs clone```
- You will probably need to install git-lfs before with these commands ```sudo apt-get install git-lfs```
```git install lfs```
- Install the required libraries 
- Run app.py using ```streamlit run app.py```
- python 3.11 recommended

## Generating requirements.txt
```pip freeze > requirements.txt```
You can ignore this part.

**After running app.py, you will be redirected to the front end, where you can choose your desired movie and get recommendations based on that**

## Uploading lfs (large files to git)
- Enable pushing large files in repository settings -> archives
- ```git lfs track "file_name"```
- ```git lfs push all origin main```
- ```git add file_name```
- ```git commit -m "large file uploaded"```


