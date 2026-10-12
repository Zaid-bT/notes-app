"""add user ownership to notes

Revision ID: 1640e8ab0b7a
Revises: 
Create Date: 2026-10-12 22:50:11.470361

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1640e8ab0b7a'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column(
        "notes",
        sa.Column("user_id", sa.Integer(), nullable=True)
    )

    op.create_foreign_key(
        "fk_notes_user_id_users",
        "notes",
        "users",
        ["user_id"],
        ["id"]
    )

    # Give existing notes to the first registered user
    op.execute(
        "UPDATE notes SET user_id = "
        "(SELECT id FROM users ORDER BY id LIMIT 1)"
    )

    op.alter_column(
        "notes",
        "user_id",
        nullable=False
    )


def downgrade():
    op.drop_constraint(
        "fk_notes_user_id_users",
        "notes",
        type_="foreignkey"
    )

    op.drop_column("notes", "user_id")
