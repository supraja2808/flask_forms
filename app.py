from flask import Flask,render_template,request

from flask_wtf import Form
from wtforms import StringField,SubmitField

from wtforms.validators import DataRequired

FAI=Flask(__name__)

@FAI.route('/htmlform',methods=['GET','POST'])

def htmlform():
    if request.method=="POST":
        fd=request.form
        return fd['n']
    return render_template('htmlform.html')

class Nameform(Form):
    name=StringField(validators=[DataRequired()])
    submit=SubmitField()

@FAI.route('/webforms',methods=['GET','POST'])
def webforms():
    form=Nameform()
    if request.method=='POST':
        fd=Nameform(request.form)
        if fd.validate():
            #return fd.name.data (this is only for name)
            return fd.data #(this is for total data)
    return render_template('webforms.html',form=form)


if __name__=='__main__':
    FAI.run(debug=True)