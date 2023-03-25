from app import exm
from random import randrange
from flask import render_template
@exm.route("/")
def index():
    list_ = [randrange(1, 200) for x in range(15)]
    list_.sort()
    return list_


@exm.route("/personal")
def personal():
    person = {
        "Ім\'я" : "Roman",
        "Вік" : 16,
        "Країна" : "Ukraine",
    }
    person.__getitem__
    return render_template('personal.html', content = person )
