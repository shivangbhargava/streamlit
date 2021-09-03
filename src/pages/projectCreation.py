import streamlit as st
def write():
    st.title("GCP Project Creation")
    st.container()
    project_type = st.selectbox("Project Type" ,["Datalake","Application","Datahub","Standalone"])
    program_id = st.text_input("Program Id")
   
    if (len(program_id) > 0 ) and (len(program_id)<16 ):
        print(len(program_id))
        # st.error("Please enter valid Project Id")
    else:
        st.error("Please enter Project Id")
    cost_center_code = st.text_input("Cost Center Code")
    requester_email = st.text_input("Email Id")
    create_project = st.button("Submit")
    if create_project:
     print(project_type ,program_id ,cost_center_code ,requester_email)