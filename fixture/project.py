from selenium.webdriver.support.ui import Select
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def add_project(self, project):
        wd = self.app.wd
        self.open_new_project_form()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def open_new_project_form(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("description")) > 0):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()
            wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def fill_project_form(self, project):
        self.change_field_value("name", project.name)
        self.change_field_value("status", project.status)
        self.change_field_value("view_state", project.view_state)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            if field_name != "status" and field_name != "view_state":
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(text)
            elif field_name == "status" or field_name == "view_state":
                wd.find_element_by_name(field_name).click()
                Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_projects_page()
            self.project_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.project_cache.append(Project(name=text, id=id))
        return list(self.project_cache)

    project_cache = None
