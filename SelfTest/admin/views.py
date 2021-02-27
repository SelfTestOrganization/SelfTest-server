# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required

blueprint = Blueprint("admin", __name__, url_prefix="/admin", static_folder="../static")


@blueprint.route("/questions")
@login_required
def questions():
    """Browse questions in database."""
    return render_template("admin/questions.html")


@blueprint.route("/candidates")
@login_required
def candidates():
    """Manage allowed candidates."""
    return render_template("admin/candidates.html")


@blueprint.route("/results")
@login_required
def results():
    """Manage candidate results."""
    return render_template("admin/results.html")
