import streamlit as st
import pandas as pd
from pymongo import MongoClient

data=pd.read_csv("sce1.csv");

st.sidebar.title("Any Issues Please Contact Facilitators")



def qwiklab():
	st.title("Qwiklabs Progress for GoogleCloudReady Facilitator Program 2021 🙏")
	st.text(" ")
	st.text(" ")
	st.write("Facilitators: Sapthagiri College Of Engineering Bangalore")
	x=st.text_input("Please Enter your Registered Email Address Only without space")
	st.button("Submit")

	try:
		for i in range(0,len(data)):
			if data['Mailid'][i]==x:
				st.write("Student Name  🖥️ ", data['Name'][i])
				st.write("No of Quests Completed  🖥️ ",data['Quest'][i])
				st.write("No of Skill Badges Completed  🖥️ ",data['Skill'][i])
				st.write("Milestone one  1️⃣ ",data['Milestone 1'][i])
				st.write("Milestone two 2️⃣",data['Milestone 2'][i])
				st.write("Milestone three 3️⃣",data['Milestone 3'][i])
				st.write("Milestone four 4️⃣",data['Milestone 4'][i])
				st.balloons()
			


	except:
		print("Try After Some Time")	

	st.text(" ")
	st.markdown("Developed with ❤️ and ☕ by [Aditya N](https://www.linkedin.com/in/aditya-n-02a0a8192) & [Deepak K](https://www.linkedin.com/in/deepak-k-31a414172/)")

def feedback():
	st.title("GoogleCloudReady Facilitator Program 2021 Feedback🙏")
	st.text(" ")
	st.text(" ")
	st.write("Facilitators: Sapthagiri College Of Engineering Bangalore")
	client=MongoClient("DATABASE_CONN")
	db=client.get_database('myFirstDatabase')
	records=db.test1
	data=st.text_input("Please click Only Once on submit button after you have given feedback")
	summary={
		"student_feedback":data
	}
	if len(summary['student_feedback'])>0:
		records.insert_one(summary)
		st.write("Thank you for your Valuable Feedback🙏")
	else:
		st.write("Please provide your Feedback")
	
	

def collective_feedback_list():
	client=MongoClient( "DATABASE_CONN" )
	db=client.get_database('myFirstDatabase')
	records=db.test1
	st.text(" ")
	st.text(" ")
	mydoc=records.find({'student_feedback':{'$gt':'A'}},{'_id':False})
	st.write("What Participants are Saying ❤️ ")
	for i in mydoc:
		st.write(i['student_feedback'])


def article():
	st.title("Welcome to Articles Zone 📚")
	st.write('''
         Done with Cloud, What Next?🤔
That was amazing to see you learning cloud from the google cloud program. 
It's time to explore more.
Here are articles by our authors beautifully explained on various topics like AWS, GoogleCloud, DevOps, and much more.
Make time to learn from them

Aditya N: https://aditya-nagraj1999.medium.com/ \n
Vinodha Kumara:  https://vinodhakumara2681997.medium.com/ \n
Deepak k: https://deepakkapse08.medium.com/ \n
Antariksh Pratham: https://medium.com/@APratham \n


		''')


def swags():
	st.title("Big Surpise!!!")
	st.write('''
		   
We are amazed to see your active participation in the program and hence here we are with **surprise swags** for all of you!!!
Time to bid farewell with some amazing extra swags!

1: Tshirt Goodie by Cockroach DB
Watch the below video and register and attend the final exam to get Tshirt Goodie

Answers and registration link are in the video group description


2: Amazon vouchers+Tshirt Goodie by AWS Reskill
Register and watch video and participate in quiz to earn points to gain Tshirt Swag
https://bit.ly/AWSReskill

3: Free Coursera premium courses for INDIANS
https://bit.ly/34X3Cur

4: Free AT&T Workshop  with swags give away
Register and attend workshops to win amazing swags and giveaways

https://bit.ly/3wajgPq

**Disclaimer: These are collected and notified by facilitators solely and have no connection with the google cloud-ready program.
We are not responsible for  swags offer guarantee or  expiry  of the offer**



		''')

	st.video("https://youtu.be/TqDP4HetHb8")


def main():
	fac_select = ["Deepak K","Aditya N"]
	fac_choice = st.sidebar.radio("Hey👋, Whom do you What to Contact", fac_select)
	if fac_choice=="Deepak K":
		st.sidebar.write("Contact No 📱",'+91 89705 51466')
		st.sidebar.markdown("Connect Us [Github](https://github.com/deepakkapse),"  "[Twitter](https://twitter.com/deepak_kapse29)")
	if fac_choice=="Aditya N":
		st.sidebar.write("Contact No 📱",'+91 86182 62232')
		st.sidebar.markdown("Connect Us [Github](https://github.com/Adityanagraj),"  "[Twitter](https://twitter.com/nagraj1999)")

	score=["Quests","Feedback","Article","Swags"]
	score_choice=st.sidebar.selectbox("Find your Progress here 🥳",score)
	st.sidebar.text("")

	if score_choice=="Quests":
		qwiklab()
	if score_choice=="Feedback":
		feedback()
		collective_feedback_list()
	if score_choice=="Article":
		article()
	if score_choice=="Swags":
		swags()
	st.sidebar.title('**Special thanks to**' )
	st.sidebar.write('''

📌 Antariksh Pratham\n
📌 Aditya Ghuge \n
📌 Kushagra Arora\n
📌 Manikanta B\n
📌 Ujwal M

for joining hands in making this event successful🙏


		''')	



if __name__ == "__main__": 
	main()

