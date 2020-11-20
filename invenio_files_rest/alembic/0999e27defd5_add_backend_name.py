#
# This file is part of Invenio.
# Copyright (C) 2020 Cottage Labs LLP
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Add backend_name."""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '0999e27defd5'
down_revision = '8ae99b034410'
branch_labels = ()
depends_on = None


def upgrade():
    """Upgrade database."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'files_files',
        sa.Column('storage_backend',
                  sa.String(length=32),
                  nullable=True))
    op.add_column(
        'files_location',
        sa.Column('storage_backend',
                  sa.String(length=32),
                  nullable=True))
    # ### end Alembic commands ###


def downgrade():
    """Downgrade database."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('files_location', 'storage_backend')
    op.drop_column('files_files', 'storage_backend')
    # ### end Alembic commands ###
