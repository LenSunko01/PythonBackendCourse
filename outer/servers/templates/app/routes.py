from app import app

reminder_template = { "note_color" : "GR", "note_text" : "Do not forget!", "note_name" : "Reminder" }
shopping_template = { "note_color" : "BL", "note_text" : "Meat, eggs, bread",
                           "note_name" : "Shopping list" }

@app.route('/reminder')
def get_reminder_template():
    return reminder_template

@app.route('/shopping')
def get_shopping_template():
    return shopping_template