import os
from sqlalchemy import create_engine

def return_engine():
	#return create_engine('sqlite:////home/kangu/Escritorio/restful-project/interview_question/database/salaries.db')
	return create_engine('sqlite:///' + os.getcwd() + '/vinyl-catalox.db')