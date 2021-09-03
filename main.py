"""Main module for the streamlit app"""
from logging import log
import streamlit as st
import src.pages.about
import src.pages.projectCreation
import base64

PAGES = {
    "GCP Project Creation": src.pages.projectCreation,
    "GCP Resource Creation": src.pages.about,
}

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
      <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
}
</style>
    
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return
def main():
    """Main function of the App"""
    creds = False
    # set_png_as_page_bg('./c.png')
    # st.sidebar.image("./c.png", use_column_width=True )
    if 'creds' not in st.session_state:
        
        st.sidebar.title("Navigation")
        st.sidebar.radio("Go to ", list(PAGES.keys()))
        username = st.text_input("User Name")
        password = st.text_input("Password",type='password')
        login_button = st.button("Login")
        if login_button:
            if username ==password:
                st.session_state.creds= True
                st.experimental_rerun()
    else:
        st.sidebar.title("Navigation")
        selection = st.sidebar.radio("Go to", list(PAGES.keys()))
        page = PAGES[selection]
        page.write()
    
    for i in range(5):
        st.sidebar.title("")
    
   
    st.sidebar.title("About")
    st.sidebar.info(
        """
        This app is maintained by Virgin Media Cloud COE Team. You can learn more   at
        https://confluencePageLink.com.
"""
    )
    


if __name__ == "__main__":
    main()