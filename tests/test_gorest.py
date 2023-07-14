import pytest


@pytest.mark.parametrize("user_data",
                         [({"name": "Vlad F123", "gender": "male", "email": "vladf123@gmail.com", "status": "active"},
                           {'title': 'my title', 'body': 'my body'})
                          ])
def test_profile_tabs(new_user, user_data):
    """
    1. Create new user
    2. Create new post
    3. Verify that post has created
    4. Delete user
    """
    user = new_user(user_data)

    user.create_user()
    # assert response.status_code == 201
    #
    # response = user.get_user()
    # assert response.json()[0]['name'] == 'Vlad F12'

    response = user.create_post()
    assert response.status_code == 201

    response = user.get_user_posts()
    assert response.json()[0]['title'] == 'my title'
