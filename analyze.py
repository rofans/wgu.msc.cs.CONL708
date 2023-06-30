# Load libraries
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


url = "https://raw.githubusercontent.com/rofans/wgu.msc.cs.CONL708/main/jobs-data-training.csv"
names = ['job_title','location','salary_currency','career_level','experience_level','education_level','employment_type','job_function','job_benefits','company_process_time','company_size','company_industry','job_description','salary']
dataset = read_csv(url, names=names, sep = '|')

print(dataset.shape)

print(dataset.head(20))

print(dataset.describe())

print(dataset.groupby('job_title').size())
