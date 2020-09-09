import random
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from ecommerce.aws.download.utils import AWSDownload
from ecommerce.aws.utils import ProtectedS3Storage
from ecommerce.utils import unique_slug_generator, get_filename