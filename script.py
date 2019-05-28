
@app.route('/floorplan/')
def floorplan():

    MIDDLE = """
     <h1><u>Floorplan</u></h1>
     <img src="/static/floorplan.jpg">
     <br>
    """

    return TOP + MIDDLE + BOTTOM

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
