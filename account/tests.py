from django.test import TestCase
from account import models as amod
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


class UserClassTest(TestCase):

    fixtures = ['data.yaml']


    def setUp(self):
        self.u1 = amod.User()
        self.u1.first_name = 'Lisa'
        self.u1.last_name = 'Simpson'
        self.u1.email = 'lisa@simpsons.com'
        self.u1.set_password('password')
        self.u1.address = '123 Road St'
        self.u1.city = 'Townsville'
        self.u1.state = 'TX'
        self.u1.zip = '12363'
        self.u1.birthdate = '1/1/76'
        self.u1.salary = 65000
        self.u1.is_staff = True
        self.u1.save()

        self.u2 = amod.User.objects.get(email='homer@simpsons.com')

    def test_load_save(self):
        """Test creating, saving, and reloading a user"""

        u2 = amod.User.objects.get(email='lisa@simpsons.com')
        self.assertEqual(self.u1.first_name, u2.first_name)
        self.assertEqual(self.u1.last_name, u2.last_name)
        self.assertEqual(self.u1.email, u2.email)
        self.assertEqual(self.u1.password, u2.password)
        self.assertTrue(u2.check_password('password'))
        self.assertEqual(u2.address, self.u1.address)
        self.assertEqual(u2.city, self.u1.city)
        self.assertEqual(u2.state, self.u1.state)
        self.assertEqual(u2.zip, self.u1.zip)
        self.assertEqual(u2.birthdate, self.u1.birthdate)
        self.assertEqual(u2.salary, self.u1.salary)

    # def test_create_group(self):
    #     """Test for adding the test user to a group"""
    #     g1 = Group()
    #     g1.name = 'TestPeople'
    #     g1.save()
    #     self.u1.groups.add(g1)
    #     self.u1.save()
    #     #self.assertEqual(self.u1.groups.get(id=g1.id))
    #     g1.permissions.add(Permission.objects.get(id=4))
    #     for p in Permission.objects.all():
    #         print(p.codename)
    #         print(p.name)
    #         print(p.content_type)
    #         self.u1.user_permissions.add(p)
    #     p = Permission()
    #     p.codename = 'change_product_price'
    #     p.name = 'Change the price of a product'
    #     p.content_type = ContentType.objects.get(id=1)
    #     p.save()

    def test_group(self):
        """Test to make sure user can be added to a group"""
        self.u2.groups.add(Group.objects.get(name='Sales'))
        self.assertTrue(self.u2.groups.filter(name='Sales').exists())
        self.assertTrue(self.u2.has_perm('admin.add_user'))



    def test_user_permission(self):
        """Test to make sure user receive permissions correctly"""
        p = Permission()
        p.codename = 'change_product_price'
        p.name = 'Change the price of a product'
        p.content_type = ContentType.objects.get(id=1)
        p.save()
        self.u1.user_permissions.add(p)
        self.assertTrue(self.u1.has_perm('admin.change_product_price'))



