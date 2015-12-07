from flask import Flask,render_template,request
import enchant
import itertools

d = enchant.Dict("en_US")



app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/solve',methods=['POST','GET'])
def solver():
	letters = request.form['letters']
	return render_template('words.html',words = solve(letters))	

def solve(letters):

	words = []
	x = {}

	for i in xrange(3,len(letters)+1):
		for e in list(itertools.combinations(letters,i)):
			for j in list(itertools.permutations(e)):
				if d.check(''.join(j)):
					words.append(''.join(j))
	b = sorted(list(set(words)),key=len)
	b.reverse()
	x['max_length_word'] = b[0]

	for ele in b:
		if not x.get(len(ele)):
				x[len(ele)] = [ele]
		else:
				x[len(ele)].append(ele)


	return x

if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0',port =8000)