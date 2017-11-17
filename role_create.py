import Blog as blog
blog.db.drop_all()
blog.db.create_all()

#roles
admin_role = blog.models.user.Role(rolename='Administrator')
anonymous_role = blog.models.user.Role(rolename='Anonymous')
common_role = blog.models.user.Role(rolename='Common Role')
moderator_role = blog.models.user.Role(rolename='Moderator')

#permission
follow_permission = blog.models.user.Permission(permission='FOLLOW')
comment_permission = blog.models.user.Permission(permission='COMMENT')
writeing_permission = blog.models.user.Permission(permission='WRITING')
moderate_comment_permission = blog.models.user.Permission(permission='MODERATE_COMMENT')
admin_permission = blog.models.user.Permission(permission='ADMINSTER')

#admin_role Authentication
admin_role.permissions.append(admin_permission)
admin_role.permissions.append(follow_permission)
admin_role.permissions.append(comment_permission)
admin_role.permissions.append(writeing_permission)
admin_role.permissions.append(moderate_comment_permission)

#moderator_role Authentication
moderator_role.permissions.append(follow_permission)
moderator_role.permissions.append(writeing_permission)
moderator_role.permissions.append(comment_permission)
moderator_role.permissions.append(moderate_comment_permission)

#common_role Authentication
common_role.permissions.append(follow_permission)
common_role.permissions.append(writeing_permission)
common_role.permissions.append(comment_permission)

#There are no Authentications for anonymous_role

blog.db.session.add(admin_role)
blog.db.session.add(moderator_role)
blog.db.session.add(common_role)
blog.db.session.add(anonymous_role)

blog.db.session.add(admin_permission)
blog.db.session.add(moderate_comment_permission)
blog.db.session.add(follow_permission)
blog.db.session.add(comment_permission)
blog.db.session.add(writeing_permission)




blog.db.session.commit()

for role in blog.models.user.Role.query.all():
    print(role.id, role.rolename)
    for permission in role.permissions:
        print("     ", permission.id, permission.permission)
