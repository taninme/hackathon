import os 

from app import app

#port = int(os.environ.get('PORT', 80))
app.debug = True
#app.run(host="0.0.0.0", port = port)
app.run()
