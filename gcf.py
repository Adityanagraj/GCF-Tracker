import streamlit as st
import pandas as pd

data=pd.read_csv("sce.csv");

st.sidebar.title("Any Issues Please Contact Facilitators")
select = ["Deepak","Aditya"]
choice = st.sidebar.selectbox("Hey👋, Whom do you What to Contact", select)
if choice=="Deepak":
	st.sidebar.write("Contact No 📱",'+91 89705 51466')
	st.sidebar.markdown("Connect Us [Github](https://github.com/deepakkapse),"  "[linkedin](https://www.linkedin.com/in/deepak-k-31a414172/)")
if choice=="Aditya":
	st.sidebar.write("Contact No 📱",'+91 8618262232')
	st.sidebar.markdown("Connect Us [Github](https://github.com/Adityanagraj),"  "[linkedin](https://www.linkedin.com/in/aditya-n-02a0a8192)")

def main():
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
	st.markdown("Developed with ❤️ and ☕ by [Aditya](https://www.linkedin.com/in/aditya-n-02a0a8192)")



if __name__ == "__main__": 
	main()

