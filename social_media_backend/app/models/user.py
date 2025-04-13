from enum import Enum
from datetime import datetime, timezone
from ..extensions import db

class UserRoleEnum(Enum):
    admin = "admin"
    moderator = "moderator"
    user = "user"

class User(db.Model):
    __tablename__ = "user"

    id: db.Mapped[int] = db.mapped_column(primary_key=True)
    username: db.Mapped[str] = db.mapped_column(db.String(80), unique=True, nullable=False)
    email: db.Mapped[str] = db.mapped_column(db.String(120), unique=True, nullable=False)
    password: db.Mapped[str] = db.mapped_column(db.String(255), nullable=False)

    f_name: db.Mapped[str] = db.mapped_column(db.String(100), nullable=False)
    l_name: db.Mapped[str] = db.mapped_column(db.String(100), nullable=False)

    bio: db.Mapped[str] = db.mapped_column(db.String(160))
    profile_picture_url: db.Mapped[str] = db.mapped_column(db.Text)

    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(
        db.DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc)
    )

    last_seen = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    role: db.Mapped[UserRoleEnum] = db.mapped_column(
        db.Enum(UserRoleEnum),
        default=UserRoleEnum.user,
        nullable=False
    )

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "f_name": self.f_name,
            "l_name": self.l_name,
            "bio": self.bio,
            "profile_picture_url": self.profile_picture_url,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "last_seen": self.last_seen.isoformat(),
            "role": self.role.name
        }

    def __repr__(self):
        return f"<User {self.username}>"
