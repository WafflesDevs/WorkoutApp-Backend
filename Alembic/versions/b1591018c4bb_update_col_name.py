"""Update Col Name

Revision ID: b1591018c4bb
Revises: 9da1dd8496e4
Create Date: 2026-06-23 23:02:06.413079

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b1591018c4bb'
down_revision: Union[str, Sequence[str], None] = '9da1dd8496e4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('users', 'id', new_column_name='user_id')

def downgrade() -> None:
    op.alter_column('users', 'user_id', new_column_name='id')
