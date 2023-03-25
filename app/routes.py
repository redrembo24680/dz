from app import app
from random import randrange



@app.route("/")
def index():
    list_ = [randrange(1, 200) for x in range(15)]
    list_.sort()
    return list_


@app.route("/personal")
def personal():
        name = "Roman"
        age = 16
        country = "Ukraine"
        return f"моє імя {name} мій вік {age} моя країна {country}"

