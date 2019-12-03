import pytest

from bas_sld_repository import create_app

from tests.bas_sld_repository.conftest.geoserver import MockGeoServerCatalogue


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture
@pytest.mark.usefixtures('app')
def app_runner(app):
    return app.test_cli_runner()


@pytest.fixture
def geoserver_catalogue():
    return MockGeoServerCatalogue()
