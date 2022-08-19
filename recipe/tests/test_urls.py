from django.urls import resolve, reverse




def test_index_url():
    path = reverse('index')
    assert resolve(path).view_name == 'index'


def test_signup_url():
    path = reverse('signup')
    assert resolve(path).view_name == 'signup'


def test_signin_url():
    path = reverse('signin')
    assert resolve(path).view_name == 'signin'


def test_signout_url():
    path = reverse('signout')
    assert resolve(path).view_name == 'signout'

def test_success_url():
    path = reverse('success')
    assert resolve(path).view_name == 'success'

def test_dashboard_url():
    path = reverse('dashboard')
    assert resolve(path).view_name == 'dashboard'

def test_detail_url():
    path = reverse('detail', kwargs={'pk':1})
    assert resolve(path).view_name == 'detail'

def test_recipe_form_url():
    path = reverse('recipe-form')
    assert resolve(path).view_name == 'recipe-form'

def test_recipe_delete_url():
    path = reverse('recipe-delete', kwargs={'pk':1})
    assert resolve(path).view_name == 'recipe-delete'

def test_recipe_update_url():
    path = reverse('recipe-update', kwargs={'pk':1})
    assert resolve(path).view_name == 'recipe-update'

def test_api_url():
    path = reverse('api-root')
    assert resolve(path).view_name == 'api-root'

def test_api_recipe_list_url():
    path = reverse('recipe-list')
    assert resolve(path).view_name == 'recipe-list'

def test_api_recipe_detail_url():
    path = reverse('recipe-detail', kwargs={'pk':1})
    assert resolve(path).view_name == 'recipe-detail'

def test_api_recipe_all_list_url():
    path = reverse('recipe-all-list')
    assert resolve(path).view_name == 'recipe-all-list'

def test_api_recipe_all_detail_url():
    path = reverse('recipe-all-detail', kwargs={'pk':1})
    assert resolve(path).view_name == 'recipe-all-detail'







