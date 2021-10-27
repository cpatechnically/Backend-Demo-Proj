import datetime 
import os
import random
import string

from django.utils import timezone
from django.utils.text import slugify

'''
random_string_generator is located here:
http://joincfe.com/blog/random-string-generator-in-python/
'''

from django.db import connection

# def my_custom_sql(self):
#     with connection.cursor() as cursor:
#         cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
#         cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
#         row = cursor.fetchone()

#     return row

def mysql_alter_table_remove():
    with connection.cursor() as cursor:
        cursor.execute("ALTER TABLE course DROP series_ref ")
        # cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        # row = cursor.fetchone()
    #return row


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


print(random_string_generator())

print(random_string_generator(size=50))


#https://www.codingforentrepreneurs.com/blog/a-unique-slug-generator-for-django/

#from yourapp.utils import random_string_generator

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        try:
            slug = slugify(instance.title)
        except:
            pass
            try: 
                slug = slugify(instance.name)
            except:
                slug = slugify("no_name_or_title")

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug




if __name__=='__main__':
    mysql_alter_table_remove()
