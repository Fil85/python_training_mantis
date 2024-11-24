from model.project import Project


def test_add_project(app):
    old_projects = app.project.get_project_list()
    project_test = Project(name=app.project.random_string(), description=app.project.random_string())
    app.project.add_project(project_test)
    old_projects.append(project_test)
    new_projects = app.project.get_project_list()
    assert sorted(old_projects, key=Project.name_sort) == sorted(new_projects, key=Project.name_sort)


def test_add_project_soap(app):
    username = app.config["webadmin"]["username"]
    password = app.config["webadmin"]["password"]
    old_projects_soap = app.soap.get_project_list_soap(username, password)
    old_projects = []
    for project in old_projects_soap:
        old_projects.append(project.name)
    project_test = Project(name=app.project.random_string(), description=app.project.random_string())
    app.project.add_project(project_test)
    new_projects_soap = app.soap.get_project_list_soap(username, password)
    new_projects = []
    for project in new_projects_soap:
        new_projects.append(project.name)
    old_projects.append(project_test.name)
    assert sorted(old_projects) == sorted(new_projects)
