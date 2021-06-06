import streamlit as st
import pandas as pd
from pymongo import MongoClient

data=pd.read_csv("sce.csv");

st.sidebar.title("Any Issues Please Contact Facilitators")


def qwiklab():
	st.title("Qwiklabs Progress for GoogleCloudReady Facilitator Program 2021 🙏")
	st.text(" ")
	st.text(" ")
	st.write("Facilitators: Sapthagiri College Of Engineering Bangalore")
	x=st.text_input("Please Enter your Registered Email Address Only")


	try:
		for i in range(0,len(data)):
			if data['Student Email'][i]==x:
				st.write("Student Name  🖥️ ", data['Student Name'][i])
				st.write("No of Quests Completed  🖥️ ",data['# of Quests Completed'][i])
				st.write("No of Skill Badges Completed  🖥️ ",data['# of Skill Badges Completed'][i])
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
	client=MongoClient("mongodb+srv://aditya:aditya@gcf-cluster.vfgbl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
	db=client.get_database('myFirstDatabase')
	records=db.test
	data=st.text_input("Please Enter Only Once after you have given feedback")
	summary={
	    "student_feedback":data
	}
	records.insert_one(summary)
	
	

def collective_feedback_list():
	client=MongoClient("mongodb+srv://aditya:aditya@gcf-cluster.vfgbl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
	db=client.get_database('myFirstDatabase')
	records=db.test
	st.text(" ")
	st.text(" ")
	mydoc=records.find({'student_feedback':{'$gt':'a'}},{'_id':False})
	st.write("What Participants are Saying ❤️ ")
	summary_list=[]
	for i in mydoc:
	    st.write(i['student_feedback'])


def article():
	st.title("Welcome to Articles Zone 📚")
	st.write("article written success")


def swags():
	st.write("swags working")



def main():
	fac_select = ["Deepak","Aditya"]
	fac_choice = st.sidebar.radio("Hey👋, Whom do you What to Contact", fac_select)
	if fac_choice=="Deepak":
		st.sidebar.write("Contact No 📱",'+91 89705 51466')
		st.sidebar.markdown("Connect Us [Github](https://github.com/deepakkapse),"  "[linkedin](https://www.linkedin.com/in/deepak-k-31a414172/)")
	if fac_choice=="Aditya":
		st.sidebar.write("Contact No 📱",'+91 8618262232')
		st.sidebar.markdown("Connect Us [Github](https://github.com/Adityanagraj),"  "[linkedin](https://www.linkedin.com/in/aditya-n-02a0a8192)")
	
	score=["Quests","Feedback","Article","Swags"]
	score_choice=st.sidebar.selectbox("Find your Progress here 🥳",score)
	if score_choice=="Quests":
		qwiklab()
	if score_choice=="Feedback":
		feedback()
		collective_feedback_list()
	if score_choice=="Article":
		article()
	if score_choice=="Swags":
		swags()

	



if __name__ == "__main__": 
	main()

