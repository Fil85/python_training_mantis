def test_sign_up_new_account(app):
    username = "user111"
    password = "test"
    app.james.ensure_user_exists(username, password)