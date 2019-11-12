import logging

from source.core.utils import FolderUtils
from .base import *

logger = logging.getLogger('source')
logger.error("Current mode: %s" % os.getenv('MODE', 'DEVELOPMENT'))

if os.getenv('MODE') == 'PRODUCTION':
    from .prod import *
else:
    from .dev import *

FolderUtils.create_folder(STATIC_ROOT)
FolderUtils.create_folder(MEDIA_ROOT)
FolderUtils.create_folders(STATICFILES_DIRS)
