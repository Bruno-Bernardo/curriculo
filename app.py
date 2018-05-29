from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')
	
@app.route("/sobre")
def sobre():
	return render_template('sobre.html')
	
if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=80)