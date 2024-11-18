from model.project import Project


def test_add_project(app):
    project_new = Project(name="111", status="stable", view_state="private", description="test")
    app.session.login("administrator", "root")
    old_projects = app.project.get_project_list()
    app.project.add_project(project_new)
    new_projects = app.project.get_project_list()
    old_projects.append(project_new)
    assert old_projects == new_projects
