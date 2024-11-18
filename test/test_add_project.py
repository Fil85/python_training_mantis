from model.project import Project


def test_add_project(app):
    project = Project(name="111", description="test")
    app.session.login("administrator", "root")
    #old_projects = app.get_project_list()
    app.projects.create(project)
    #new_projects = app.get_project_list()
    #old_projects.append(project)
    #assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)