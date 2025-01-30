from flask import Flask,request,render_template
import random
app=Flask(__name__)
choices=["stone","paper","scissor"]
@ app.route("/",methods=["POST"])
def explore():
    if request.method=="POST":
        my_choice=request.form.get("choice")
        computer_choice=random.choice(choices)
        if my_choice==computer_choice:
            result="it is tie"
        elif (my_choice=="stone"and computer_choice=="scissor")or\
             (my_choice=="paper"and computer_choice=="stone")or\
             (my_choice=="scissor" and computer_choice=="paper"):
            result="you won the game"
        else:
            result="computer won the game"
        return render_template("home.html",my_choice=my_choice,computer_choice=computer_choice,result=result)
    return render_template("home.html",my_choice=None,computer_choice=None,result=None)
if __name__ == "__main__":
    app.run(debug=True)
    