from deta import Deta
import streamlit as st
from streamlit_option_menu import option_menu
import time

st.title(":rainbow[NEWSSPOT]")
st.header(":blue[Explore the World]")
with st.sidebar:
     st.header("SELECT THE CATEGORY")
     selected=option_menu(menu_title="SELECT",options=["HOME","LOG OUT","HELP","QUERIES"],default_index=1,
                          menu_icon="None",orientation="vertical",styles="None")
if selected:
    if selected=="HOME":
              tab1, tab2, tab3 = st.tabs([":red[HOME]", ":red[SEARCH]", ":red[RATE THE APP]"])
              with tab1:
                    st.header("ABOUT NEWSSPOT")
                    st.write( """
                            Welcome to "NEWSSPOT," your go-to destination for staying informed and up-to-date with the 
                            latest news and happenings around the world. We understand the importance of reliable and 
                            timely information in today's fast-paced world, and that's why we've created a cutting-edge 
                            news app designed to keep you in the know effortlessly.
                            "NEWSSPOT" curates a personalized news feed that brings you stories aligned with your preferences. 
                            Whether you're into world affairs, technology, entertainment, or sports, we've got you covered.""")
              st.snow()
              with tab2:
                   select = st.text_input("Enter the Word")
                   submit = st.button("Search")
                   if submit:
                       with st.spinner("Wait for a second"):
                           time.sleep(5)
        
                       DETA_KEY ="yuihvgfjjijtfcjjj"
                       deta = Deta(DETA_KEY)
                       db = deta.Base("Workshop")
                       res = db.fetch(query={"category?contains": select})
                       data=res.items
                       for news in data:
                           st.header(news["headlines"])
                           with st.container():
                                left,right = st.columns(2)
                           with left:
                                st.image(news["images"])
                           with right:
                                st.write(news["news"])
                                st.write(news["authors"])
                                st.write(news["Date"])
                                st.write(news["country"])
              with tab3:
                    abc=st.slider("Rate the app",0,5,1)
                    se=st.button("SUBMIT")
                    if se:
                         st.write("THANK YOU")
                
                    
    if selected=="HELP":
         st.title(":grey[Welcome to NEWSSPOT Help Center]")
         st.markdown("-----------------------------")
         st.write("""
                  Thank you for choosing NEWSSPOT to stay informed about the latest news and updates.
                  Our Help Center is designed to assist you in navigating through the app and making 
                  the most of its features. If you have any specific questions, feel free to reach out
                  to our support team at [abcdefg@gmail.com/9056783467].""")
         st.title(":grey[Security and Privacy]")
         st.header("Account Security:")
         st.write("""
                  1. Ensure the security of your account by using a strong, unique password.
                  2. We prioritize the privacy and security of your data. Review our privacy policy for more information.""")
         st.divider()
         st.write("""Thank you for choosing NEWSSPOT.We hope you enjoy staying informed with our app. 
                  If you have any further questions, please don't hesitate to reach out to our support team.""")
         st.caption("""
                    Happy reading!
                    NEWSSPOT Team,:smile:""")

                  
               






                 

    
    
