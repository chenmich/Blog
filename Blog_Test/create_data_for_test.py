import os
import sys
sys.path.append('.')
import unittest
from Blog import db, create_app
from Blog.models import Role, role_name, Permission, permission_name, User, Post, Post_User

def create_base_row(db):    
        #roles
        admin_role = Role(rolename=role_name.admin)
        anonymous_role = Role(rolename=role_name.anonymous)
        common_role = Role(rolename=role_name.common)
        moderator_role = Role(rolename=role_name.moderator)

        #permission
        follow_permission = Permission(permission=permission_name.follow)
        comment_permission = Permission(permission=permission_name.comment)
        writing_permission = Permission(permission=permission_name.writing)
        moderate_comment_permission = Permission(permission=permission_name.moderate_comment)
        admin_permission = Permission(permission=permission_name.admin)

        #admin_role Authentication
        admin_role.permissions.append(admin_permission)
        admin_role.permissions.append(follow_permission)
        admin_role.permissions.append(comment_permission)
        admin_role.permissions.append(writing_permission)
        admin_role.permissions.append(moderate_comment_permission)

        #moderator_role Authentication
        moderator_role.permissions.append(follow_permission)
        moderator_role.permissions.append(writing_permission)
        moderator_role.permissions.append(comment_permission)
        moderator_role.permissions.append(moderate_comment_permission)

        #common_role Authentication
        common_role.permissions.append(follow_permission)
        common_role.permissions.append(writing_permission)
        common_role.permissions.append(comment_permission)

        #There are no Authentications for anonymous_role

        db.session.add(admin_role)
        db.session.add(moderator_role)
        db.session.add(common_role)
        db.session.add(anonymous_role)

        db.session.add(admin_permission)
        db.session.add(moderate_comment_permission)
        db.session.add(follow_permission)
        db.session.add(comment_permission)
        db.session.add(writing_permission)


        micheal = User(username='micheal', 
                        email='micheal@163.com', 
                        password='111111',
                        role=admin_role)

        lrq = User(username='lrq',
                    email='lrq@163.com',
                    password='111111',
                    role=admin_role
                )

        kfl = User(username='kfl',
                    email='kfl@163.com',
                    password='111111',
                    role=admin_role
                )

        zyq = User(username='zyq',
                    email='zyq@163.com',
                    password='111111',
                    role=admin_role
                )

        zl = User(username='zl',
                   email='zl@163.com',
                   password='111111',
                   role=moderator_role
                )

        ny = User(username='ny',
                   email='ny@163.com',
                   password='111111',
                   role=moderator_role
                )

        lzj = User(username='lzj',
                    email='lzj@163.com',
                    password='111111',
                    role=common_role
                )
        
        db.session.add_all([micheal, lrq, zyq, 
                            kfl, zl, ny, lzj])
        db.session.commit()


    