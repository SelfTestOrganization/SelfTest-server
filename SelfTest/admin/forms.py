# -*- coding: utf-8 -*-
"""Admin forms."""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

from .models import Candidate


class CandidateForm(FlaskForm):
    """Candidate form."""

    identification = StringField(
        "Identification", validators=[DataRequired(), Length(min=1, max=200)]
    )
    # TODO: testsets
    # TODO: also silently add "creator"

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(CandidateForm, self).__init__(*args, **kwargs)
        self.identification = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(CandidateForm, self).validate()
        if not initial_validation:
            return False
        candidate = Candidate.query.filter_by(
            identification=self.identification.data
        ).first()
        if candidate:
            self.identification.errors.append(
                "Candidate already exists, delete it before creating it again please"
            )
            return False
        return True
