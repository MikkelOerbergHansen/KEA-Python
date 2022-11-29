
# import af modulet Flask
from flask import Flask, request, render_template, redirect, session
import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

plt.switch_backend('agg')



def TreeExample():
    df = pandas.read_excel("Semester_2/SimCorp_stuff/Static/testData.xlsx", sheet_name="DecTree")

    d = {'UK': 0, 'USA': 1, 'N': 2}
    df['Nationality'] = df['Nationality'].map(d)
    d = {'YES': 1, 'NO': 0}
    df['Go'] = df['Go'].map(d)

    features = ['Age', 'Experience', 'Rank', 'Nationality']

    X = df[features]
    y = df['Go']

    dtree = DecisionTreeClassifier()
    dtree = dtree.fit(X, y)

    tree.plot_tree(dtree, feature_names=features)
    plt.savefig('Semester_2/SimCorp_stuff/Static//Treeplot.png')

    data = []
    for i in range(0, len(list(df["Age"]))):
        templist = []
    
        templist.append(list(df["Age"])[i])
        templist.append(list(df["Experience"])[i])
        templist.append(list(df["Rank"])[i])
        templist.append(list(df["Nationality"])[i])
        templist.append(list(df["Go"])[i])
        data.append(templist)

    resultater = []
    resultater.append(data)
    resultater.append(dtree)

    return resultater







app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def startside():
    HeadLine = "Welcome"

    if request.method == 'POST':
        SearchWord = request.form['searchbar']
        
        return render_template('Startside.html', Headline = HeadLine, Search = SearchWord)


    
    return render_template('Startside.html', Headline = HeadLine)



@app.route('/LinRegExample', methods=['GET', 'POST'])
def LinearRegEx():
    HeadLine = "Linear Regression"

    if request.method == 'POST':
        SearchWord = request.form['searchbar']
        
        return render_template('LinReg.html', Headline = HeadLine, Search = SearchWord)


    
    return render_template('LinReg.html', Headline = HeadLine)





@app.route('/DecTreeExample', methods=['GET', 'POST'])
def DecTreesEx():
    HeadLine = "Decision Tree"
    datastuff = TreeExample()
    data = datastuff[0]
    dtree = datastuff[1]
    rule1 = "convert the values 'UK' to 0, 'USA' to 1, and 'N' to 2"
    rule2 = "convert the values 'YES' to 1, 'NO' to 0"
    Problem = "Beslut om der skal ses komedie show baseret på skuepillers karakteristik"
    

    if request.method == 'POST':
        
        if 'form1' in request.form:
            
            SearchWord = request.form['searchbar']
            return render_template('DecTree.html', Headline = HeadLine, Search = SearchWord, rule1=rule1, rule2=rule2, Data = data, problem = Problem)
        
        elif 'form2' in request.form:
            
            Age = int(request.form['Age'])
            Experience = int(request.form['Experience'])
            Rank = int(request.form['Rank'])
            Nationality = int(request.form['Nationality'])
            Resultat = dtree.predict([[Age, Experience, Rank, Nationality]])
            
            return render_template('DecTree.html', Headline = HeadLine, rule1=rule1, rule2=rule2, Data = data, problem = Problem, result = Resultat)


    
    return render_template('DecTree.html', Headline = HeadLine, rule1=rule1, rule2=rule2, Data = data, problem = Problem)






# til at køre koden direkte
if __name__== '__main__':
    app.run()
































