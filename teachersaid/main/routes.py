from flask import render_template, request, Blueprint
from teachersaid.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html', title='Home')


@main.route("/list")
def list():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('list.html', posts=posts)


@main.route("/test")
def about():
    return render_template('test.html', title='Test')