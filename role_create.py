import Blog as blog
blog.db.drop_all()
blog.db.create_all()

#roles
admin_role = blog.models.user.Role(
    rolename=blog.models.user.role_name.admin)
anonymous_role = blog.models.user.Role(
    rolename=blog.models.user.role_name.anonymous)
common_role = blog.models.user.Role(
    rolename=blog.models.user.role_name.common)
moderator_role = blog.models.user.Role(
    rolename=blog.models.user.role_name.moderator)

#permission
follow_permission = blog.models.user.Permission(
    permission=blog.models.user.permission_name.follow)
comment_permission = blog.models.user.Permission(
    permission=blog.models.user.permission_name.comment)
writing_permission = blog.models.user.Permission(
    permission=blog.models.user.permission_name.writing)
moderate_comment_permission = blog.models.user.Permission(
    permission=blog.models.user.permission_name.moderate_comment)
admin_permission = blog.models.user.Permission(
    permission=blog.models.user.permission_name.admin)

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

blog.db.session.add(admin_role)
blog.db.session.add(moderator_role)
blog.db.session.add(common_role)
blog.db.session.add(anonymous_role)

blog.db.session.add(admin_permission)
blog.db.session.add(moderate_comment_permission)
blog.db.session.add(follow_permission)
blog.db.session.add(comment_permission)
blog.db.session.add(writing_permission)




blog.db.session.commit()


