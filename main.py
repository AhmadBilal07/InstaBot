from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import time

#your login credentials
insta_username='ahmadbilalaslam@gmail.com'
insta_password='Parkinson@123'

def job():
  session = InstaPy(username=insta_username, password=insta_password,geckodriver_path="C:\\Users\\ahmad\\Downloads\\geckodriver.exe")
  with smart_run(session):
      session.follow_by_tags([ 'mahirakhan','fawadkhan'], amount=120)
job()