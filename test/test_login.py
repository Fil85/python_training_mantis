def test_login(app):
    app.session.login("administrator", "root")
    assert app.session_is_logged_in("administrator")