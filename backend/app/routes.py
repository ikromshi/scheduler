from app import app

@app.route("/")
@app.route("/index")
def index():
  return "Index Route"

if __name__ == '__main__':
  app.run(debug=True)