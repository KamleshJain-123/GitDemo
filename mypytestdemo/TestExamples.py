import pytest

from mypytestdemo.baseClass import baseClass


@pytest.mark.usefixtures("testdata")
class TestExamples(baseClass):
    def test_fixturedemo(self, testdata):
        log = self.getlogger()
        log.info(testdata[1])
        log.info(testdata)
        print("this is print")
