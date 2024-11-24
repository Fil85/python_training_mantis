import random
from model.project import Project


def test_del_project(app):
    if len(app.project.get_project_list()) == 0:
        project_test = Project(name=app.project.random_string(), description=app.project.random_string())
        app.project.add_project(project_test)
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.del_project(project.name)
    old_projects.remove(project)
    new_projects = app.project.get_project_list()
    assert sorted(old_projects, key=Project.name_sort) == sorted(new_projects, key=Project.name_sort)


def test_del_project_soap(app):
    username = app.config["webadmin"]["username"]
    password = app.config["webadmin"]["password"]
    if len(app.project.get_project_list()) == 0:
        project_test = Project(name=app.project.random_string(), description=app.project.random_string())
        app.project.add_project(project_test)
    old_projects_soap = app.soap.get_project_list_soap(username, password)
    old_projects = []
    for project in old_projects_soap:
        old_projects.append(Project(id = project.id, name=project.name))
    project = random.choice(old_projects)
    app.project.del_project(project.name)
    old_projects.remove(project)
    new_projects_soap = app.soap.get_project_list_soap(username, password)
    new_projects = []
    for project in new_projects_soap:
        new_projects.append(Project(id = project.id, name=project.name))
    assert sorted(old_projects, key=Project.name_sort) == sorted(new_projects, key=Project.name_sort)
