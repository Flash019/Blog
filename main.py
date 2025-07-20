from fastapi import FastAPI


app= FastAPI()

@app.get('/')
def index():
    return {'name': 'Soumyabrata'} #dictionary
@app.get('/about')
def about():
    return {'Founder':'Apexars'}