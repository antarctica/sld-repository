class MockGeoserverCatalogueWorkspace:
    def __init__(self, name):
        self.name = name


class MockGeoserverCatalogueStyle:
    def __init__(self, name, workspace):
        self.name = name
        self.style_format = 'sld10'
        self.workspace = MockGeoserverCatalogueWorkspace(name=workspace).name


class MockGeoServerCatalogue:
    @staticmethod
    def get_version() -> str:
        return 'testing'

    @staticmethod
    def get_workspaces():
        return [MockGeoserverCatalogueWorkspace(name=test_workspace_data['label'])]

    @staticmethod
    def get_workspace(name: str):
        return MockGeoserverCatalogueWorkspace(name=name)

    # noinspection PyUnusedLocal
    @staticmethod
    def get_styles(workspaces=None):
        return [MockGeoserverCatalogueStyle(
            name=test_style_data['label'],
            workspace=test_style_data['workspace']['name']
        )]

    @staticmethod
    def get_style(name: str, workspace: str):
        return MockGeoserverCatalogueStyle(
            name=name,
            workspace=workspace
        )


test_workspace_data = {
    'name': 'test-workspace-1'
}

test_style_data = {
    'name': 'test-style-1',
    'style_type': 'sld',
    'workspace': test_workspace_data
}
