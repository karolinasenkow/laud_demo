from datetime import datetime
from laud import db, login_manager
from flask_login import UserMixin
from functools import partial
from sqlalchemy import orm

db.Model.metadata.reflect(db.engine)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
class Metadata(db.Model):
   __table__ = db.Model.metadata.tables['dataset']
    
