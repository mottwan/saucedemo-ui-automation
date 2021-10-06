import pytest
import logging

LOGGER = logging.getLogger(__name__)


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    LOGGER.info('log something')
    pass
