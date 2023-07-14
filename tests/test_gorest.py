

def test_profile_tabs(user):
    """
    1. Create new user
    2. Verify that user has created
    3. Create new post
    4. Verify that post has created
    5. Delete user
    """
    status_code = user.get_user()
    assert status_code == 200

    status_code = user.create_post()
    assert status_code == 201

    status_code = user.get_user_posts()
    assert status_code == 200

