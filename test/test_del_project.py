import random
from model.project import Project


def test_del_project(app):
    app.session.login("administrator", "root")
    if len(app.project.get_project_list()) == 0:
        project_test = Project(name=app.project.random_string(), description=app.project.random_string())
        app.project.add_project(project_test)
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.del_project(project.name)
    old_projects.remove(project)
    new_projects = app.project.get_project_list()
    assert sorted(old_projects, key=Project.name_sort) == sorted(new_projects, key=Project.name_sort)
