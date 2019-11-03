import logging

from source.core.utils import FolderUtils
from .base import *

logger = logging.getLogger('source')
logger.error("Current mode: %s" % os.getenv('MODE', 'DEVELOPMENT'))

if os.getenv('MODE') == 'PRODUCTION':
    from .prod import *
else:
    from .dev import *

FolderUtils.create_folders([STATIC_ROOT, MEDIA_ROOT] + [i for i in STATICFILES_DIRS])
