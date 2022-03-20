import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import seaborn as sns
import numpy as np
import plotly.express as px
from PIL import Image



# create a function that takes in the location of a csv and returns the pandas dataframe with the score sum and score avg columns
def create_df(file_path):
    students_df = pd.read_csv(file_path)
    students_df.head()
    students_df['score sum'] = students_df['math score'] + students_df['reading score'] + students_df['writing score']
    students_df['score average'] = (students_df['math score'] + students_df['reading score'] + students_df['writing score'])/3
    return students_df

def graph_scatter(students_df):
    sns.scatterplot(data = students.df, x = students_df['writing score'], y= students_df['math score'], hue ='day')
    plt.scatter(students_df['writing score'], students_df['math score'], color='blue', label='Math Score')
    plt.scatter(students_df['writing score'], students_df['reading score'], color='green', label='Reading Score')
    m, c = np.polyfit(students_df['writing score'], students_df['reading score'], 1)
    plt.plot(students_df['writing score'], m*students_df['writing score']+c, color='red', label='Reading LOBF')
    a, b = np.polyfit(students_df['math score'], students_df['reading score'], 1)
    plt.plot(students_df['writing score'], a*students_df['writing score']+b, color='black', label='Math LOBF')
    plt.legend()
    plt.xlabel("Writing Score")
    plt.ylabel("Score")    
    
    plt.show()
    
def concat_scatter_scores(students_df):
    math_scores = students_df['math score'].tolist()
    reading_scores = students_df['reading score'].tolist()
    writing_scores = students_df['writing score'].tolist()

    full_writing_scores = writing_scores + writing_scores
    full_scores = reading_scores + math_scores

    score_type = []
    for i in range(len(writing_scores)):
        score_type.append('reading')
    for i in range(len(writing_scores)):
        score_type.append('math')

    scores_dict = {'score type': score_type,'all scores': full_scores, "writing scores": full_writing_scores}
    scores = pd.DataFrame.from_dict(scores_dict)
    
    fig = Figure()
    ax = fig.subplots()
    sns.scatterplot(data=scores, x="writing scores", y='all scores', hue='score type', ax=ax)
    
    return fig

def sns_scatter(students_df):
    fig = Figure()
    ax = fig.subplots()
    sns.scatterplot(data = students_df, x = students_df['writing score'], y=students_df['math score'],ax=ax)
    return fig

# create a function that displays the bar graph of parents' college background and their students' scores
def create_college_bars(students_df):
    students_df['score sum'] = students_df['math score'] + students_df['reading score'] + students_df['writing score']
    students_df['score average'] = (students_df['math score'] + students_df['reading score'] + students_df['writing score'])/3
    stu_gr = students_df.groupby(['parental level of education'])['score average'].mean().reset_index()
    stugr_sorted = stu_gr.sort_values('score average')

    plt.bar(stugr_sorted['parental level of education'], stugr_sorted['score average'],color='orange')
    plt.xlabel("Parental Level of Education", size = 20 )
    plt.ylabel("Score Average", size = 20 )
    plt.title("Parents College Background Vs Test Scores", size = 20)

    plt.show()

def sns_barplot(students_df):
    fig = Figure()
    ax = fig.subplots()
    stu_gr = students_df.groupby(['parental level of education'])['score average'].mean().reset_index()
    stugr_sorted = stu_gr.sort_values('score average')
    sns.barplot(data = stugr_sorted, x = stugr_sorted['parental level of education'], y=stugr_sorted['score average'], ax=ax)
    ax.set_xlabel("Parental Level of Education")
    ax.set_ylabel("Score Average")
    ax.set_title("Parents College Background VS. Test Scores")
    ax.set_ylim(0,100)
    return fig


# create a function that displays a bar graph between test preparation and students' scores
def scoreprep_bars(students_df):
    students_df['score average'] = (students_df['math score'] + students_df['reading score'] + students_df['writing score'])/3
    preparation_df = students_df[students_df['test preparation course']=="none"]
    preparation1_df = students_df[students_df['test preparation course']=="completed"]
    X = ['none', 'completed']
    Ymale = [63.044372, 70.781609]
    Zfemale = [66.878244, 74.454710]
    X_axis = np.arange(len(X))
    plt.bar(X_axis - 0.2, Ymale, 0.4, label = 'male', color='paleturquoise')
    plt.bar(X_axis + 0.2, Zfemale, 0.4, label = 'female', color='darksalmon')
    plt.xticks(X_axis, X)
    plt.xlabel("Test Preparation Course")
    plt.ylabel("Score Average")
    plt.title("Test Preparation vs Score Average", size = 20)
    plt.legend()
    plt.show()

def sns_barplot2(students_df):
    fig = Figure()
    ax = fig.subplots()
    sns.barplot(data = students_df , x = 'test preparation course', y = 'score average', hue = 'gender', ci = None, palette = "coolwarm_r", ax=ax)
    return fig

# all plotly plots

# math + reading vs writing scores scatterplot
def plt_display_scores(students_df):
    math_scores = students_df['math score'].tolist()
    reading_scores = students_df['reading score'].tolist()
    writing_scores = students_df['writing score'].tolist()
    full_writing_scores = writing_scores + writing_scores
    full_scores = reading_scores + math_scores
    score_type = []
    for i in range(len(writing_scores)):
        score_type.append('reading')
    for i in range(len(writing_scores)):
        score_type.append('math')
    scores_dict = {'score type': score_type,'all scores': full_scores, "writing scores": full_writing_scores}
    scores = pd.DataFrame.from_dict(scores_dict)
    fig = px.scatter(data_frame= scores, x= "writing scores", y="all scores", color='score type', opacity = .4)
    return fig
# test preparation course vs score average bar plot
def plt_testprep_bars(students_df, column_var):
    students_df['score sum'] = students_df['math score'] + students_df['reading score'] + students_df['writing score']
    students_df['score average'] = (students_df['math score'] + students_df['reading score'] + students_df['writing score'])/3
    stu_gr = students_df.groupby(['test preparation course'])[column_var].mean().reset_index()
    fig = px.histogram(students_df, x="test preparation course", y=column_var, color='gender', barmode='group', height=400, histfunc='avg', category_orders={"gender": ["male", "female"]})
    fig.update_layout(xaxis_title_text='Test Preparation Course')
    return fig
# parental level of education vs scores bar plot with buttons
def plotly_barplot(students_df, column_var = 'average score'):
    stu_gr = students_df.groupby(['parental level of education'])[column_var].mean().reset_index()
    stugr_sorted = stu_gr.sort_values(column_var)
    df = stugr_sorted
    fig = px.bar(df, x='parental level of education', y=column_var)
    return fig

students_df = create_df('data/StudentsPerformance.csv')

# create streamlit app
st.title('Students Performance Analysis')
st.image("https://res.cloudinary.com/practicaldev/image/fetch/s--nkbKznEQ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://cdn.hashnode.com/res/hashnode/image/upload/v1636441705202/ODmr6FiX6.jpeg")
st.subheader("This interactive website demonstrates the correlation of many elements to a student's performance.")
st.subheader("These graphs below show the various results of students with variables altering their performance.")
st.subheader("Students are being more academically challenged with today's society and educational pressures.")

st.write('Math & Reading v. Writing Scores')
st.plotly_chart(plt_display_scores(students_df))

col1, col2 = st.columns(2)
with col1:
    score_selection = st.radio("Select Certain Scores", ('Writing score', 'Reading score', 'Math score', 'Score average'), key=1).lower()

with col2:
    st.write("Test Preparation v. Test Scores Average")
    st.plotly_chart(plt_testprep_bars(students_df, score_selection))

col3, col4 = st.columns(2)
with col3:
    score_selection = st.radio("Select Certain Scores", ('Writing score', 'Reading score', 'Math score', 'Score average'), key=2).lower()

with col4:
    st.write("Parental Level of Education & Test Scores Average")
    st.plotly_chart(plotly_barplot(students_df, score_selection))
st.subheader("Rigors of students backgrounds are tested through the means of exams... Through this dataset we have compared the exam scores of men and women based on variables that we found that would affect academic performance. Dataset used: https://www.kaggle.com/spscientist/students-performance-in-exams")
