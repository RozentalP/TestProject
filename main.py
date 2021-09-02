from flask import Flask
from app import views

app = Flask(__name__)

# url
app.add_url_rule('/base','base',views.base)
app.add_url_rule('/','index',views.index)
app.add_url_rule('/faceapp','faceapp',views.faceapp)
app.add_url_rule('/faceapp2','faceapp2',views.faceapp2)
app.add_url_rule('/faceapp/gender','gender',views.gender,methods=['GET','POST'])
app.add_url_rule('/faceapp2/emotion','emotion',views.emotion,methods=['GET','POST'])
# 
if __name__ == "__main__":
    app.run(debug=True)