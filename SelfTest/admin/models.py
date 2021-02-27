# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt
import enum

from flask_login import AnonymousUserMixin

from SelfTest.database import Column, PkModel, db, reference_col, relationship


class ResultsEnum(enum.Enum):
    """Enum for results."""

    good = 1
    bad = 2
    not_evaluated = 3


class Result(PkModel):
    """A result question we can ask."""

    __tablename__ = "results"
    result = Column(db.Enum(ResultsEnum))
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    asked_at = Column(db.DateTime, default=None)
    answered_at = Column(db.DateTime, default=None)
    candidate_id = reference_col("candidates")
    candidate = relationship("Candidate", backref="results")
    question_id = reference_col("questions")
    question = relationship("Question", backref="results")

    def __init__(self, candidate, question, **kwargs):
        """Create instance."""
        super().__init__(candidate=candidate, question=question, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<Result({self.candidate}, {self.question}, {self.result})>"


class Question(PkModel):
    """A question we can ask."""

    __tablename__ = "questions"
    name = Column(db.String(100), nullable=False)
    area = Column(db.String(100), nullable=False)
    testset = Column(db.String(100), nullable=False)
    version = Column(db.Integer, nullable=False)
    data = Column(db.JSON, nullable=False)

    def __init__(self, name, **kwargs):
        """Create instance."""
        super().__init__(name=name, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<Question({self.testset}/{self.area}/{self.name}:{self.version})>"


class Candidate(AnonymousUserMixin, PkModel):
    """A users taking the test."""

    __tablename__ = "candidates"
    identification = Column(db.String(200), unique=True, nullable=False)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    started_at = Column(db.DateTime, default=None)
    finished_at = Column(db.DateTime, default=None)
    # TODO: creator - user that crerated it
    # TODO: testsets - what testsets user have to take
    # TODO: watchers - who should be notified when candidate finishes the test

    def __init__(self, identification, **kwargs):
        """Create instance."""
        super().__init__(identification=identification, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<Candidate({self.identification})>"
