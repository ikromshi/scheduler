from app import app
# from scheduler import schedule_shifts

@app.route("/")
@app.route("/index")
def index():
  # shifts = schedule_shifts
  return "Index"

if __name__ == '__main__':
  app.run(debug=True)