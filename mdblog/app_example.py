from flask import Flask

flask_app = Flask(__name__)

@flask_app.route("/")
def index():
    return "Hello world"

@flask_app.route("/admin/")
def view_admin():
    return "Hello admin"

# string if default
@flask_app.route("/admin/<string:name>/" , methods=["GET","POST"])
def view_admin_name(name):
    return "Hello {}".format(name)

@flask_app.route("/article/<int:art_id>/")
def view_article(art_id):
    return "Article #{}".format(art_id)

@flask_app.route("/article/<int:art_id>/tool/<float:foo>")
def view_article_tool(art_id,foo):
    return "Article #{} tool: {}".format(art_id,foo)
