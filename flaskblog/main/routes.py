from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    q = request.args.get('q')
    if q:
        posts = Post.query.filter(Post.title.contains(q)).order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
    else:
        posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
    return render_template('home.html', posts=posts)


@main.route('/about')
def about():
    return render_template('about.html', title='About')