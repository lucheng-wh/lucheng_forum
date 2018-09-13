"""
lucheng.forum.views.

This module handles the  forum logic like creating and viewing
topics and post.
"""
from flask import Blueprint, request, render_template

from lucheng.forum.models import Category
from lucheng.user.models import User
from lucheng.forum.forms import UserSearchForm


forum = Blueprint("forum", __name__)


@forum.route("/")
def index():
    """Forum index route function."""
    categories = Category.get_all()
    user_count = 1
    topic_count = 1
    post_count = 1

    return render_template('forum/index.html',
                           categories=categories,
                           user_count=user_count,
                           topic_count=topic_count,
                           post_count=post_count)


@forum.route("/memberlist", methods=['GET', 'POST'])
def memberlist():
    """Memberlist show logic view."""
    page = request.args.get('page', 1, type=int)

    search_form = UserSearchForm()
    if search_form.validate():
        print(search_form.search_query.data)
        users = User.query.paginate(page, 3, False)
    else:
        users = User.query.paginate(page, 3, False)

    print(users)
    return render_template("forum/memberlist.html", users=users,
                           search_form=search_form)
